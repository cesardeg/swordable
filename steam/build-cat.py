#!/usr/bin/env python3

import sys
import os

# --- Path Setup to find the main build script ---
# Add the 'utils' directory to the system path to find the build module
script_dir = os.path.dirname(os.path.realpath(__file__))
utils_dir = os.path.join(script_dir, '..', 'utils')
sys.path.insert(0, utils_dir)

# Import only the function we need from the main build script
from build import create_cat_file

def main():
    """
    Wrapper script that calls the centralized create_cat_file function.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {os.path.basename(sys.argv[0])} <path_to_sworcery.dat_or_its_directory>")
        sys.exit(1)

    input_path = sys.argv[1]

    if os.path.isdir(input_path):
        res_dir = input_path
    elif os.path.isfile(input_path):
        res_dir = os.path.dirname(input_path)
    else:
        print(f"Error: Path not found or is not a valid file/directory: {input_path}")
        sys.exit(1)

    create_cat_file(res_dir)

if __name__ == "__main__":
    main()