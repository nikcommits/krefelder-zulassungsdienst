import os
src = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst'
dest = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro/src/pages'

for file in ['auftrag.html', 'vollmacht.html']:
    with open(f"{src}/{file}", 'r') as f:
        content = f.read()
    
    # Fix links
    content = content.replace('index.html', '/')
    content = content.replace('auftrag.html', '/auftrag')
    content = content.replace('vollmacht.html', '/vollmacht')
    
    with open(f"{dest}/{file.replace('.html', '.astro')}", 'w') as f:
        f.write("---\n---\n" + content)
