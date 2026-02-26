#!/usr/bin/env python3

import sys
import os

# --- Path Setup to find the main build script ---
# Add the 'utils' directory to the system path to find the build module
script_dir = os.path.dirname(os.path.realpath(__file__))
utils_dir = os.path.join(script_dir, '..', 'utils')
sys.path.insert(0, utils_dir)

# Import only the function we need from the main build script
from build import create_dat_from_folder

def main():
    """
    Wrapper script that calls the centralized create_dat_from_folder function.
    It packs all contents of a source directory into a new sworcery.dat file.
    """
    if len(sys.argv) < 2:
        print(f"Usage: {os.path.basename(sys.argv[0])} <source_directory> [destination_directory]")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else None

    if dest_dir is None:
        # If no destination is provided, it becomes a sibling of the source directory.
        dest_dir = os.path.dirname(source_dir)

    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    output_dat_path = os.path.join(dest_dir, "sworcery.dat")

    create_dat_from_folder(source_dir, output_dat_path)

if __name__ == "__main__":
    main()