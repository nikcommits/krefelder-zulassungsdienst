import os
import re

astro_file = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2/src/pages/auftrag.astro'
css_file = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst-Astro-v2/public/styles/system.css'

# 1. Update system.css with global modal styles
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '#sig-modal' not in css_content:
    css_content += """
/* Global Modals */
#sig-modal, #wa-modal {
  position: fixed !important;
  inset: 0 !important;
  z-index: 99999 !important;
  background: rgba(0,0,0,0.85) !important;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.sig-modal-content, .wa-modal-content {
  background: var(--paper-2);
  padding: 32px;
  border-radius: var(--r-lg);
  width: 100%;
  max-width: 700px;
  box-shadow: var(--shadow-lg);
  text-align: center;
}
.sig-modal-content h3, .wa-modal-content h3 {
  font-size: 1.5rem;
  color: var(--orange);
  margin-top: 0;
}
.sig-modal-content p, .wa-modal-content p {
  color: var(--muted);
  line-height: 1.5;
  margin-bottom: 24px;
}
.landscape-hint {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  background: var(--paper-3);
  padding: 12px;
  border-radius: var(--r);
  color: var(--ink);
  font-weight: 600;
  margin-bottom: 16px;
  border: 1px solid var(--orange);
}
.landscape-hint svg {
  width: 24px;
  height: 24px;
  fill: var(--orange);
  animation: rotatePhone 2s infinite ease-in-out;
}
@keyframes rotatePhone {
  0% { transform: rotate(0deg); }
  50% { transform: rotate(-90deg); }
  100% { transform: rotate(0deg); }
}
.wa-loader { display:inline-block; width:48px; height:48px; border:4px solid var(--hair); border-top-color:var(--orange); border-radius:50%; animation:spin 1s linear infinite; margin:0 auto; }
@keyframes spin { 100% { transform:rotate(360deg); } }
"""
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)

# 2. Update auftrag.astro
with open(astro_file, 'r', encoding='utf-8') as f:
    astro_content = f.read()

# Replace the HTML for modals
new_html = """
<!-- Signature Modal -->
<div id="sig-modal" style="display:none;">
  <div class="sig-modal-content">
    <h3>Unterschrift</h3>
    
    <div class="landscape-hint">
      <svg viewBox="0 0 512 512"><path d="M320 0H192C156.7 0 128 28.7 128 64v384c0 35.3 28.7 64 64 64h128c35.3 0 64-28.7 64-64V64c0-35.3-28.7-64-64-64zm32 448c0 17.6-14.4 32-32 32H192c-17.6 0-32-14.4-32-32V64c0-17.6 14.4-32 32-32h128c17.6 0 32 14.4 32 32v384z"/></svg>
      Bitte drehen Sie Ihr Smartphone für eine optimale Unterschrift quer!
    </div>

    <p style="text-align:left; margin-bottom:12px;">Ihre Unterschrift gilt als offizielle Vollmacht für unseren Zulassungsdienst.</p>
    
    <div style="border:2px dashed var(--hair-2); border-radius:var(--r-md); background:#fff; margin-bottom:16px; position:relative; height:250px; touch-action:none; overflow:hidden;">
      <canvas id="sig-canvas" style="width:100%; height:100%; display:block; border-radius:inherit;"></canvas>
    </div>
    
    <div style="display:flex; gap:12px; justify-content:flex-end; flex-wrap:wrap;">
      <button type="button" class="af-submit" style="background:var(--paper-3); color:var(--ink); box-shadow:none; border:1px solid var(--hair-2); width:auto; padding:12px 24px;" onclick="clearSignature()">Löschen</button>
      <button type="button" class="af-submit" style="background:var(--paper-3); color:var(--ink); box-shadow:none; border:1px solid var(--hair-2); width:auto; padding:12px 24px;" onclick="closeSignatureModal()">Abbrechen</button>
      <button type="button" class="af-submit" style="width:auto; padding:12px 32px;" onclick="confirmSignature()">Übernehmen</button>
    </div>
  </div>
</div>

<!-- WA Modal -->
<div id="wa-modal" style="display:none;">
  <div class="wa-modal-content">
    <h3>Auftrag wird erstellt...</h3>
    <p>Bitte warten Sie kurz. Das PDF wird generiert und Sie werden zu WhatsApp weitergeleitet.</p>
    <div class="wa-loader"></div>
  </div>
</div>
"""

# Strip old HTML completely using regex
astro_content = re.sub(r'<!-- Signature Modal -->.*?</div>\s*</div>\s*<!-- WA Modal -->.*?</div>\s*</div>', new_html, astro_content, flags=re.DOTALL)

# Update SignaturePad instantiation for natural pen feel
old_sig_pad = """      signaturePad = new SignaturePad(canvas, {
        backgroundColor: 'rgba(255,255,255,0)',
        penColor: 'rgb(11,26,48)'
      });"""

new_sig_pad = """      signaturePad = new SignaturePad(canvas, {
        backgroundColor: 'rgba(255,255,255,0)',
        penColor: 'rgb(11,26,48)',
        minWidth: 1.0,
        maxWidth: 2.5,
        velocityFilterWeight: 0.7
      });"""

astro_content = astro_content.replace(old_sig_pad, new_sig_pad)

with open(astro_file, 'w', encoding='utf-8') as f:
    f.write(astro_content)

print("Modal styling and signature pad configured.")
