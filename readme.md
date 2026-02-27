# Superbrothers Sword & Sworcery EP Localization

This repository contains the community localization files and tools for Superbrothers: Sword & Sworcery EP. It provides everything necessary to translate the game into Spanish, Portuguese, and other custom languages.

The project is organized into the following core folders:

- **`data/`**: The raw assets needed for translation.
  - `locales/`: Contains the actual TSV translation dictionaries for various languages.
  - `fonts/`: Includes custom font patches required to support special characters (like accents and ñ) missing in the vanilla game.
- **`tools/`**: The backend build scripts required to decompile the game's core archives, inject the new fonts/locales, and legally recompile them. It includes separate pipelines for the `steam` (PC/Mac/Linux) and `ios` versions of the game.
- **`patcher/`**: A modern, lightweight Desktop Application built with Tauri (Rust + JS). This beautiful App automates the secure installation, backup, and removal of the generated translations on end-users' machines.

---

## 🚀 Game Patcher (For Users)

If you just want to play the game in Spanish or Portuguese, you don't need to compile anything manually. Simply download and run our automated patcher.

Please refer to the Desktop App instructions here: **[patcher/README.md](patcher/README.md)**

---

## 🛠️ Manual Compilation (For Developers)

If you are a developer or translator looking to build the raw `.dat` patches yourself, or want to contribute a new language:

1. Obtain a clean `sworcery.dat` from your game's installation.
2. Read the build pipeline documentation: **[tools/steam/readme.md](tools/steam/readme.md)**.

## Contributing

If you would like to contribute translations, fix typos, or improve the patcher's codebase, feel free to submit a pull request!

## Legal

Please note that any modifications made to your game files are at your own risk (though the patcher creates backups automatically). Ensure that you own a legal copy of Superbrothers: Sword & Sworcery EP before proceeding with using any of these tools. This project does NOT distribute copyrighted original game files.

## Credits

Special thanks to all contributors for their efforts in localizing and improving the game experience for the community.
