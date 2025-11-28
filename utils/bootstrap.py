#!/usr/bin/env python3

import os
import sys
import subprocess
import importlib

def ensure_environment(required_packages=None):
    """
    Ensures the script is running in a project-specific virtual environment.

    - Creates a 'venv' if it doesn't exist at the project root.
    - Re-launches the script using the venv's Python interpreter if not already active.
    - Installs any packages from 'required_packages' that are not already installed.
    """
    if required_packages is None:
        required_packages = []

    # Determine the project root (assuming this script is in a subdirectory like 'utils')
    project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    venv_path = os.path.join(project_root, "venv")

    # Determine the python executable path within the venv
    python_executable = os.path.join(venv_path, "bin", "python")
    if sys.platform == "win32":
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")

    # 1. If venv doesn't exist, create it.
    if not os.path.isdir(venv_path):
        print(f"Virtual environment not found. Creating one at: {venv_path}")
        # Use the system's python to create the venv
        system_python = sys.executable
        subprocess.check_call([system_python, "-m", "venv", venv_path])
        print("Virtual environment created.")

    # 2. If the script is not running from the venv, re-launch it.
    if sys.executable != python_executable:
        print("Switching to the project's virtual environment...")
        os.execv(python_executable, [python_executable] + sys.argv)

    # 3. If we are in the venv, check and install dependencies.
    if required_packages:
        for package in required_packages:
            try:
                importlib.import_module(package)
            except ImportError:
                print(f"Dependency '{package}' not found. Installing...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"'{package}' has been successfully installed.")