#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess
import argparse

# --- Path Setup ---
script_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.dirname(script_dir)
common_tools_dir = os.path.join(script_dir, 'common')

# Add common tools to path for bootstrap import
sys.path.insert(0, common_tools_dir)

from bootstrap import ensure_environment

def main():
    parser = argparse.ArgumentParser(description="Bundle the S:S&S EP Patcher into a standalone executable.")
    parser.add_argument("locale", nargs="?", default="es", choices=["es", "pt"], help="Locale to bundle (default: es)")
    args = parser.parse_args()

    # 1. Ensure environment and dependencies
    print(f"--- Bootstrapping Environment for Locale: {args.locale} ---")
    ensure_environment(required_packages=['pyinstaller', 'Pillow'])

    # 2. Check if build data exists
    data_build_dir = os.path.join(project_root, "build", "steam", args.locale)
    dat_path = os.path.join(data_build_dir, "sworcery.dat")
    cat_path = os.path.join(data_build_dir, "sworcery.dat.cat")

    if not os.path.exists(dat_path):
        print(f"Error: Translation data not found in {data_build_dir}")
        print(f"Please run first: ./tools/steam/build.sh sworcery.dat {args.locale}")
        sys.exit(1)

    # 3. Prepare ephemeral assets for PyInstaller
    temp_assets_dir = os.path.join(project_root, "build", "temp_assets")
    assets_subfolder = os.path.join(temp_assets_dir, "assets")
    
    if os.path.exists(temp_assets_dir):
        shutil.rmtree(temp_assets_dir)
    
    os.makedirs(assets_subfolder)
    
    shutil.copy2(dat_path, temp_assets_dir)
    if os.path.exists(cat_path):
        shutil.copy2(cat_path, temp_assets_dir)
    
    # Save target locale for the bundled app
    with open(os.path.join(temp_assets_dir, "locale.txt"), "w") as f:
        f.write(args.locale)
    
    bg_path = os.path.join(project_root, "installer", "assets", "background.png")
    if os.path.exists(bg_path):
        shutil.copy2(bg_path, assets_subfolder)
    
    icon_png = os.path.join(project_root, "installer", "assets", "icon.png")
    if os.path.exists(icon_png):
        shutil.copy2(icon_png, assets_subfolder)

    # 4. Define output naming
    suffix = "ES" if args.locale == "es" else "PT"
    output_name = f"Sworcery_Patcher_{suffix}"
    output_dir = os.path.join(project_root, "build", "installer", args.locale)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 5. Run PyInstaller
    print(f"--- Running PyInstaller for {output_name} ---")
    
    # Use ';' as separator for Windows, ':' for Mac/Linux
    separator = ";" if sys.platform == "win32" else ":"
    icon_file = os.path.join(project_root, "installer", "assets", "icon.ico") if sys.platform == "win32" else icon_png
    
    work_path = os.path.join(project_root, "build", "pyinstaller_work")
    spec_path = os.path.join(project_root, "build", "pyinstaller_spec")

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--noconsole",
        "--add-data", f"{temp_assets_dir}/*{separator}.",
        "--name", output_name,
        "--clean",
        "--icon", icon_file,
        "--workpath", work_path,
        "--specpath", spec_path,
        "installer/patcher.py"
    ]

    try:
        # Run from project root
        subprocess.check_call(cmd, cwd=project_root)
        
        # 6. Move result to the requested location
        dist_dir = os.path.join(project_root, "dist")
        
        if sys.platform == "darwin":
            app_bundle = os.path.join(dist_dir, f"{output_name}.app")
            final_dest = os.path.join(output_dir, f"{output_name}.app")
            if os.path.exists(app_bundle):
                if os.path.exists(final_dest):
                    shutil.rmtree(final_dest)
                shutil.move(app_bundle, output_dir)
            else:
                shutil.move(os.path.join(dist_dir, output_name), output_dir)
        elif sys.platform == "win32":
            shutil.move(os.path.join(dist_dir, f"{output_name}.exe"), output_dir)
        else:
            # Linux / Others
            shutil.move(os.path.join(dist_dir, output_name), output_dir)

        print(f"--- Bundle Complete: {os.path.join(output_dir, output_name)} ---")

    except subprocess.CalledProcessError as e:
        print(f"Error during PyInstaller execution: {e}")
        sys.exit(1)
    finally:
        # Cleanup ephemeral build artifacts
        print("--- Cleaning up temporary build artifacts ---")
        for path in [temp_assets_dir, os.path.join(project_root, "dist"), work_path, spec_path]:
            if os.path.exists(path):
                try:
                    if os.path.isdir(path):
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
                except Exception as e:
                    print(f"Warning: Could not remove {path}: {e}")

if __name__ == "__main__":
    main()
