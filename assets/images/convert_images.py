import os
from PIL import Image

images = [
    "code-zulassungsescheinigung-teil1-freigelegt.jpg",
    "code-zulassungsescheinigung-teil-freigelegt.jpg",
    "code-kennzeichen-freigelegt-hinten.png"
]

for img_name in images:
    with Image.open(img_name) as img:
        img.thumbnail((500, 500))
        new_name = os.path.splitext(img_name)[0] + ".webp"
        img.save(new_name, "WEBP", quality=80)
        print(f"Converted and resized {img_name} to {new_name}")
