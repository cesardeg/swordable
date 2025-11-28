#!/usr/bin/env python3

import os
import sys
import subprocess

def main():
    """
    This is a wrapper script. It calls the main build.py script at the
    project root with the 'steam' platform argument.
    """
    # Get the directory of this script (e.g., /path/to/swordable/steam)
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Find the main build.py script at the project root (one level up)
    project_root = os.path.dirname(script_dir)
    main_build_script = os.path.join(project_root, 'utils', 'build.py')

    # Construct the command to call the main script
    # e.g., "python3 /path/to/build.py steam [args...]"
    command = [sys.executable, main_build_script, 'steam'] + sys.argv[1:]

    # Execute the command and exit with its status code
    result = subprocess.run(command)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()