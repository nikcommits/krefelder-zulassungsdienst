import os
import glob

astro_dir = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2'
astro_files = glob.glob(os.path.join(astro_dir, 'src/**/*.astro'), recursive=True)

for file in astro_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix CSS
    content = content.replace('BASE_URL + "styles/system.css"', 'BASE_URL + "/styles/system.css"')
    
    # Fix Assets
    content = content.replace('BASE_URL + "assets/', 'BASE_URL + "/assets/')
    
    # Fix Links
    content = content.replace('BASE_URL + "auftrag"', 'BASE_URL + "/auftrag"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Hotfixed trailing slashes for BASE_URL")
