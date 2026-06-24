import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from PIL import Image
except ImportError:
    install("Pillow")
    from PIL import Image

def remove_white_bg(image_path, output_path, tolerance=230):
    img = Image.open(image_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # If all RGB values are above the tolerance, it's considered white
        if item[0] >= tolerance and item[1] >= tolerance and item[2] >= tolerance:
            # We can do basic feathering: 
            # if it's pure white (255), alpha is 0
            # if it's 230, alpha is somewhat visible.
            # But simple transparent is often enough for a quick fix if tolerance is high
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(output_path, "PNG")
    print(f"Background removed and saved to {output_path}")

if __name__ == "__main__":
    # We will use a very high tolerance (like 245) to only remove pure white and not ruin anti-aliasing too much.
    # Actually, a better approach for logos on dark backgrounds is to use the image itself as an alpha mask if it's single color, 
    # but since we don't know the exact logo colors, we'll stick to a simple white removal.
    remove_white_bg('assets/images/Kennwerk-Logo.png', 'assets/images/Kennwerk-Logo.png', tolerance=245)
