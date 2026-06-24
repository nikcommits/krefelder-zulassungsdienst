import os

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('https://share.google/LAMT6cFstM0kQ9UqE', 'https://www.google.com/search?q=Zulassungsdienst+Ostwall+Krefeld&review=1')

with open('index.html', 'w') as f:
    f.write(content)

print("Done google link replace.")
