import os
import sys
import shutil
import argparse

# --- System Dependency Check ---
try:
    import _tkinter
except ImportError:
    print("\n" + "!" * 60)
    print(" ERROR: MISSING SYSTEM DEPENDENCY (tkinter) ".center(60, "!"))
    print("!" * 60)
    if sys.platform == "darwin":
        print("\n On macOS, you need to install tcl-tk via Homebrew:")
        print("   brew install tcl-tk python-tk")
        print("\n After installing, please try running this script again.")
    elif sys.platform == "linux":
        print("\n On Linux, you likely need:")
        print("   sudo apt install python3-tk")
    else:
        print("\n Please ensure your Python installation includes Tcl/Tk support.")
    print("!" * 60 + "\n")
    sys.exit(1)

import tkinter as tk
from tkinter import filedialog, messagebox
try:
    from PIL import Image, ImageTk
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False

# --- CLI Arguments ---
def get_args():
    # Production: Check for baked locale metadata
    default_locale = os.getenv("APP_LOCALE", "es")
    frozen = getattr(sys, 'frozen', False)
    if frozen:
        locale_path = os.path.join(sys._MEIPASS, "locale.txt")
        if os.path.exists(locale_path):
            try:
                with open(locale_path, "r") as f:
                    default_locale = f.read().strip()
            except:
                pass

    parser = argparse.ArgumentParser(description="Sword & Sworcery EP Patcher")
    parser.add_argument("--locale", default=default_locale, choices=["es", "pt"], help="Locale to use")
    parser.add_argument("--os", default=sys.platform, help="Operating system target")
    parser.add_argument("--game-path", help="Direct path to game folder")
    return parser.parse_known_args()[0]

ARGS = get_args()

# --- i18n Dictionary ---
STRINGS = {
    "es": {
        "title": "Sworcery Patcher ES",
        "header": "SUPERBROTHERS:\nSWORD & SWORCERY EP",
        "subtitle": "INSTALADOR - ESPAÑOL",
        "detected": "Carpeta del juego detectada:",
        "browse": "Cambiar carpeta...",
        "install": "INSTALAR TRADUCCIÓN",
        "reinstall": "REINSTALAR TRADUCCIÓN",
        "uninstall": "ELIMINAR TRADUCCIÓN",
        "not_found": "JUEGO NO ENCONTRADO",
        "success_install": "¡Traducción al Español instalada correctamente!",
        "success_revert": "Archivos originales restaurados.",
        "error_internal": "Error interno: Archivos no encontrados.",
        "error_build_needed": "No se encontraron los datos de traducción en:\n{path}\n\nPor favor, ejecuta primero:\ntools/steam/build.sh sworcery.dat {locale}",
        "error_install": "No se pudo instalar:\n",
        "error_revert": "Error al restaurar: "
    },
    "pt": {
        "title": "Sworcery Patcher PT",
        "header": "SUPERBROTHERS\nSWORD & SWORCERY EP",
        "subtitle": "INSTALADOR - PORTUGUÊS",
        "detected": "Pasta do jogo detectada:",
        "browse": "Alterar pasta...",
        "install": "INSTALAR TRADUÇÃO",
        "reinstall": "REINSTALAR TRADUÇÃO",
        "uninstall": "REMOVER TRADUÇÃO",
        "not_found": "JOGO NÃO ENCONTRADO",
        "success_install": "Tradução para Português instalada com sucesso!",
        "success_revert": "Arquivos originais restaurados.",
        "error_internal": "Erro interno: Arquivos no encontrados.",
        "error_build_needed": "Dados de tradução não encontrados em:\n{path}\n\nPor favor, execute primeiro:\ntools/steam/build.sh sworcery.dat {locale}",
        "error_install": "No foi possível instalar:\n",
        "error_revert": "Erro ao restaurar: "
    }
}

def get_resource_path(relative_path):
    frozen = getattr(sys, 'frozen', False)
    if frozen:
        # Production: Files are inside the bundle
        base_path = sys._MEIPASS
    else:
        # Development: Look in build/steam/[locale]
        script_dir = os.path.dirname(os.path.realpath(__file__))
        project_root = os.path.dirname(script_dir)
        
        # Exception for assets (background) which are in installer/assets
        if "assets" in relative_path:
            return os.path.join(script_dir, relative_path)
            
        base_path = os.path.join(project_root, "build", "steam", ARGS.locale)
        
    return os.path.join(base_path, relative_path)

class SworceryInstaller(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.locale = ARGS.locale
        self.text = STRINGS.get(self.locale, STRINGS["es"])
        
        self.title(self.text["title"])
        self.geometry("500x450")
        self.resizable(False, False)
        self.configure(bg="#0a0a0a")

        # Set Window Icon
        icon_path = get_resource_path(os.path.join("assets", "icon.png"))
        if os.path.exists(icon_path):
            try:
                icon_img = tk.PhotoImage(file=icon_path)
                self.iconphoto(False, icon_img)
            except:
                pass

        self.game_path = ARGS.game_path if ARGS.game_path else self.detect_game_path()
        self.setup_ui()
        self.center_window()
        self.check_data_files()
        self.update_status()

    def center_window(self):
        """Centers the window on the screen."""
        self.update_idletasks()
        width = 500
        height = 450
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def check_data_files(self):
        """Checks if sworcery.dat exists in the expected location."""
        dat_path = get_resource_path("sworcery.dat")
        if not os.path.exists(dat_path):
            error_msg = self.text["error_build_needed"].format(path=dat_path, locale=self.locale)
            messagebox.showwarning("Missing Files", error_msg)
            print(f"CRITICAL: {error_msg}")

    def detect_game_path(self):
        paths = []
        if sys.platform == "win32":
            paths = [
                r"C:\Program Files (x86)\Steam\steamapps\common\sworcery",
                r"C:\Program Files (x86)\Steam\steamapps\common\Superbrothers Sword & Sworcery EP",
                r"D:\SteamLibrary\steamapps\common\sworcery",
                r"D:\SteamLibrary\steamapps\common\Superbrothers Sword & Sworcery EP"
            ]
        elif sys.platform == "darwin":
            paths = [
                os.path.expanduser("~/Library/Application Support/Steam/steamapps/common/Superbrothers Sword & Sworcery EP/swordandsworcery_pc.app/Contents/Resources/Game"),
                os.path.expanduser("~/Library/Application Support/Steam/steamapps/common/Superbrothers Sword & Sworcery EP/Superbrothers Sword & Sworcery EP.app/Contents/Resources"),
                os.path.expanduser("~/Library/Application Support/Steam/steamapps/common/sworcery/Superbrothers Sword & Sworcery EP.app/Contents/Resources")
            ]
        else:
            paths = [
                os.path.expanduser("~/.steam/steam/steamapps/common/sworcery"),
                os.path.expanduser("~/.steam/steam/steamapps/common/Superbrothers Sword & Sworcery EP")
            ]
        for p in paths:
            if os.path.exists(os.path.join(p, "sworcery.dat")): return p
        return ""

    def create_retro_button(self, y_pos, text, color, command, is_uninstall=False):
        """Creates a retro 3D button using a Label with sunken/raised effects."""
        btn = tk.Label(self, text=text, font=("Courier", 12, "bold"),
                       width=20, height=1, fg="white", bg=color,
                       cursor="hand2", padx=20, pady=10,
                       relief="raised", borderwidth=3)
        
        def on_press(e):
            if str(btn.cget("state")) != "disabled":
                btn.config(relief="sunken", bg=self.darken_color(color))

        def on_release(e):
            if str(btn.cget("state")) != "disabled":
                btn.config(relief="raised", bg=color)
                command()

        def on_enter(e):
            if str(btn.cget("state")) != "disabled":
                btn.config(highlightbackground="#ffd700", highlightthickness=1)

        def on_leave(e):
            btn.config(highlightthickness=0)

        btn.bind("<ButtonPress-1>", on_press)
        btn.bind("<ButtonRelease-1>", on_release)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        window_id = self.canvas.create_window(250, y_pos, window=btn)
        return btn, window_id

    def darken_color(self, hex_color):
        """Simple helper to darken a hex color for the pressed effect."""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        dark_rgb = tuple(max(0, c - 40) for c in rgb)
        return '#%02x%02x%02x' % dark_rgb

    def setup_ui(self):
        self.canvas = tk.Canvas(self, width=500, height=450, highlightthickness=0, bg="#0a0a0a")
        self.canvas.pack(fill="both", expand=True)

        bg_path = get_resource_path(os.path.join("assets", "background.png"))
        if os.path.exists(bg_path):
            if HAS_PILLOW:
                pil_img = Image.open(bg_path)
                pil_img = pil_img.resize((500, 450), Image.Resampling.LANCZOS)
                self.bg_img = ImageTk.PhotoImage(pil_img)
            else:
                self.bg_img = tk.PhotoImage(file=bg_path)
            self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

        # Header with retro shadow effect
        self.canvas.create_text(245, 43, text=self.text["header"], fill="#555", font=("Helvetica", 18, "bold"), justify="center")
        self.canvas.create_text(242, 40, text=self.text["header"], fill="#ffd700", font=("Helvetica", 18, "bold"), justify="center")
        
        self.subtitle = self.canvas.create_text(242, 85, text=self.text["subtitle"], fill="#00ffff", font=("Courier", 11, "bold"))

        self.canvas.create_text(250, 125, text=self.text["detected"], fill="white", font=("Courier", 10, "bold"))
        
        self.path_frame = tk.Frame(self, bg="#0a0a0a")
        
        self.path_entry = tk.Entry(self.path_frame, width=36, bg="#111", fg="#00ff00", 
                                   borderwidth=1, relief="solid", insertbackground="white", font=("Courier", 10))
        self.path_entry.insert(0, self.game_path)
        self.path_entry.xview_moveto(1.0) # Show the end of the path
        self.path_entry.pack(side="left", padx=(0, 2))

        self.browse_btn = tk.Label(self.path_frame, text=" 📂 ", 
                                  bg="#222", fg="#00ffff", cursor="hand2", 
                                  relief="raised", borderwidth=2, font=("Helvetica", 10))
        self.browse_btn.bind("<Button-1>", lambda e: self.browse_path())
        self.browse_btn.pack(side="left")

        self.canvas.create_window(250, 150, window=self.path_frame)

        # Buttons (Retro Styled)
        self.install_btn, self.install_btn_window = self.create_retro_button(215, "---", "#008000", self.install)
        self.uninstall_btn, self.uninstall_btn_window = self.create_retro_button(285, self.text["uninstall"], "#800000", self.revert)

        # Credits
        self.canvas.create_text(250, 435, text="Por @cesardeg | Sworcery Patcher Team", fill="white", font=("Courier", 8, "bold"))

        self.path_entry.bind("<KeyRelease>", self.update_status)

    def browse_path(self):
        current = self.path_entry.get().strip()
        initial = current if os.path.isdir(current) else None
        
        # If the path looks like an internal .app path, go up to the .app level for browsing
        if initial and ".app/Contents/Resources" in initial:
            initial = initial.split(".app")[0] + ".app"
            initial = os.path.dirname(initial)

        folder = filedialog.askdirectory(initialdir=initial)
        if folder:
            # 1. Check if the selected folder contains the .app or if we should search inside
            if sys.platform == "darwin" and not os.path.exists(os.path.join(folder, "sworcery.dat")):
                # Look for known bundles inside the selected folder
                try:
                    for item in os.listdir(folder):
                        lower_item = item.lower()
                        if item.endswith(".app") and ("sword" in lower_item or "sworcery" in lower_item):
                            potential_app = os.path.join(folder, item)
                            # Use internal resolution for this bundle
                            for sub in [os.path.join("Contents", "Resources", "Game"), os.path.join("Contents", "Resources")]:
                                full_sub = os.path.join(potential_app, sub)
                                if os.path.exists(os.path.join(full_sub, "sworcery.dat")):
                                    folder = full_sub
                                    break
                            if "Contents" in folder: break
                except:
                    pass

            # 2. Existing smart resolution for direct .app selections (if supported by OS)
            if folder.endswith(".app"):
                for sub in [os.path.join("Contents", "Resources", "Game"), os.path.join("Contents", "Resources")]:
                    internal_path = os.path.join(folder, sub)
                    if os.path.exists(os.path.join(internal_path, "sworcery.dat")):
                        folder = internal_path
                        break

            self.game_path = folder
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)
            self.path_entry.xview_moveto(1.0) # Show the end of the path
            self.update_status()

    def update_status(self, *args):
        self.game_path = self.path_entry.get().strip()
        
        # Smart resolution for macOS: if path is a .app or contains one
        if sys.platform == "darwin" and not os.path.exists(os.path.join(self.game_path, "sworcery.dat")):
            # If the path itself is the .app
            if self.game_path.endswith(".app"):
                for sub in [os.path.join("Contents", "Resources", "Game"), os.path.join("Contents", "Resources")]:
                    full_sub = os.path.join(self.game_path, sub)
                    if os.path.exists(os.path.join(full_sub, "sworcery.dat")):
                        self.game_path = full_sub
                        self.path_entry.delete(0, tk.END)
                        self.path_entry.insert(0, self.game_path)
                        self.path_entry.xview_moveto(1.0) # Show the end of the path
                        break
            # If the path contains the .app inside
            elif os.path.isdir(self.game_path):
                try:
                    for item in os.listdir(self.game_path):
                        lower_item = item.lower()
                        if item.endswith(".app") and ("sword" in lower_item or "sworcery" in lower_item):
                            potential_app = os.path.join(self.game_path, item)
                            for sub in [os.path.join("Contents", "Resources", "Game"), os.path.join("Contents", "Resources")]:
                                full_sub = os.path.join(potential_app, sub)
                                if os.path.exists(os.path.join(full_sub, "sworcery.dat")):
                                    self.game_path = full_sub
                                    self.path_entry.delete(0, tk.END)
                                    self.path_entry.insert(0, self.game_path)
                                    self.path_entry.xview_moveto(1.0) # Show the end of the path
                                    break
                            if "Contents" in self.game_path: break
                except:
                    pass

        dat_exists = os.path.exists(os.path.join(self.game_path, "sworcery.dat"))
        is_patched = os.path.exists(os.path.join(self.game_path, "sworcery.dat.bak"))

        if not dat_exists:
            self.install_btn.config(text=self.text["not_found"], state="disabled", bg="#444", fg="#888", relief="flat")
            self.canvas.itemconfigure(self.uninstall_btn_window, state="hidden")
            return

        self.install_btn.config(state="normal", relief="raised")
        if is_patched:
            self.install_btn.config(text=self.text["reinstall"], bg="#008080", fg="white") # Electric Cyan
            self.canvas.itemconfigure(self.uninstall_btn_window, state="normal")
        else:
            self.install_btn.config(text=self.text["install"], bg="#008000", fg="white") # Phospor Green
            self.canvas.itemconfigure(self.uninstall_btn_window, state="hidden")

    def install(self):
        if str(self.install_btn.cget("state")) == "disabled": return
        dat_path = os.path.join(self.game_path, "sworcery.dat")
        cat_path = dat_path + ".cat"
        try:
            if not os.path.exists(dat_path + ".bak"):
                shutil.copy2(dat_path, dat_path + ".bak")
                if os.path.exists(cat_path): shutil.copy2(cat_path, cat_path + ".bak")

            new_dat = get_resource_path("sworcery.dat")
            new_cat = get_resource_path("sworcery.dat.cat")
            
            if not os.path.exists(new_dat): raise Exception(self.text["error_internal"])
            shutil.copy2(new_dat, dat_path)
            if os.path.exists(new_cat): shutil.copy2(new_cat, cat_path)
            
            messagebox.showinfo("OK", self.text["success_install"])
            self.update_status()
        except Exception as e: messagebox.showerror("Error", f"{self.text['error_install']}{e}")

    def revert(self):
        if str(self.uninstall_btn.cget("state")) == "hidden": return
        dat_path = os.path.join(self.game_path, "sworcery.dat")
        cat_path = dat_path + ".cat"
        try:
            shutil.move(dat_path + ".bak", dat_path)
            if os.path.exists(cat_path + ".bak"): shutil.move(cat_path + ".bak", cat_path)
            messagebox.showinfo("OK", self.text["success_revert"])
            self.update_status()
        except Exception as e: messagebox.showerror("Error", f"{self.text['error_revert']}{e}")

if __name__ == "__main__":
    app = SworceryInstaller()
    def check_loop():
        app.update_status()
        app.after(1000, check_loop)
    app.after(1000, check_loop)
    app.mainloop()
