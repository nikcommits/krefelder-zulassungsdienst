import re

astro_file = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2/src/pages/index.astro'
auftrag_file = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2/src/pages/auftrag.astro'

# 1. Update index.astro
with open(astro_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add AOS to Services Grid items
items = re.findall(r'<div class="item">.*?</div>', content)
for i, item in enumerate(items):
    aos_attr = 'data-aos="fade-right"' if i % 2 == 0 else 'data-aos="fade-left"'
    delay = (i // 2) * 50
    new_item = item.replace('<div class="item">', f'<div class="item" {aos_attr} data-aos-delay="{delay}">')
    content = content.replace(item, new_item)

# Add AOS to EVB pill
content = content.replace('<div class="evb-pill"', '<div class="evb-pill" data-aos="fade-up" data-aos-delay="250"')

# Add AOS to Services Card
content = content.replace('<div class="services-card">', '<div class="services-card" data-aos="fade-left" data-aos-delay="300">')

# Stagger steps in "3 Schritten ans Ziel"
steps = re.findall(r'<div class="step" data-aos="fade-up" data-aos-delay="100">', content)
for i, step in enumerate(steps):
    delay = 100 + (i * 100)
    new_step = f'<div class="step" data-aos="fade-up" data-aos-delay="{delay}">'
    # We replace only the first occurrence to avoid replacing all remaining ones at once
    content = content.replace(step, new_step, 1)

with open(astro_file, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Update auftrag.astro
with open(auftrag_file, 'r', encoding='utf-8') as f:
    a_content = f.read()

# Fix the spacing by adding margin-top to .vm-intro so the badge doesn't overlap header
a_content = a_content.replace('.vm-intro{text-align:center;margin-bottom:40px}', '.vm-intro{text-align:center;margin-bottom:40px;margin-top:24px}')

# Fix .vm-header wrapping issue just in case
a_content = a_content.replace('.vm-header .row{display:flex;justify-content:space-between;align-items:center;padding:16px 0}', '.vm-header .row{display:flex;justify-content:space-between;align-items:center;padding:16px 0;flex-wrap:wrap;gap:16px;}')

with open(auftrag_file, 'w', encoding='utf-8') as f:
    f.write(a_content)

print("Animations added and spacing fixed.")
