import os

files = ['index.html', 'auftrag.html', 'vollmacht.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # Phone number replacements
    content = content.replace('0173 280 3507', '0172 8474357')
    content = content.replace('01732803507', '01728474357')
    content = content.replace('491732803507', '491728474357')
    
    # Google link replacements
    content = content.replace('https://share.google/GdE9jqD7wi3ojyp4M', 'https://share.google/LAMT6cFstM0kQ9UqE')
    
    # TikTok replacements
    content = content.replace('https://www.tiktok.com/@zulassungsdienstostwall', 'https://www.tiktok.com/@kennwerk')
    
    with open(f, 'w') as file:
        file.write(content)

print("Done replacing.")
