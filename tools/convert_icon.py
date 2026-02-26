from PIL import Image
import os

def convert_icon():
    img = Image.open('installer/assets/icon.png')
    # Save as ICO for Windows
    img.save('installer/assets/icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    print("Created icon.ico")
    # PNG can be used for Mac in many cases with PyInstaller, or we can just use the PNG.
    # Actually, for Mac, PyInstaller --icon accepts .icns or .iconset or even .png/jpg sometimes but .icns is safest.
    # Converting to .icns is more involved without native tools, but Pillow doesn't support .icns writing well.
    # We will use the PNG for Mac as PyInstaller can handle it or we'll stick to PNG for runtime.

if __name__ == "__main__":
    convert_icon()
