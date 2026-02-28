use std::path::{Path, PathBuf};
use std::fs;
use tauri::path::BaseDirectory;
use tauri::Manager;

const TRANSLATION_FILES: &[&str] = &["sworcery.dat"];
const OPTIONAL_FILES: &[&str] = &["sworcery.dat.cat"];
const BACKUP_SUFFIX: &str = ".bak";

fn looks_like_game_dir(p: &Path) -> bool {
    let markers = ["sworcery.dat", "sworcery_pc.app", "sworcery.exe"];
    markers.iter().any(|m| p.join(m).exists())
}

fn resolve_game_folder(base_path: &Path) -> PathBuf {
    #[cfg(target_os = "macos")]
    {
        if base_path.extension().and_then(|e| e.to_str()) == Some("app") {
            for sub in ["Contents/Resources/Game", "Contents/Resources"] {
                let full_sub = base_path.join(sub);
                if full_sub.join("sworcery.dat").exists() {
                    return full_sub;
                }
            }
        } else if base_path.is_dir() {
            if let Ok(entries) = fs::read_dir(base_path) {
                for entry in entries.flatten() {
                    let path = entry.path();
                    let name = path.file_name().unwrap_or_default().to_string_lossy().to_lowercase();
                    if path.extension().and_then(|e| e.to_str()) == Some("app") && (name.contains("sword") || name.contains("sworcery")) {
                        for sub in ["Contents/Resources/Game", "Contents/Resources"] {
                            let full_sub = path.join(sub);
                            if full_sub.join("sworcery.dat").exists() {
                                return full_sub;
                            }
                        }
                    }
                }
            }
        }
    }
    base_path.to_path_buf()
}

fn validate(path: &str) -> Result<PathBuf, String> {
    let p = Path::new(path);
    if !p.exists() {
        return Err(format!("Folder does not exist: {}", path));
    }
    let resolved = resolve_game_folder(p);
    if !looks_like_game_dir(&resolved) {
        return Err("This doesn't look like the Sworcery game folder.".into());
    }
    Ok(resolved)
}

#[tauri::command]
pub fn detect_path() -> Option<String> {
    let mut paths: Vec<String> = Vec::new();

    #[cfg(target_os = "windows")]
    {
        paths = vec![
            r#"C:\Program Files (x86)\Steam\steamapps\common\sworcery"#.into(),
            r#"C:\Program Files (x86)\Steam\steamapps\common\Superbrothers Sword & Sworcery EP"#.into(),
            r#"C:\Program Files (x86)\Steam\steamapps\common\Superbrothers Sword & Sworcery EP\res"#.into(),
            r#"D:\SteamLibrary\steamapps\common\sworcery"#.into(),
            r#"D:\SteamLibrary\steamapps\common\Superbrothers Sword & Sworcery EP"#.into(),
            r#"D:\SteamLibrary\steamapps\common\Superbrothers Sword & Sworcery EP\res"#.into(),
        ];
    }
    
    #[cfg(target_os = "macos")]
    {
        if let Ok(home) = std::env::var("HOME") {
            paths = vec![
                format!("{}/Library/Application Support/Steam/steamapps/common/Superbrothers Sword & Sworcery EP/swordandsworcery_pc.app/Contents/Resources/Game", home),
                format!("{}/Library/Application Support/Steam/steamapps/common/Superbrothers Sword & Sworcery EP/Superbrothers Sword & Sworcery EP.app/Contents/Resources", home),
                format!("{}/Library/Application Support/Steam/steamapps/common/sworcery/Superbrothers Sword & Sworcery EP.app/Contents/Resources", home),
            ];
        }
    }

    #[cfg(target_os = "linux")]
    {
        if let Ok(home) = std::env::var("HOME") {
            paths = vec![
                format!("{}/.steam/steam/steamapps/common/sworcery", home),
                format!("{}/.steam/steam/steamapps/common/sworcery/res", home),
                format!("{}/.steam/steam/steamapps/common/Superbrothers Sword & Sworcery EP", home),
                format!("{}/.steam/steam/steamapps/common/Superbrothers Sword & Sworcery EP/res", home),
                format!("{}/snap/steam/common/.local/share/Steam/steamapps/common/Superbrothers Sword & Sworcery EP", home),
                format!("{}/snap/steam/common/.local/share/Steam/steamapps/common/Superbrothers Sword & Sworcery EP/res", home),
            ];
        }
    }
    
    for path_str in paths {
        let candidate = Path::new(&path_str);
        if candidate.exists() && looks_like_game_dir(candidate) {
            return Some(path_str.to_string());
        }
    }
    None
}

#[tauri::command]
pub fn check_patch_status(path: String) -> Result<bool, String> {
    let game_dir = validate(&path)?;
    
    for filename in TRANSLATION_FILES {
        let dest = game_dir.join(filename);
        let mut backup = dest.clone();
        backup.set_extension(format!("{}{}", dest.extension().unwrap_or_default().to_string_lossy(), BACKUP_SUFFIX));
        if backup.exists() {
            return Ok(true);
        }
    }
    Ok(false)
}

#[tauri::command]
pub fn install_patch(app_handle: tauri::AppHandle, path: String) -> Result<(), String> {
    let game_dir = validate(&path)?;
    
    let src_dir = app_handle.path().resolve("assets", BaseDirectory::Resource)
        .map_err(|e| format!("Could not resolve resources: {}", e))?;
        
    if !src_dir.exists() {
        return Err(format!("Translation source not found: {}", src_dir.display()));
    }

    for file_list in &[TRANSLATION_FILES, OPTIONAL_FILES] {
        for filename in *file_list {
            let src = src_dir.join(filename);
            let dest = game_dir.join(filename);

            let is_required = *file_list == TRANSLATION_FILES;
            
            if is_required && !src.exists() {
                return Err(format!("Missing translation file: {}", filename));
            }
            if !src.exists() {
                continue;
            }

            let mut backup = dest.clone();
            backup.set_extension(format!("{}{}", dest.extension().unwrap_or_default().to_string_lossy(), BACKUP_SUFFIX));
            if dest.exists() && !backup.exists() {
                fs::copy(&dest, &backup).map_err(|e| e.to_string())?;
            }

            fs::copy(&src, &dest).map_err(|e| e.to_string())?;
        }
    }
    Ok(())
}

#[tauri::command]
pub fn remove_patch(path: String) -> Result<(), String> {
    let game_dir = validate(&path)?;
    let mut restored = 0;

    for file_list in &[TRANSLATION_FILES, OPTIONAL_FILES] {
        for filename in *file_list {
            let dest = game_dir.join(filename);
            let mut backup = dest.clone();
            backup.set_extension(format!("{}{}", dest.extension().unwrap_or_default().to_string_lossy(), BACKUP_SUFFIX));

            if backup.exists() {
                fs::copy(&backup, &dest).map_err(|e| e.to_string())?;
                fs::remove_file(&backup).unwrap_or_default();
                if *file_list == TRANSLATION_FILES {
                    restored += 1;
                }
            }
        }
    }

    if restored == 0 {
        return Err("No backup files found — translation may not be installed.".into());
    }
    Ok(())
}
