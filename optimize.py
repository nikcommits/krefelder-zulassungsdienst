import sys
from PIL import Image

def optimize_image(input_path, output_path, max_width=1200):
    try:
        with Image.open(input_path) as img:
            # Convert to RGB if it's RGBA
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Calculate new dimensions
            ratio = max_width / float(img.size[0])
            if ratio < 1.0:
                new_height = int((float(img.size[1]) * float(ratio)))
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Save as WebP
            img.save(output_path, 'webp', quality=85)
            print(f"Successfully optimized {input_path} to {output_path}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    optimize_image(
        '/Users/aziz/.gemini/antigravity/brain/6af28334-8c43-4a74-bb0e-1dee841ff2b9/media__1780447048753.jpg', 
        '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst/assets/images/hero-new.webp'
    )
