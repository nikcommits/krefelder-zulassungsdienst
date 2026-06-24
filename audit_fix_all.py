import os
import re

files = [
    'index.html',
    'auftrag.html',
    'vollmacht.html',
    'styles/system.css'
]

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Text replacements
    content = content.replace('Krefelder Zulassungsdienst', 'Zulassungsdienst Ostwall')
    content = content.replace('Ali Hakan Zengin', 'Muhammet Aygan')
    content = content.replace('Bahnstraße 16a', 'Ostwall 53')
    content = content.replace('47799 Krefeld', '47798 Krefeld')
    content = content.replace('https://share.google/nexC2D69iQ7lRoy7I', 'https://share.google/GdE9jqD7wi3ojyp4M')

    # Hide social links instead of removing them to prevent regex nesting bugs
    content = content.replace('<div class="social-grid">', '<div class="social-grid" style="display: none;">')
    content = content.replace('<a href="https://www.facebook.com', '<a style="display:none;" href="https://www.facebook.com')
    content = content.replace('<a href="https://www.instagram.com', '<a style="display:none;" href="https://www.instagram.com')

    with open(filepath, 'w') as f:
        f.write(content)

print("Done")
