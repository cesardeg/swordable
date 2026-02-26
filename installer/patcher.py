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
from typing import Optional, Dict, List, Any, Union
try:
    from PIL import Image, ImageTk # Helping PyInstaller find the module
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
        "title": "S:S&S ES",
        "header": "SUPERBROTHERS\nSWORD & SWORCERY EP",
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
        "error_revert": "Error al restaurar: ",
        "help_btn": "AYUDA / MANUAL",
        "help_title": "MANUAL DEL USUARIO",
        "help_manual": "1. DETECCIÓN: El parcheador busca el juego automáticamente.\n\n2. CARPETA (WINDOWS/LINUX): Si no se encuentra, selecciona la carpeta raíz que contiene 'sworcery.dat'.\n\n3. CARPETA (MACOS): Selecciona el archivo '.app' del juego o la carpeta que lo contiene.\n\n4. INSTALAR: Aplica la traducción. Se crea una copia de seguridad (.bak).\n\n5. ELIMINAR: Restaura los archivos originales."
    },
    "pt": {
        "title": "S:S&S PT",
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
        "error_revert": "Erro ao restaurar: ",
        "help_btn": "AJUDA / MANUAL",
        "help_title": "MANUAL DO USUÁRIO",
        "help_manual": "1. DETECÇÃO: O patcher procura o jogo automaticamente.\n\n2. PASTA (WINDOWS/LINUX): Se não for encontrado, selecione a pasta raiz que contém 'sworcery.dat'.\n\n3. PASTA (MACOS): Selecione o arquivo '.app' do jogo ou a pasta que o contém.\n\n4. INSTALAR: Aplica a tradução. É criada uma cópia de segurança (.bak).\n\n5. REMOVER: Restaura os arquivos originais."
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
 
class CustomAlert(tk.Toplevel):
    def __init__(self, parent, title, message, alert_type="info"):
        super().__init__(parent)
        self.title(title)
        self.geometry("380x180")
        self.resizable(False, False)
        self.configure(bg=parent.colors["bg"])
        self.transient(parent)
        self.grab_set()
        
        # Center on parent
        x = parent.winfo_x() + (parent.winfo_width() // 2) - 190
        y = parent.winfo_y() + (parent.winfo_height() // 2) - 90
        self.geometry(f"380x180+{x}+{y}")
 
        # UI Elements
        canvas = tk.Canvas(self, width=380, height=180, bg=parent.colors["bg"], highlightthickness=0)
        canvas.pack(fill="both", expand=True)
 
        # Content Frame
        content = tk.Frame(self, bg=parent.colors["bg"])
        canvas.create_window(190, 75, window=content, width=360)
 
        # Icon mapping
        icon_file = f"{alert_type}.png"
        icon_path = get_resource_path(os.path.join("assets", icon_file))
        self.alert_img = None
        if os.path.exists(icon_path):
            try:
                pil_icon = Image.open(icon_path)
                pil_icon = pil_icon.resize((48, 48), Image.Resampling.LANCZOS)
                self.alert_img = ImageTk.PhotoImage(pil_icon)
                tk.Label(content, image=self.alert_img, bg=parent.colors["bg"]).pack(side="left", padx=15)
            except:
                pass
 
        txt_frame = tk.Frame(content, bg=parent.colors["bg"])
        txt_frame.pack(side="left", fill="both", expand=True)
 
        tk.Label(txt_frame, text=message, font=parent.font_small,
                 fg=parent.colors["text"], bg=parent.colors["bg"],
                 wraplength=250, justify="left").pack(anchor="w", pady=10)
 
        # Ok Button
        btn_frame = tk.Frame(self, bg=parent.colors["border_dark"], padx=1, pady=1)
        btn = tk.Label(btn_frame, text="OK", font=parent.font_main,
                       width=8, fg=parent.colors["text"], bg=parent.colors["surface"],
                       cursor="hand2", padx=10, pady=5, relief="raised", borderwidth=2)
        btn.pack()
        
        def on_release(e):
            self.destroy()
 
        btn.bind("<ButtonRelease-1>", on_release)
        canvas.create_window(190, 145, window=btn_frame)

class SworceryInstaller(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Initialize UI attributes to fix lint errors
        self.canvas: tk.Canvas = None  # type: ignore
        self.bg_img: tk.PhotoImage = None  # type: ignore
        self.folder_img: tk.PhotoImage = None  # type: ignore
        self.path_frame: tk.Frame = None  # type: ignore
        self.path_entry: tk.Entry = None  # type: ignore
        self.browse_btn: tk.Label = None  # type: ignore
        self.install_btn: tk.Label = None  # type: ignore
        self.install_btn_window: int = None  # type: ignore
        self.uninstall_btn: tk.Label = None  # type: ignore
        self.uninstall_btn_window: int = None  # type: ignore
        self.help_img: Optional[tk.PhotoImage] = None
        self.help_btn: Optional[tk.Label] = None
        self.subtitle: Optional[Union[tk.Label, int]] = None
        
        self.locale = ARGS.locale
        self.text = STRINGS.get(self.locale, STRINGS["es"])
        
        self.title(self.text["title"])
        self.geometry("500x450")
        self.resizable(False, False)
        self.configure(bg="#1A2B23") # Deep Pine Forest Background

        # Midnight Forest Harmony Palette (Subtle HUD)
        self.colors = {
            "bg": "#121C17",      # Even Deeper Pine
            "surface": "#18231E", # Darker Sage
            "folder_bg": "#0D1411", # Ultra Dark Pine for Folder Icon
            "text": "#BCCAD6",    # Moonlight Silver
            "river": "#6A8B8C",   # Muted Misty River Blue
            "fire": "#D98324",    # Ember Amber (Alert)
            "mint": "#96EDC6",    # Sylvan Mint (Positive)
            "primary": "#D98324", # Fire Amber (Wait/Alert - Now Uninstall)
            "secondary": "#96EDC6", # Sylvan Mint (Action/Install)
            "border_light": "#2A3830", # Submerging Border
            "border_dark": "#0A120E"
        }

        # MacOS 7 / Monaco Style Font family (System Fallbacks)
        self.font_main = ("Monaco", 10, "bold") if sys.platform == "darwin" else ("Courier New", 10, "bold")
        self.font_small = ("Monaco", 9) if sys.platform == "darwin" else ("Courier New", 9)
        self.font_header = ("Monaco", 14, "bold") if sys.platform == "darwin" else ("Courier New", 14, "bold")

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
            CustomAlert(self, "!", error_msg, "error")
            print(f"CRITICAL: {error_msg}")

    def detect_game_path(self):
        paths = []
        if sys.platform == "win32":
            paths = [
                r"C:\Program Files (x86)\Steam\steamapps\common\sworcery",
                r"C:\Program Files (x86)\Steam\steamapps\common\Superbrothers Sword & Sworcery EP",
                r"C:\Program Files (x86)\Steam\steamapps\common\Superbrothers Sword & Sworcery EP\res",
                r"D:\SteamLibrary\steamapps\common\sworcery",
                r"D:\SteamLibrary\steamapps\common\Superbrothers Sword & Sworcery EP",
                r"D:\SteamLibrary\steamapps\common\Superbrothers Sword & Sworcery EP\res"
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
                os.path.expanduser("~/.steam/steam/steamapps/common/sworcery/res"),
                os.path.expanduser("~/.steam/steam/steamapps/common/Superbrothers Sword & Sworcery EP"),
                os.path.expanduser("~/.steam/steam/steamapps/common/Superbrothers Sword & Sworcery EP/res")
            ]
        for p in paths:
            if os.path.exists(os.path.join(p, "sworcery.dat")): return p
        return ""

    def create_retro_button(self, y_pos, text, command, is_primary=True):
        """Creates a classic beveled button with robust hit areas."""
        fg_color = self.colors["primary"] if is_primary else self.colors["secondary"]
        
        btn_frame = tk.Frame(self, bg=self.colors["border_dark"], padx=1, pady=1)
        
        # Avoid fixed width, use padding for safe hit area
        btn = tk.Label(btn_frame, text=text.upper(), font=self.font_main,
                       fg=fg_color, bg=self.colors["surface"],
                       activeforeground=fg_color, activebackground=self.colors["surface"],
                       cursor="hand2", padx=30, pady=12,
                       relief="raised", borderwidth=4)
        btn.pack(fill="both", expand=True)
        
        def on_press(e):
            if str(btn.cget("state")) != "disabled":
                btn.config(relief="sunken", bg=self.colors["bg"])

        def on_release(e):
            if str(btn.cget("state")) != "disabled":
                btn.config(relief="raised", bg=self.colors["surface"])
                command()
        
        def on_enter(e):
             if str(btn.cget("state")) != "disabled":
                btn.config(bg=self.colors["border_light"])

        def on_leave(e):
             if str(btn.cget("state")) != "disabled":
                btn.config(bg=self.colors["surface"])

        # Bind to both frame and label. Use <Button-1> instead of Press/Release on Mac for robustness
        click_event = "<Button-1>" if sys.platform == "darwin" else "<ButtonRelease-1>"
        press_event = "<ButtonPress-1>"
        
        for w in [btn, btn_frame]:
            w.bind(press_event, on_press)
            w.bind(click_event, on_release)
            w.bind("<Enter>", on_enter)
            w.bind("<Leave>", on_leave)
        
        window_id = self.canvas.create_window(250, y_pos, window=btn_frame)
        return btn, window_id

    def setup_ui(self):
        self.canvas = tk.Canvas(self, width=500, height=450, highlightthickness=0, bg=self.colors["bg"])
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
 
        # Load System 7 Folder Icon
        folder_icon_path = get_resource_path(os.path.join("assets", "folder.png"))
        if os.path.exists(folder_icon_path):
            if HAS_PILLOW:
                pil_folder = Image.open(folder_icon_path)
                pil_folder = pil_folder.resize((34, 28), Image.Resampling.LANCZOS)
                self.folder_img = ImageTk.PhotoImage(pil_folder)
            else:
                self.folder_img = tk.PhotoImage(file=folder_icon_path)
        else:
            self.folder_img = None
 
        # Header Title (Centered horizontally with moon altitude)
        self.canvas.create_text(250, 82, text=self.text["header"], fill=self.colors["text"], font=self.font_header, justify="center")
        
        # Subtitle
        self.subtitle = self.canvas.create_text(250, 115, text=self.text["subtitle"], 
                                                 fill=self.colors["river"], font=self.font_main)

        self.canvas.create_text(250, 180, text=self.text["detected"], fill=self.colors["text"], font=self.font_small)
        
        self.path_frame = tk.Frame(self, bg=self.colors["surface"], padx=2, pady=2, relief="sunken", borderwidth=1)
        
        self.path_entry = tk.Entry(self.path_frame, width=38, bg=self.colors["bg"], fg=self.colors["text"], 
                                   borderwidth=0, relief="flat", insertbackground=self.colors["text"], font=self.font_small)
        self.path_entry.insert(0, self.game_path)
        self.path_entry.xview_moveto(1.0) # Show the end of the path
        self.path_entry.pack(side="left", padx=(0, 2), fill="both", expand=True, ipady=3)

        self.browse_btn = tk.Label(self.path_frame, 
                                  image=self.folder_img if self.folder_img else "",
                                  bg=self.colors["folder_bg"], cursor="hand2", 
                                  relief="flat", borderwidth=0, padx=0, pady=0)
        self.browse_btn.bind("<Button-1>", lambda e: self.browse_path())
        self.browse_btn.pack(side="left", fill="both", expand=True)

        self.canvas.create_window(250, 210, window=self.path_frame)
 
        # Buttons (Minimalist Beveled)
        self.install_btn, self.install_btn_window = self.create_retro_button(280, "---", self.install, is_primary=False)
        self.uninstall_btn, self.uninstall_btn_window = self.create_retro_button(350, self.text["uninstall"], self.revert, is_primary=True)
 
        # Help Button
        help_icon_path = get_resource_path(os.path.join("assets", "help.png"))
        self.help_img = None
        if os.path.exists(help_icon_path):
            try:
                pil_help = Image.open(help_icon_path)
                pil_help = pil_help.resize((20, 20), Image.Resampling.LANCZOS)
                self.help_img = ImageTk.PhotoImage(pil_help)
            except: pass
            
        self.help_btn = tk.Label(self, image=self.help_img if self.help_img else "", 
                                text=" ? " if not self.help_img else "",
                                font=self.font_main, bg=self.colors["bg"], fg=self.colors["river"],
                                cursor="hand2")
        self.help_btn.bind("<Button-1>", lambda e: self.show_help())
        self.canvas.create_window(470, 435, window=self.help_btn)
 
        # Credits
        self.canvas.create_text(250, 435, text="POR @CESARDEG // SWORCERY PATCHER // 2026", fill=self.colors["river"], font=("Monospace", 7))
 
        self.path_entry.bind("<KeyRelease>", self.update_status)
 
    def show_help(self):
        """Shows the HUD Integrated Manual with crash protection."""
        try:
            help_win = tk.Toplevel(self)
            help_win.title(self.text["help_title"])
            help_win.geometry("460x420")
            help_win.resizable(False, False)
            help_win.configure(bg=self.colors["bg"])
            help_win.transient(self)
            
            help_win.update_idletasks()
            help_win.lift()
            
            # Simple math for robust compatibility
            pw, ph = self.winfo_width(), self.winfo_height()
            px, py = self.winfo_x(), self.winfo_y()
            x = px + (pw // 2) - 230
            y = py + (ph // 2) - 210
            help_win.geometry(f"460x420+{x}+{y}")

            canvas = tk.Canvas(help_win, width=460, height=420, bg=self.colors["bg"], highlightthickness=0)
            canvas.pack(fill="both", expand=True)

            tk.Label(help_win, text=self.text["help_title"], font=self.font_header,
                     fg=self.colors["mint"], bg=self.colors["bg"]).place(x=230, y=40, anchor="center")

            # Pillow status indicator
            status_color = self.colors["river"] if HAS_PILLOW else self.colors["fire"]
            status_text = "PILLOW OK" if HAS_PILLOW else "PILLOW MISSING (LOW-RES)"
            tk.Label(help_win, text=status_text, font=self.font_small,
                     fg=status_color, bg=self.colors["bg"]).place(x=230, y=65, anchor="center")

            manual_txt = tk.Label(help_win, text=self.text["help_manual"], font=self.font_small,
                                  fg=self.colors["text"], bg=self.colors["bg"],
                                  wraplength=420, justify="left")
            manual_txt.place(x=20, y=90, anchor="nw")

            btn_frame = tk.Frame(help_win, bg=self.colors["border_dark"], padx=1, pady=1)
            btn = tk.Label(btn_frame, text="ENTENDIDO", font=self.font_main,
                           width=12, fg=self.colors["text"], bg=self.colors["surface"],
                           cursor="hand2", padx=10, pady=5, relief="raised", borderwidth=4)
            btn.pack()
            
            # Safe binding
            btn.bind("<Button-1>", lambda e: help_win.destroy())
            canvas.create_window(230, 380, window=btn_frame)
            
            help_win.grab_set()
        except:
            # Fallback for old/unstable environments
            messagebox.showinfo(self.text["help_title"], self.text["help_manual"])
 
        canvas = tk.Canvas(help_win, width=460, height=420, bg=self.colors["bg"], highlightthickness=0)
        canvas.pack(fill="both", expand=True)
 
        tk.Label(help_win, text=self.text["help_title"], font=self.font_header,
                 fg=self.colors["mint"], bg=self.colors["bg"]).place(x=230, y=40, anchor="center")
 
        manual_txt = tk.Label(help_win, text=self.text["help_manual"], font=self.font_small,
                              fg=self.colors["text"], bg=self.colors["bg"],
                              wraplength=420, justify="left")
        manual_txt.place(x=20, y=80, anchor="nw")
 
        btn_frame = tk.Frame(help_win, bg=self.colors["border_dark"], padx=1, pady=1)
        btn = tk.Label(btn_frame, text="ENTENDIDO", font=self.font_main,
                       width=12, fg=self.colors["text"], bg=self.colors["surface"],
                       cursor="hand2", padx=10, pady=5, relief="raised", borderwidth=2)
        btn.pack()
        btn.bind("<ButtonRelease-1>", lambda e: help_win.destroy())
        canvas.create_window(230, 380, window=btn_frame)

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
        if sys.platform == "darwin" and not os.path.exists(os.path.join(str(self.game_path), "sworcery.dat")):
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
            self.install_btn.config(text=self.text["not_found"], state="disabled", bg=self.colors["bg"], fg=self.colors["river"], relief="flat")
            self.canvas.itemconfigure(self.uninstall_btn_window, state="hidden")
            return

        self.install_btn.config(state="normal", relief="raised")
        if is_patched:
            self.install_btn.config(text=self.text["reinstall"], fg=self.colors["secondary"])
            self.canvas.itemconfigure(self.uninstall_btn_window, state="normal")
        else:
            self.install_btn.config(text=self.text["install"], fg=self.colors["secondary"])
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
            
            CustomAlert(self, "OK", self.text["success_install"], "success")
            self.update_status()
        except Exception as e: CustomAlert(self, "Error", f"{self.text['error_install']}{e}", "error")

    def revert(self):
        if str(self.uninstall_btn.cget("state")) == "hidden": return
        dat_path = os.path.join(self.game_path, "sworcery.dat")
        cat_path = dat_path + ".cat"
        try:
            shutil.move(dat_path + ".bak", dat_path)
            if os.path.exists(cat_path + ".bak"): shutil.move(cat_path + ".bak", cat_path)
            CustomAlert(self, "OK", self.text["success_revert"], "success")
            self.update_status()
        except Exception as e: CustomAlert(self, "Error", f"{self.text['error_revert']}{e}", "error")

if __name__ == "__main__":
    app = SworceryInstaller()
    def check_loop():
        app.update_status()
        app.after(1000, check_loop)
    app.after(1000, check_loop)
    app.mainloop()
