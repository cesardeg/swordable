# IPA Modification Scripts

This project provides a set of scripts to modify IPA (iOS App Store Package) files. The scripts allow for patching the font, locale, and Info.plist files of an IPA, enabling you to generate modified IPAs with specific translations and fixes. This can be particularly useful for customizing and localizing iOS apps.

## Requirements

- Python 3.x
- `unzip` command-line tool
- OpenSSH (for `scp.sh` script)
- Jailbroken iPhone with OpenSSH (for `scp.sh` script)

## Getting Started

1. Clone the repository to your local machine:

```shell
git clone https://github.com/cesardeg/swordable.git
cd ios
```

2. Ensure that you have the necessary requirements installed, as mentioned in the Requirements section.

## Scripts

### build.sh

This script allows you to modify IPA files by patching the font, locale, and Info.plist files. It supports batch processing of multiple IPAs.

#### Usage:

```shell
./build.sh <ipa_path> [locale]
```

- `<ipa_path>`: The path to the IPA file or directory containing multiple IPAs.
- `[locale]` (optional): The desired locale ["es", "pt"]. Default is "es" (Spanish).

The modified IPAs will be saved in the `/build/ios` directory.

`locales/dialog.tsv` is not copied as-is. Credit lines whose `portrait` cell is `Logos/DolbyDigital` or `Logos/DigitalSurround` are removed during the copy. See [Missing credit logos](#missing-credit-logos). The same filter runs in `tools/common/build.py` when the platform is `ios`.

### patch_info_plist.py

This Python script is used to patch the Info.plist file of an IPA. It resolves a bug in iOS 16+ where the game is not playable due to the game rendering only in portrait mode.

#### Usage:

```shell
python patch_info_plist.py <info_plist_path>
```

- `<info_plist_path>`: The path to the Info.plist file.

### scp.sh

This script allows you to copy translation files to an iPhone with jailbreak and OpenSSH using SCP (Secure Copy). It connects to the iPhone and copies the necessary files to the appropriate directories.

#### Usage:

```shell
./scp.sh <remote_ip> [locale]
```

- `<remote_ip>`: The IP address of the remote iPhone.
- `[locale]` (optional): The desired locale. Default is "es" (Spanish).

Please note that you need to have the necessary permissions and setups in place for OpenSSH and Jailbroken iPhone with OpenSSH in order to use the `scp.sh` script.

`dialog.tsv` is filtered the same way as in `build.sh` before it is uploaded. The file in `data/locales/` is left unchanged.

---

## Appendix A: Platform-Specific Build Notes

### iOS / iPadOS Build

**iPadOS 16+ Orientation Lock Issue:**

Due to changes in how modern iPadOS handles multitasking (Stage Manager, Split View), the game may incorrectly rotate when the device is turned to landscape, breaking the "unsheathe" mechanic.

**Solution:** The application must be run in **Full Screen App Mode**.
- **To ensure correct behavior:** Go to `Settings > Home Screen & Multitasking > Stage Manager` and ensure it is turned **OFF** for the game. The game is not compatible with windowed multitasking modes.
- In Full Screen mode, the orientation lock works as intended. This is a known limitation of running a legacy application on a modern, multitasking-oriented OS.

### Missing credit logos

The credits are lines in `dialog.tsv`. A logo is not an image next to the text: the `portrait` column names a sprite, and the engine loads that sprite from `sprites/logos` when the line is shown.

These two names are in the PC/Steam logo sheet and in the credit script, and they are **not** in the iOS `sprites/logos` sheet:

| `portrait` | What the line is | Lines removed on iOS |
|---|---|---|
| `Logos/DolbyDigital` | Dolby Laboratories trademark, and the Dolby Digital Live PC-audio notice | 2 |
| `Logos/DigitalSurround` | DTS Digital Surround trademark | 1 |

Opening the credits asks the engine to draw every named portrait. On iOS that lookup fails for these two sprites and the app crashes. The notices are also PC audio copy, so dropping the lines does not remove an iOS credit that the player can actually see.

The other credit logos stay, because those sprites are on iOS: `Logos/superbrothers`, `Logos/capy`, `Logos/eightfour`, `Logos/omdc`, and `Logos/FMOD`.

**Do not delete the lines from `data/locales/*/dialog.tsv`.** Steam still has the sprites, and the same files are the Steam drop-in. The iOS copy is the only place they are cut:

- `tools/ios/build.sh` and `tools/common/build.py` (`ios`), through `tools/common/copy_files.sh` / `copy_files()`
- `tools/ios/scp.py`, into a temp file that is uploaded and then deleted

The copy goes through `tools/common/tsv_filter.py`. A `DropRule` names a platform, a filename, a column, and the cell values to drop. This case is the rule for platform `mobile`, file `dialog.tsv`, column `portrait`, values `Logos/DolbyDigital` and `Logos/DigitalSurround`. The match is the whole cell, and kept rows keep their line endings. Spanish and Portuguese each lose the 3 lines above. French, Italian, and Russian mention Dolby and DTS as plain text with an empty `portrait`, so they do not load a sprite and are copied unchanged. Platform `desk` has no rule, so the Steam copy is unchanged.

To drop another value, on another platform, or from another column, add a `DropRule` to `DROP_RULES`. A legal sentence with an empty `portrait` does not need a rule.
