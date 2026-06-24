import sys
import os

try:
    from PIL import Image
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--break-system-packages", "Pillow"])
    from PIL import Image

def optimize_image():
    input_path = "assets/images/Kurve.png"
    output_path = "assets/images/Kurve.webp"
    
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    with Image.open(input_path) as img:
        # Convert to RGBA if not already to ensure transparency is preserved
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        # A logo displayed at max-height 48px only needs ~144px height for perfect 3x retina sharpness.
        # We set max bounds to 800x150. thumbnail() preserves aspect ratio.
        img.thumbnail((800, 150), Image.Resampling.LANCZOS)
        
        # Save as WEBP for optimal size and performance
        img.save(output_path, "WEBP", quality=85, method=6)
        print(f"Optimized logo saved to {output_path} with new size: {img.size}")

if __name__ == "__main__":
    optimize_image()
