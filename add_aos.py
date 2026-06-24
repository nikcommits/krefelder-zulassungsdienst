import re

file_path = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2/src/pages/index.astro'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Animate hero elements
content = content.replace('<div class="hero-copy">', '<div class="hero-copy" data-aos="fade-right">')
content = content.replace('<div class="hero-media">', '<div class="hero-media" data-aos="fade-left">')

# Animate steps
content = content.replace('<div class="step">', '<div class="step" data-aos="fade-up" data-aos-delay="100">')

# Animate section headers
content = content.replace('<div class="sec-head">', '<div class="sec-head" data-aos="fade-up">')

# Animate checker container
content = content.replace('<div class="checker-box" id="checker-container">', '<div class="checker-box" id="checker-container" data-aos="zoom-in">')

# Animate price cards
content = content.replace('<div class="price-card">', '<div class="price-card" data-aos="fade-up" data-aos-delay="100">')

# Animate trust grid items
content = content.replace('<div class="trust-left">', '<div class="trust-left" data-aos="fade-right">')
content = content.replace('<div class="trust-grid">', '<div class="trust-grid" data-aos="fade-left">')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("AOS animations added to index.astro")
