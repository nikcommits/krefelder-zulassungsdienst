import sys

file_path = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst/auftrag.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace inline signature block with Button + Preview
old_sig_html = """        <div class="af-field" style="text-align:left; max-width:600px; margin:0 auto 24px">
          <label style="display:block; font-weight:700; margin-bottom:8px;">Ihre Unterschrift für die Vollmacht *</label>
          <div class="sig-box">
            <div class="sig-watermark"><span>Hier zeichnen</span></div>
            <canvas id="sig-canvas"></canvas>
          </div>
          <div class="sig-actions">
            <button type="button" class="sig-btn" onclick="clearSignature()">Neu / Löschen</button>
          </div>
        </div>"""

new_sig_html = """        <div class="af-field" style="text-align:left; max-width:600px; margin:0 auto 24px">
          <label style="display:block; font-weight:700; margin-bottom:8px;">Ihre Unterschrift für die Vollmacht *</label>
          <button type="button" id="open-sig-btn" class="af-submit" style="background:var(--paper-3); color:var(--ink); font-weight:600; padding:12px; font-size:1rem; box-shadow:none; border:1px solid var(--hair-2); display:flex; align-items:center; justify-content:center; gap:8px;" onclick="openSignatureModal()">
            <svg viewBox="0 0 640 512" fill="currentColor" width="20" height="20"><path d="M623.2 192c-51.8 3.5-125.7 54.7-163.1 88.5-26.6 24-46.6 5.8-21.9-22.4 14.2-16.2 70.6-67.6 70.6-92.6 0-15.4-21-13.4-35.4-9.8-37.2 9.4-71.9 30.4-100.7 56.5-22.3 20.2-41.8 43.3-57.9 68.5-7.7 12-39.3 84.5-47.4 87.8-12.9 5.4-26.9-21.2-31.8-30.6-13.8-26.4-24.7-54.5-34.7-82.5-23.9 23.9-46.6 33.5-72.5 14.8C29.1 348.4 0 401.4 0 401.4s30.7 21.3 49.4 6.9c20.3-15.6 34-39.5 48.5-59.8 8.8 22.9 33.6 92.6 70.7 86.3 36-6.1 65.2-95.6 78.6-126.5 19.2-44.4 56.7-99.1 105.8-114.2 0 22.7-49.6 70.9-65 86.4-21.1 21.2-13.3 51.5 15.3 49.7 32.1-2 116.6-77.3 156.3-82.4 16.7-2.2 24-15.2 24-31.1 0-26.4-87.5-26.4-104-15z"/></svg>
            Hier digital unterschreiben
          </button>
          <div id="sig-preview-wrap" style="display:none; text-align:center; margin-top:12px; border:1px solid #16a34a; border-radius:8px; padding:12px; background:#f0fdf4;">
            <img id="sig-preview-img" src="" alt="Ihre Unterschrift" style="max-height:80px; mix-blend-mode:multiply;">
          </div>
        </div>"""
html = html.replace(old_sig_html, new_sig_html)


# 2. Add Signature Modal HTML before wa-modal
modal_html = """
<div id="sig-modal" style="position:fixed; inset:0; z-index:10000; background:#ffffff; display:none; flex-direction:column;">
  <div style="padding:16px; border-bottom:1px solid var(--hair); display:flex; justify-content:space-between; align-items:center;">
    <h3 style="margin:0; font-size:1.25rem;">Bitte unterschreiben</h3>
    <button type="button" onclick="closeSignatureModal()" style="background:transparent; border:none; font-size:1.5rem; cursor:pointer;">&times;</button>
  </div>
  <div style="flex-grow:1; position:relative; background:#ffffff; touch-action:none;">
    <div class="sig-watermark" style="opacity:0.05;"><span>Hier zeichnen</span></div>
    <canvas id="sig-canvas" style="width:100%; height:100%; cursor:crosshair; position:absolute; inset:0;"></canvas>
  </div>
  <div style="padding:16px; border-top:1px solid var(--hair); display:flex; flex-direction:column; gap:12px;">
    <button type="button" onclick="clearSignature()" style="background:transparent; border:none; color:var(--muted); font-size:0.875rem; text-decoration:underline; cursor:pointer; padding:8px;">Löschen / Neu</button>
    <button type="button" class="af-submit" onclick="confirmSignature()" style="margin:0;">Unterschrift bestätigen</button>
  </div>
</div>

<div id="wa-modal">
"""
html = html.replace('<div id="wa-modal">', modal_html)


# 3. JS Changes: Add modal logic and modify submitAuftrag
js_additions = """  // --- NEU: SPA LOGIK ---
  let signatureBase64 = null;

  function openSignatureModal() {
    document.getElementById('sig-modal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
    initSignaturePad();
    setTimeout(resizeCanvas, 50); 
  }

  function closeSignatureModal() {
    document.getElementById('sig-modal').style.display = 'none';
    document.body.style.overflow = '';
  }

  function confirmSignature() {
    if(!signaturePad || signaturePad.isEmpty()) {
      alert("Bitte unterschreiben Sie zuerst.");
      return;
    }
    signatureBase64 = signaturePad.toDataURL('image/png');
    
    document.getElementById('sig-preview-img').src = signatureBase64;
    document.getElementById('sig-preview-wrap').style.display = 'block';
    
    const btn = document.getElementById('open-sig-btn');
    btn.innerHTML = `<svg viewBox="0 0 512 512" fill="#16a34a" width="20" height="20"><path d="M470.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L192 338.7 425.4 105.4c12.5-12.5 32.8-12.5 45.3 0z"/></svg> Unterschrift ändern`;
    btn.style.border = "1px solid #16a34a";
    btn.style.color = "#16a34a";

    closeSignatureModal();
  }

  function syncDataToPDF() {"""
html = html.replace("  // --- NEU: SPA LOGIK ---\n  function syncDataToPDF() {", js_additions)


# 4. Remove setTimeout(initSignaturePad, 50); from af-vorgang change listener
html = html.replace("      setTimeout(initSignaturePad, 50);\n", "")


# 5. Modify signature validation in submitAuftrag
old_val = """    if (!signaturePad || signaturePad.isEmpty()) {
      alert("Bitte unterschreiben Sie die Vollmacht.");
      return;
    }

    syncDataToPDF(); 
    const dataURL = signaturePad.toDataURL('image/png');
    const sigImg = document.getElementById('out-signature-img');
    sigImg.src = dataURL;
    sigImg.style.display = 'inline-block';"""

new_val = """    if (!signatureBase64) {
      alert("Bitte unterschreiben Sie die Vollmacht.");
      return;
    }

    syncDataToPDF(); 
    const sigImg = document.getElementById('out-signature-img');
    sigImg.src = signatureBase64;
    sigImg.style.display = 'inline-block';"""
html = html.replace(old_val, new_val)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Modal update applied successfully.")
