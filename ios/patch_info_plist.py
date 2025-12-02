#!/usr/bin/env python3

import sys
import os

# --- Path Setup to find the main build script ---
# Add the 'utils' directory to the system path to find the build module
script_dir = os.path.dirname(os.path.realpath(__file__))
utils_dir = os.path.join(script_dir, '..', 'utils')
sys.path.insert(0, utils_dir)

# Import only the function we need from the main build script
from build import patch_info_plist

def main():
    """
    Wrapper script that calls the centralized patch_info_plist function.
    """
    if len(sys.argv) < 2:
        print(f"Usage: {os.path.basename(sys.argv[0])} <path_to_info.plist>")
        sys.exit(1)

    info_plist_path = sys.argv[1]
    patch_info_plist(info_plist_path)

if __name__ == "__main__":
    main()
