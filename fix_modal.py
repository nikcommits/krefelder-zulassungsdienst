import re

file_path = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2/src/pages/auftrag.astro'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS to append
css_append = """
  #sig-modal { position:fixed; inset:0; z-index:9999; background:rgba(0,0,0,0.8); display:none; align-items:center; justify-content:center; padding:20px; }
  .sig-modal-content { background:var(--paper-2); padding:32px; border-radius:var(--r-lg); width:100%; max-width:600px; box-shadow:var(--shadow-lg); }
  .sig-modal-content h3 { font-size:1.5rem; color:var(--ink); margin-top:0; }
  .sig-modal-content p { color:var(--muted); line-height:1.5; margin-bottom:24px; }
"""

# HTML to append just before the script tag
html_append = """
<!-- Signature Modal -->
<div id="sig-modal">
  <div class="sig-modal-content">
    <h3>Unterschrift</h3>
    <p>Bitte unterschreiben Sie im Feld unten. Dies gilt als Vollmacht für den Zulassungsdienst.</p>
    <div style="border:1px solid var(--hair-2); border-radius:var(--r-md); background:#fff; margin-bottom:16px; position:relative; height:200px; touch-action:none;">
      <canvas id="sig-canvas" style="width:100%; height:100%; display:block; border-radius:inherit;"></canvas>
    </div>
    <div style="display:flex; gap:12px; justify-content:flex-end;">
      <button type="button" class="btn btn-ghost" onclick="clearSignature()">Löschen</button>
      <button type="button" class="btn btn-ghost" onclick="closeSignatureModal()">Abbrechen</button>
      <button type="button" class="btn btn-orange" onclick="confirmSignature()">Übernehmen</button>
    </div>
  </div>
</div>

<!-- WA Modal -->
<div id="wa-modal">
  <div class="wa-modal-content">
    <h3>Auftrag wird erstellt...</h3>
    <p>Bitte warten Sie kurz. Das PDF wird generiert und Sie werden zu WhatsApp weitergeleitet.</p>
    <div class="wa-loader"></div>
  </div>
</div>
"""

if '#sig-modal {' not in content:
    content = content.replace('/* Modal & Signature */', '/* Modal & Signature */\n' + css_append)

if 'id="sig-modal"' not in content:
    content = content.replace('<script is:inline>', html_append + '\n<script is:inline>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modals added.")
