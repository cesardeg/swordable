# S:S&S EP - Translation Installer

This directory contains the graphical patcher (GUI) for end-users to install the translation on their computers.

## 🚀 Usage for Users
If you are running the compiled binary (`Sworcery_Patcher_ES.exe` or `.app`):
1.  Open the program.
2.  The installer will automatically attempt to detect your Steam folder.
3.  Click **INSTALL TRANSLATION**.

## 🛠️ Usage for Developers
If you want to run the Python script directly for testing:

### 1. Prerequisite: Build the Data
The installer requires the patched `.dat` and `.cat` files. If you don't have them, you must generate them first from the project root:
```bash
./tools/steam/build.sh sworcery.dat es
```

### 2. Local Execution
Once the files exist in `build/steam/es/`, you can launch the interface:
```bash
python3 installer/patcher.py --locale es
```

### 3. Final Bundling
To create the executable distributed to users:
```bash
python3 tools/bundle_patcher.py es
```

---

## Technical Features
- **Auto-Detection**: Supports Steam on Windows, Mac, and Linux.
- **Secure Backup**: Automatic `.bak` file creation so users never lose their original files.
- **Immersive Design**: Custom interface with game art.

---

## 🛠️ Troubleshooting

### Missing "tkinter" on macOS
If you see an error about `MISSING SYSTEM DEPENDENCY (tkinter)`, it's because the version of Python that comes with macOS is "stripped" and doesn't include the graphical engine.

**Fix**: Install a full version of Python via Homebrew:
```bash
brew install tcl-tk python-tk
```

### Missing "tkinter" on Linux
On Ubuntu/Debian based systems, you may need to install it manually:
```bash
sudo apt install python3-tk
```
