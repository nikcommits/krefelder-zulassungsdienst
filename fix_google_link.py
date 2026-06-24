import os

with open('index.html', 'r') as f:
    content = f.read()

# Replace the wrong Ostwall link with the correct one
wrong_link = 'https://www.google.com/search?q=Zulassungsdienst+Ostwall+Krefeld&review=1'
right_link = 'https://www.google.com/search?q=Zulassungsdienst+Krefeld+NO.1&kgmid=/g/11ltywf6n3&review=1'

content = content.replace(wrong_link, right_link)

with open('index.html', 'w') as f:
    f.write(content)

print("Fixed Google links.")
