import os
import glob
import re

astro_dir = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2'

# Find all .astro files
astro_files = glob.glob(os.path.join(astro_dir, 'src/**/*.astro'), recursive=True)

for file in astro_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace paths that start with / (except external like //)
    # Be very careful. 
    # <link rel="stylesheet" href="/styles/system.css"> -> href={import.meta.env.BASE_URL + "styles/system.css"}
    # <a href="/auftrag" -> href={import.meta.env.BASE_URL + "auftrag"}
    # src="/assets/ -> src={import.meta.env.BASE_URL + "assets/
    
    # Let's do simple string replaces for the specific assets and links we know exist
    
    # CSS
    content = content.replace('href="/styles/system.css"', 'href={import.meta.env.BASE_URL + "styles/system.css"}')
    content = content.replace('href="styles/system.css"', 'href={import.meta.env.BASE_URL + "styles/system.css"}')
    
    # Images/Assets
    # Note: src="/assets/..." or src="assets/..."
    content = re.sub(r'src="/assets/([^"]+)"', r'src={import.meta.env.BASE_URL + "assets/\1"}', content)
    content = re.sub(r'src="assets/([^"]+)"', r'src={import.meta.env.BASE_URL + "assets/\1"}', content)
    
    # Links
    content = content.replace('href="/auftrag"', 'href={import.meta.env.BASE_URL + "auftrag"}')
    content = content.replace('href="/auftrag/"', 'href={import.meta.env.BASE_URL + "auftrag"}')
    
    content = content.replace('href="/"', 'href={import.meta.env.BASE_URL}')
    
    # Except do not replace "http..." or similar
    # The above explicit replaces are safe.
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Paths fixed for Astro BASE_URL")
