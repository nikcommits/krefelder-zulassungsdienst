import os
import re

html_dir = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst'
astro_dir = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2'

# 1. Update auftrag.astro
with open(os.path.join(html_dir, 'auftrag.html'), 'r', encoding='utf-8') as f:
    auftrag_html = f.read()

# Replace <script> with <script is:inline> to avoid Astro processing issues
auftrag_html = auftrag_html.replace('<script>', '<script is:inline>')
# Also adjust links
auftrag_html = auftrag_html.replace('href="index.html"', 'href="/"')
auftrag_html = auftrag_html.replace('href="vollmacht.html"', 'href="/vollmacht"')
auftrag_html = auftrag_html.replace('href="datenschutz.html"', 'href="/datenschutz"')
auftrag_html = auftrag_html.replace('href="impressum.html"', 'href="/impressum"')
# Remove the '.webp' from assets if needed, but Astro public works with absolute or relative. Let's use absolute.
auftrag_html = auftrag_html.replace('src="assets/', 'src="/assets/')

auftrag_astro_content = "---\n---\n" + auftrag_html
with open(os.path.join(astro_dir, 'src', 'pages', 'auftrag.astro'), 'w', encoding='utf-8') as f:
    f.write(auftrag_astro_content)

# 2. Update index.astro
with open(os.path.join(astro_dir, 'src', 'pages', 'index.astro'), 'r', encoding='utf-8') as f:
    index_astro = f.read()

# Step 1
old_step1 = """      <div class="step">
        <div class="num dark">1</div>
        <div class="ico ico-wa"><svg viewBox="0 0 448 512" fill="currentColor"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.2-157zM223.9 438.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.5-186.6 184.5zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/></svg></div>
        <h3 class="h3">Dokumente senden</h3>
        <p>Sende uns ein Foto deines Ausweises und der Papiere mit freigerubbeltem Sicherheitscode – ganz einfach per WhatsApp.</p>
      </div>"""
new_step1 = """      <div class="step">
        <div class="num dark">1</div>
        <div class="ico ico-wa"><svg viewBox="0 0 576 512" fill="currentColor"><path d="M402.6 83.2 462 142.6 290 314.6l-72.2 8 8-72.2 172-167.2zM512 92.6 484.6 65.2c-12.5-12.5-32.8-12.5-45.3 0l-30.1 30.1 59.4 59.4 30.1-30.1c12.5-12.5 12.5-32.8 0-45.3zM96 64C43 64 0 107 0 160v256c0 53 43 96 96 96h256c53 0 96-43 96-96v-96c0-17.7-14.3-32-32-32s-32 14.3-32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V160c0-17.7 14.3-32 32-32h96c17.7 0 32-14.3 32-32s-14.3-32-32-32H96z"/></svg></div>
        <h3 class="h3">Online Auftrag erteilen</h3>
        <p>Fülle in 2 Minuten unser Online-Formular aus, unterschreibe bequem am Bildschirm und sende uns Fotos deiner Dokumente per WhatsApp.</p>
      </div>"""
index_astro = index_astro.replace(old_step1, new_step1)

# Step 2
old_step2 = """    <div class="center" style="margin-top:48px">
      <a href="https://wa.me/491728474357" target="_blank" rel="noopener" class="btn btn-orange glow btn-lg">
        <span class="fi"><svg viewBox="0 0 448 512" fill="currentColor"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.2-157zM223.9 438.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.5-186.6 184.5zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/></svg></span>
        Jetzt Dokumente per WhatsApp senden
      </a>
    </div>"""
new_step2 = """    <div class="center" style="margin-top:48px">
      <a href="/auftrag" class="btn btn-orange glow btn-lg">
        <span class="fi"><svg viewBox="0 0 576 512" fill="currentColor"><path d="M402.6 83.2 462 142.6 290 314.6l-72.2 8 8-72.2 172-167.2zM512 92.6 484.6 65.2c-12.5-12.5-32.8-12.5-45.3 0l-30.1 30.1 59.4 59.4 30.1-30.1c12.5-12.5 12.5-32.8 0-45.3zM96 64C43 64 0 107 0 160v256c0 53 43 96 96 96h256c53 0 96-43 96-96v-96c0-17.7-14.3-32-32-32s-32 14.3-32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V160c0-17.7 14.3-32 32-32h96c17.7 0 32-14.3 32-32s-14.3-32-32-32H96z"/></svg></span>
        Jetzt Online-Auftrag starten
      </a>
    </div>"""
index_astro = index_astro.replace(old_step2, new_step2)

# Step 3
old_step3 = """          <div class="trust-divider">
            <p style="color:#cbd5e1;font-size:.875rem;margin-bottom:12px">Noch keine Vollmacht für uns?</p>
            <a href="/vollmacht" class="btn-vollmacht">
              <span class="fi"><svg viewBox="0 0 576 512" fill="currentColor"><path d="M402.6 83.2 462 142.6 290 314.6l-72.2 8 8-72.2 172-167.2zM512 92.6 484.6 65.2c-12.5-12.5-32.8-12.5-45.3 0l-30.1 30.1 59.4 59.4 30.1-30.1c12.5-12.5 12.5-32.8 0-45.3zM96 64C43 64 0 107 0 160v256c0 53 43 96 96 96h256c53 0 96-43 96-96v-96c0-17.7-14.3-32-32-32s-32 14.3-32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V160c0-17.7 14.3-32 32-32h96c17.7 0 32-14.3 32-32s-14.3-32-32-32H96z"/></svg></span>
              Vollmacht am Handy unterschreiben
            </a>
          </div>"""
new_step3 = """          <div class="trust-divider">
            <p style="color:#cbd5e1;font-size:.875rem;margin-bottom:12px">Starte jetzt bequem digital:</p>
            <a href="/auftrag" class="btn-vollmacht">
              <span class="fi"><svg viewBox="0 0 576 512" fill="currentColor"><path d="M402.6 83.2 462 142.6 290 314.6l-72.2 8 8-72.2 172-167.2zM512 92.6 484.6 65.2c-12.5-12.5-32.8-12.5-45.3 0l-30.1 30.1 59.4 59.4 30.1-30.1c12.5-12.5 12.5-32.8 0-45.3zM96 64C43 64 0 107 0 160v256c0 53 43 96 96 96h256c53 0 96-43 96-96v-96c0-17.7-14.3-32-32-32s-32 14.3-32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V160c0-17.7 14.3-32 32-32h96c17.7 0 32-14.3 32-32s-14.3-32-32-32H96z"/></svg></span>
              Online-Auftrag starten
            </a>
          </div>"""
index_astro = index_astro.replace(old_step3, new_step3)

# Note: Astro files might use `vollmacht.html` or `/vollmacht`.
old_step3_alt = old_step3.replace('"/vollmacht"', '"vollmacht.html"')
index_astro = index_astro.replace(old_step3_alt, new_step3)

# 4-Schritte check
old_check = """      <h2 class="h2 uppercase">Der 10-Minuten Online-Check</h2>
      <div class="sec-rule"></div>
      <p class="lead">Prüfe in 3 Klicks, ob dein Auto für die Express-Zulassung in Frage kommt.</p>"""
new_check = """      <h2 class="h2 uppercase">Der 4-Schritte-Check</h2>
      <div class="sec-rule"></div>
      <p class="lead">Prüfe in 4 Klicks, ob dein Fahrzeug für die digitale Express-Zulassung geeignet ist.</p>"""
index_astro = index_astro.replace(old_check, new_check)

with open(os.path.join(astro_dir, 'src', 'pages', 'index.astro'), 'w', encoding='utf-8') as f:
    f.write(index_astro)

# 3. Update Header.astro
header_path = os.path.join(astro_dir, 'src', 'components', 'Header.astro')
if os.path.exists(header_path):
    with open(header_path, 'r', encoding='utf-8') as f:
        header = f.read()
    # Remove Vollmacht link from Desktop Nav
    header = re.sub(r'<a href="/vollmacht".*?Vollmacht\s*</a>', '', header, flags=re.DOTALL)
    # Remove Vollmacht link from Mobile Nav
    header = re.sub(r'<a href="/vollmacht".*?Vollmacht erstellen\s*</a>', '', header, flags=re.DOTALL)
    with open(header_path, 'w', encoding='utf-8') as f:
        f.write(header)

# 4. Update Footer.astro
footer_path = os.path.join(astro_dir, 'src', 'components', 'Footer.astro')
if os.path.exists(footer_path):
    with open(footer_path, 'r', encoding='utf-8') as f:
        footer = f.read()
    footer = footer.replace('| <a href="/vollmacht">Vollmacht</a>', '')
    footer = footer.replace('<a href="/vollmacht">Vollmacht</a> |', '')
    with open(footer_path, 'w', encoding='utf-8') as f:
        f.write(footer)

# 5. Remove vollmacht.astro
vollmacht_path = os.path.join(astro_dir, 'src', 'pages', 'vollmacht.astro')
if os.path.exists(vollmacht_path):
    os.remove(vollmacht_path)

print("Migration completed.")
