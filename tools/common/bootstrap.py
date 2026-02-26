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

    # Determine the project root (going up 2 levels from tools/common/)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    venv_path = os.path.join(project_root, "venv")

    # CI Detection: GitHub Actions runners already provide a clean environment.
    # We skip venv creation/re-launch to avoid os.execv race conditions on Windows.
    is_ci = os.getenv("GITHUB_ACTIONS") == "true"

    if is_ci:
        print("CI Environment detected. Skipping virtual environment setup.")
        # In CI, we just use the current python and install dependencies globally.
    else:
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
    # Update pip first to avoid issues
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

    if required_packages:
        for package in required_packages:
            # Map common import names to pip package names (e.g., PIL -> Pillow)
            pip_name = package
            if package == "PIL": pip_name = "Pillow"
            if package == "PyInstaller": pip_name = "pyinstaller"
            
            try:
                importlib.import_module(package)
            except ImportError:
                print(f"Dependency '{package}' not found. Installing '{pip_name}'...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
                print(f"'{pip_name}' has been successfully installed.")