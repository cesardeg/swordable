#!/usr/bin/env python3

import argparse
import os
import sys
import plistlib
import shutil
import struct
import zipfile

# --- Environment and Dependency Setup ---
# Since this script is in 'utils', the project root is one level up.
project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
utils_dir = os.path.join(project_root, 'utils')
sys.path.insert(0, utils_dir)

# Dynamically add script directories to path for imports
sys.path.insert(0, os.path.join(project_root, 'ios'))

from bootstrap import ensure_environment

# Ensure all potential dependencies are met
ensure_environment(required_packages=['py7zr'])

import py7zr

# --- Global Constants ---
SWORCERY_DAT_PASSWORD = "GdHGhd4yuNF"

# =============================================================================
# --- 1. General Helper Functions ---
# =============================================================================

def copy_files(destination_dir, locale, platform):
    """Migrated logic from copy_files.sh."""
    print(f"Copying files for locale '{locale}' and platform '{platform}' to '{destination_dir}'...")
    language_name = get_language_name(locale)

    files_txt_name = f"{platform}_cyrillic.txt" if locale == "ru" else f"{platform}_latin.txt"
    files_txt_path = os.path.join(utils_dir, "files", files_txt_name)

    locales_folder = os.path.join(project_root, "locales", language_name)
    fonts_folder = os.path.join(project_root, "fonts", "cyrillic" if locale == "ru" else "patched")

    with open(files_txt_path, 'r') as f:
        for file_rel_path in f:
            file_rel_path = file_rel_path.strip()
            if not file_rel_path:
                continue

            source_path = ""
            dest_path = os.path.join(destination_dir, file_rel_path)

            if file_rel_path.startswith('fonts/'):
                # e.g., fonts/conduit_itc.fnt -> conduit_itc.fnt
                base_name = os.path.basename(file_rel_path)
                source_path = os.path.join(fonts_folder, base_name)
            elif file_rel_path.startswith('locales/'):
                base_name = os.path.basename(file_rel_path)
                source_path = os.path.join(locales_folder, base_name)

            if not source_path or not os.path.exists(source_path):
                print(f"Warning: Source file not found, skipping: {source_path or file_rel_path}")
                continue

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy(source_path, dest_path)
    print("File copy complete.")

def get_language_name(locale_code):
    """Maps locale code to full language name."""
    mapping = {"es": "spanish", "fr": "french", "it": "italian", "pt": "portuguese", "ru": "russian"}
    if locale_code not in mapping:
        print(f"Error: Invalid locale '{locale_code}'. Valid locales are: {', '.join(mapping.keys())}")
        sys.exit(1)
    return mapping[locale_code]

# =============================================================================
# --- 2. Steam-Specific Helper Functions ---
# =============================================================================

def unpack_dat(dat_path, output_directory=None, file_list=None):
    """Unpacks a sworcery.dat file."""
    if not os.path.isfile(dat_path):
        print(f"Error: The sworcery.dat file does not exist at: {dat_path}")
        sys.exit(1)

    if output_directory is None:
        output_directory = os.path.dirname(dat_path)

    os.makedirs(output_directory, exist_ok=True)

    print(f"Unpacking '{dat_path}' to '{output_directory}'...")
    try:
        # The password is required for the original game archives.
        with py7zr.SevenZipFile(dat_path, 'r', password=SWORCERY_DAT_PASSWORD) as archive:
            if file_list:
                archive.extract(path=output_directory, targets=file_list)
            else:
                archive.extractall(path=output_directory)
        print("Unpacking complete.")
    except Exception as e:
        print(f"Error unpacking file: {e}")
        sys.exit(1)

def repack_dat(source_dir, files_to_repack=None, dat_path=None):
    """
    Repacks (updates) a sworcery.dat file with new/modified files.
    Uses 'a' (append/update) mode of 7zr.
    If dat_path is not provided, it defaults to 'sworcery.dat' as a sibling to source_dir.
    """
    if dat_path is None:
        parent_dir = os.path.dirname(source_dir)
        dat_path = os.path.join(parent_dir, "sworcery.dat")

    if not os.path.isdir(source_dir):
        print(f"Error: Source directory for repacking not found: {source_dir}")
        sys.exit(1)

    print(f"Repacking '{dat_path}' with localized files from '{source_dir}'...")
    try:
        files_map = {}
        if files_to_repack:
            # Case 1: A specific list of files is provided.
            print("Updating with a specific list of files...")
            files_map = {os.path.join(source_dir, f): f for f in files_to_repack if os.path.exists(os.path.join(source_dir, f))}
        else:
            # Case 2: No list provided. Repack all files from the source directory.
            print("Updating with all files from the source directory...")
            files_map = {os.path.join(source_dir, f): f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))}

        with py7zr.SevenZipFile(dat_path, 'a', password=SWORCERY_DAT_PASSWORD) as archive:
            archive.write(files_map)
        print("Repacking complete.")
    except Exception as e:
        print(f"Error repacking file: {e}")
        sys.exit(1)

def create_dat_from_folder(source_dir, output_dat_path):
    """
    Creates a new sworcery.dat file from a source folder.
    This will overwrite any existing file at output_dat_path.
    """
    print(f"Creating new archive '{output_dat_path}' from folder '{source_dir}'...")
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory not found: {source_dir}")
        sys.exit(1)

    try:
        # Use 'w' (write) mode to create a new archive.
        with py7zr.SevenZipFile(output_dat_path, 'w', password=SWORCERY_DAT_PASSWORD) as archive:
            archive.writeall(source_dir, arcname='') # arcname='' puts files at the root of the archive
        print("Archive creation complete.")
    except Exception as e:
        print(f"Error creating archive: {e}")
        sys.exit(1)

def create_cat_file(res_dir="."):
    """
    Generates the sworcery.dat.cat file.
    Logic moved from steam/build-cat.py.
    """
    # Constants for magic numbers, offsets, and byte sizes
    ENDREC_SIGNATURE = 0x06054B50
    HEADER_SIGNATURE = 0x02014B50
    HEADER_PTHLNG_OFFSET = 28
    HEADER_ABOUTE_OFFSET = 30
    HEADER_RESADR_OFFSET = 46
    BYTES_INT_OFFSET = 12  # Offset for skipping bytes when seeking with BYTES_INT
    FILE_SEARCH_LIMIT = 100
    BYTES_INT = 4
    BYTES_SHORT = 2

    def find_central_header(fp):
        """
        Finds the start of the central directory header in a ZIP file.
        It does this by seeking from the end of the file and looking for the
        ENDREC_SIGNATURE.
        """
        found = False
        fstadr = 0
        file_size = fp.seek(0, 2)  # Get the size of the file

        for i in range(file_size - BYTES_INT, file_size - FILE_SEARCH_LIMIT, -1):
            fp.seek(i)  # Seek from the end of the file
            ch = struct.unpack("I", fp.read(BYTES_INT))[0]
            if ch == ENDREC_SIGNATURE:
                fp.seek(BYTES_INT_OFFSET, 1)  # Seek BYTES_INT_OFFSET bytes ahead from the current position
                fstadr = struct.unpack("I", fp.read(BYTES_INT))[0]
                found = True
                break

        if not found:
            print("Error: ENDREC_SIGNATURE not found in the file.")
            sys.exit(1)

        return fstadr

    dat_file_path = os.path.join(res_dir, "sworcery.dat")
    cat_file_path = os.path.join(res_dir, "sworcery.dat.cat")

    # 1. Check if the source sworcery.dat file exists.
    if not os.path.isfile(dat_file_path):
        print(f"Error: 'sworcery.dat' not found in directory: {res_dir}")
        sys.exit(1)

    print(f"Building '{cat_file_path}'...")
    try:
        # 2. Open the .cat file in 'wb' (write binary) mode. This will automatically
        #    create the file or overwrite it if it already exists.
        with open(dat_file_path, "rb") as fpr, open(cat_file_path, "wb") as fpw:
            resadr = find_central_header(fpr)
            resnum = 0
            while True:
                fpr.seek(resadr)
                if struct.unpack("I", fpr.read(BYTES_INT))[0] != HEADER_SIGNATURE:
                    break

                fpr.seek(resadr + HEADER_PTHLNG_OFFSET)
                pthlng = struct.unpack("H", fpr.read(BYTES_SHORT))[0]
                aboute = struct.unpack("H", fpr.read(BYTES_SHORT))[0]
                fpr.seek(resadr + HEADER_RESADR_OFFSET)
                respath = fpr.read(pthlng).decode("utf-8").lower()

                fpw.write(struct.pack("I", pthlng) + respath.encode("utf-8") + struct.pack("II", resadr, resnum))
                resnum += 1
                resadr += HEADER_RESADR_OFFSET + pthlng + aboute
    except (IOError, struct.error) as e:
        print(f"Error during .cat file creation: {e}")
        sys.exit(1)

# =============================================================================
# --- 3. iOS-Specific Helper Functions ---
# =============================================================================

def patch_info_plist(plist_path):
    """Migrated logic from patch_info_plist.py."""
    print(f"Patching Info.plist at: {plist_path}")
    with open(plist_path, "rb") as fp:
        plist = plistlib.load(fp)

    # --- Legacy Orientation Lock (for iOS 12 and older) ---
    # This tells the app to only support Portrait mode.
    plist["UISupportedInterfaceOrientations"] = ["UIInterfaceOrientationPortrait"]
    plist["UISupportedInterfaceOrientations~ipad"] = ["UIInterfaceOrientationPortrait"]

    # Force Full-Screen Mode (iPad Specific Fix):
    # On modern iPadOS, the system may still ignore legacy orientation keys to support multitasking.
    # Setting UIRequiresFullScreen to true tells iPadOS that this app cannot do multitasking
    # and MUST run full-screen, which forces it to respect the orientation lock.
    plist["UIRequiresFullScreen"] = True
    print("Set UIRequiresFullScreen to True to enforce orientation lock on iPad.")
            
    with open(plist_path, "wb") as fp:
        plistlib.dump(plist, fp)
    print("Info.plist patched successfully.")

# =============================================================================
# --- 4. Main Build Orchestrator Functions ---
# =============================================================================

def build_steam(args):
    """Orchestrates the build for the Steam platform."""
    print(f"--- Starting Steam build for locale: {args.locale} ---")
    if not os.path.isfile(args.dat_path):
        print(f"Error: The sworcery.dat file does not exist at: {args.dat_path}")
        sys.exit(1)

    res_dir = os.path.join(project_root, "build", "steam", args.locale)
    os.makedirs(res_dir, exist_ok=True)

    # 1. Copy original .dat file
    shutil.copy(args.dat_path, res_dir)
    dat_file_in_build = os.path.join(res_dir, "sworcery.dat")

    # 2. Copy localized files into the build directory.
    copy_files(res_dir, args.locale, "desk")

    # 3. Determine which files to repack based on locale
    files_txt_name = "desk_cyrillic.txt" if args.locale == "ru" else "desk_latin.txt"
    files_txt_path = os.path.join(utils_dir, "files", files_txt_name)
    try:
        with open(files_txt_path, 'r') as f:
            files_to_repack = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File list not found at {files_txt_path}")
        sys.exit(1)

    # 4. Repack the archive
    repack_dat(res_dir, files_to_repack, dat_file_in_build)

    # 5. Build the .cat file
    create_cat_file(res_dir)

    print(f"--- Steam build for locale '{args.locale}' completed successfully! ---")
    print(f"Output located in: {res_dir}")

def build_ios(args):
    """Orchestrates the build for the iOS platform."""
    print(f"--- Starting iOS build for locale: {args.locale} ---")
    if not os.path.isfile(args.ipa_path):
        print(f"Error: IPA file not found at: {args.ipa_path}")
        sys.exit(1)

    res_dir = os.path.join(project_root, "build", "ios", args.locale)
    os.makedirs(res_dir, exist_ok=True)

    temp_dir = os.path.join(res_dir, "temp_unzip")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    try:
        # 1. Unzip IPA
        print(f"Unzipping '{args.ipa_path}'...")
        import plistlib
        with zipfile.ZipFile(args.ipa_path, 'r') as ipa_zip:
            ipa_zip.extractall(temp_dir)

        payload_dir = os.path.join(temp_dir, "Payload")
        app_folder_name = next((d for d in os.listdir(payload_dir) if d.endswith(".app")), None)
        if not app_folder_name:
            print("Error: No .app folder found inside the IPA Payload.")
            sys.exit(1)
        app_folder_path = os.path.join(payload_dir, app_folder_name)

        # 2. Copy localized files
        copy_files(app_folder_path, args.locale, "mobile")

        # 3. Patch Info.plist
        patch_info_plist(os.path.join(app_folder_path, "Info.plist"))

        # 4. Re-zip into a new IPA
        ipa_basename = os.path.basename(args.ipa_path)
        modified_ipa_name = f"{os.path.splitext(ipa_basename)[0]}-{args.locale}.ipa"
        modified_ipa_path = os.path.join(res_dir, modified_ipa_name)

        print(f"Repackaging into '{modified_ipa_path}'...")
        with zipfile.ZipFile(modified_ipa_path, 'w', zipfile.ZIP_DEFLATED) as new_ipa:
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, temp_dir)
                    new_ipa.write(full_path, arcname)

        print(f"--- iOS build for locale '{args.locale}' completed successfully! ---")
        print(f"Output located at: {modified_ipa_path}")

    finally:
        # 5. Clean up temp directory
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

# =============================================================================
# --- 5. Main Script Entrypoint ---
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Unified build script for Sword & Sworcery localization.")
    subparsers = parser.add_subparsers(dest="platform", required=True, help="The platform to build for.")

    # Define shared locale options to avoid repetition
    AVAILABLE_LOCALES = ["es", "fr", "it", "pt", "ru"]
    DEFAULT_LOCALE = "es"

    # --- Steam Parser ---
    parser_steam = subparsers.add_parser("steam", help="Build for Steam (desktop).")
    parser_steam.add_argument("dat_path", help="Path to the original sworcery.dat file.")
    parser_steam.add_argument("-l", "--locale", default=DEFAULT_LOCALE, choices=AVAILABLE_LOCALES, help="The locale to build.")
    parser_steam.set_defaults(func=build_steam)

    # --- iOS Parser ---
    parser_ios = subparsers.add_parser("ios", help="Build for iOS (mobile).")
    parser_ios.add_argument("ipa_path", help="Path to the original .ipa file.")
    parser_ios.add_argument("-l", "--locale", default=DEFAULT_LOCALE, choices=AVAILABLE_LOCALES, help="The locale to build.")
    parser_ios.set_defaults(func=build_ios)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()