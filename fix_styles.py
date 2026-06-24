import os

files = ['auftrag.html', 'vollmacht.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # Common fixes
    content = content.replace('background:#fff;', 'background:var(--paper-2);')
    content = content.replace('background:#ffffff;', 'background:var(--paper-2);')
    content = content.replace('border-bottom:1px solid var(--hair)', 'border-bottom:1px solid var(--hair-2)')
    content = content.replace('border:1px solid var(--hair)', 'border:1px solid var(--hair-2)')
    
    # auftrag.html specific fixes
    content = content.replace('background:var(--ink); color:#fff;', 'background:var(--paper-3); color:var(--orange); box-shadow: 0 0 10px rgba(0,240,255,0.1);')
    
    with open(f, 'w') as file:
        file.write(content)

print("Done replacing inline styles.")
