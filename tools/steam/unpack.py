#!/usr/bin/env python3

import sys
import os

# --- Path Setup to find the main build script ---
# Add the 'utils' directory to the system path to find the build module
script_dir = os.path.dirname(os.path.realpath(__file__))
utils_dir = os.path.join(script_dir, '..', 'utils')
sys.path.insert(0, utils_dir)

# Import only the function we need from the main build script
from build import unpack_dat

def main():
    """
    Wrapper script that calls the centralized unpack_dat function.
    """
    if len(sys.argv) < 2:
        print(f"Usage: {os.path.basename(sys.argv[0])} <path_to_sworcery.dat> [output_directory]")
        sys.exit(1)

    dat_path = sys.argv[1]
    # If output_dir is not provided, set it to None.
    # The unpack_dat function will then default to the dat_path's directory.
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    # Call unpack_dat to extract everything, without any specific file list.
    # The file_list parameter will be None by default, triggering extractall().
    unpack_dat(dat_path, output_directory=output_dir)

if __name__ == "__main__":
    main()
