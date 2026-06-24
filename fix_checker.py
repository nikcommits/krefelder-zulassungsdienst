import re

with open('/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

with open('/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2/src/pages/index.astro', 'r', encoding='utf-8') as f:
    astro_content = f.read()

# Extract checker-box from html
match_html = re.search(r'(<div class="checker-box" id="checker-container">.*?</div>\s+</div>\s+</section>)', html_content, re.DOTALL)
if match_html:
    checker_html = match_html.group(1)
    
    # Extract checker-box from astro
    match_astro = re.search(r'(<div class="checker-box" id="checker-container">.*?</div>\s+</div>\s+</section>)', astro_content, re.DOTALL)
    if match_astro:
        astro_content = astro_content.replace(match_astro.group(1), checker_html)
        
        # We need to make sure the links in the copied HTML are correct for Astro.
        # e.g., href="auftrag.html" -> href="/auftrag"
        astro_content = astro_content.replace('href="auftrag.html"', 'href="/auftrag"')
        astro_content = astro_content.replace('href="index.html"', 'href="/"')
        astro_content = astro_content.replace('href="vollmacht.html"', 'href="/vollmacht"')
        
        with open('/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2/src/pages/index.astro', 'w', encoding='utf-8') as f:
            f.write(astro_content)
        print("Successfully updated index.astro")
    else:
        print("Could not find checker-box in index.astro")
else:
    print("Could not find checker-box in index.html")
