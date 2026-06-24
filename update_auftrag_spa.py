import sys

file_path = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst/auftrag.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add scripts to head
head_insert = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/signature_pad@4.1.7/dist/signature_pad.umd.min.js" defer></script>
</head>
"""
if "html2pdf" not in html:
    html = html.replace("</head>", head_insert)

# 2. Add CSS to head
css_insert = """
  /* Modal & Signature */
  #wa-modal { position:fixed; inset:0; z-index:9999; background:rgba(0,0,0,0.8); display:none; align-items:center; justify-content:center; padding:20px; }
  .wa-modal-content { background:var(--paper-2); padding:32px; border-radius:var(--r-lg); text-align:center; max-width:500px; box-shadow:var(--shadow-lg); }
  .wa-modal-content h3 { font-size:1.5rem; color:var(--orange); margin-top:0; }
  .wa-modal-content p { color:var(--muted); line-height:1.5; margin-bottom:24px; }
  .wa-loader { display:inline-block; width:48px; height:48px; border:4px solid var(--hair); border-top-color:var(--orange); border-radius:50%; animation:spin 1s linear infinite; }
  @keyframes spin { 100% { transform:rotate(360deg); } }

  .sig-box { border:2px dashed var(--hair-2); border-radius:var(--r); background:var(--paper-3); position:relative; overflow:hidden; touch-action:none; margin-bottom:16px; }
  .sig-watermark { position:absolute; inset:0; pointer-events:none; display:flex; align-items:center; justify-content:center; opacity:.1; }
  .sig-watermark span { font-size:1.5rem; font-weight:900; text-transform:uppercase; letter-spacing:.1em; transform:rotate(-10deg); color:var(--muted); }
  canvas#sig-canvas { display:block; width:100%; height:200px; cursor:crosshair; }
  .sig-actions { display:flex; justify-content:flex-end; gap:8px; margin-bottom:24px; }
  .sig-btn { background:transparent; border:1px solid var(--hair-2); padding:6px 12px; border-radius:var(--r-sm); font-size:0.875rem; cursor:pointer; color:var(--muted); }
  .sig-btn:hover { background:var(--hair); color:var(--ink); }

  /* PDF Content (hidden) */
  #pdf-wrap { display:none; }
  #pdf-content { background:#ffffff; padding:40px; font-size:.875rem; width:100%; max-width:210mm; min-height:297mm; color:#1f2937; }
  #pdf-content * { box-sizing:border-box; }
  #pdf-content .doc-head { margin-bottom:48px; border-bottom:2px solid var(--orange); padding-bottom:16px; display:flex; justify-content:space-between; align-items:flex-end; gap:16px; }
  #pdf-content .doc-head h1 { font-size:1.5rem; font-weight:700; text-transform:uppercase; letter-spacing:.08em; margin:0; color:#1f2937; }
  #pdf-content .doc-head p { color:#6b7280; margin:4px 0 0; }
  #pdf-content .doc-head .right { text-align:right; font-size:.75rem; color:#6b7280; }
  #pdf-content .doc-block { margin-bottom:32px; }
  #pdf-content .doc-block h3 { font-weight:700; border-bottom:1px solid #d1d5db; margin:0 0 8px; padding-bottom:4px; font-size:1rem; color:#1f2937; }
  #pdf-content .pl { padding-left:8px; }
  #pdf-content .out-line { min-height:1.5rem; }
  #pdf-content .out-name { font-weight:700; font-size:1rem; }
  #pdf-content .out-muted { color:#374151; }
  #pdf-content .doc-list { list-style:disc; padding-left:24px; margin:16px 0; }
  #pdf-content .doc-list li { margin-bottom:4px; }
  #pdf-content .doc-kfz { display:flex; gap:8px; padding-left:8px; }
  #pdf-content .doc-kfz .val { font-family:monospace; background:#f3f4f6; padding:0 8px; border-radius:4px; min-width:200px; display:inline-block; }
  #pdf-content .doc-consent { background:#fff7ed; padding:16px; border:1px solid #ffedd5; border-radius:8px; font-size:.75rem; line-height:1.6; color:#374151; margin-bottom:40px; }
  #pdf-content .doc-sepa { border:1px solid #d1d5db; border-radius:8px; padding:16px; margin-bottom:40px; background:#f9fafb; }
  #pdf-content .doc-sign { margin-top:64px; display:flex; justify-content:space-between; align-items:flex-end; gap:24px; }
  #pdf-content .doc-sign .col { width:50%; }
  #pdf-content .doc-sign .line { font-size:.75rem; color:#6b7280; border-top:1px solid #9ca3af; padding-top:4px; }
  #pdf-content .doc-sign .sig-area { min-height:3rem; display:flex; align-items:flex-end; justify-content:center; position:relative; margin-bottom:4px; }
  #pdf-content .doc-sign .sig-area img { max-height:64px; object-fit:contain; }
</style>
"""
if "#wa-modal" not in html:
    html = html.replace("</style>", css_insert)

# 3. Signature block in submit area
sig_html = """
        <div class="af-field" style="text-align:left; max-width:600px; margin:0 auto 24px">
          <label style="display:block; font-weight:700; margin-bottom:8px;">Ihre Unterschrift für die Vollmacht *</label>
          <div class="sig-box">
            <div class="sig-watermark"><span>Hier zeichnen</span></div>
            <canvas id="sig-canvas"></canvas>
          </div>
          <div class="sig-actions">
            <button type="button" class="sig-btn" onclick="clearSignature()">Neu / Löschen</button>
          </div>
        </div>

        <label class="af-check" style="text-align:left;display:inline-flex;max-width:600px;margin:0 auto 24px">
"""
if "sig-box" not in html:
    html = html.replace('<label class="af-check" style="text-align:left;display:inline-flex;max-width:600px;margin:0 auto 24px">', sig_html)


# 4. Hidden PDF template and modal before closing body
pdf_modal_html = """
<div id="wa-modal">
  <div class="wa-modal-content">
    <div class="wa-loader"></div>
    <h3>Fast geschafft!</h3>
    <p>Ihre Vollmacht wurde generiert und als PDF heruntergeladen.<br><br>Sie werden nun zu WhatsApp weitergeleitet. <strong>Bitte vergessen Sie nicht, die heruntergeladene Vollmacht-PDF sowie Ihre Fotos (Ausweis, Fahrzeugdokumente) im Chat anzuhängen!</strong></p>
  </div>
</div>

<div id="pdf-wrap">
  <div id="pdf-content">
    <div class="doc-head">
      <div>
        <h1>Vollmacht</h1>
        <p>zur Vorlage bei der Kfz-Zulassungsbehörde</p>
      </div>
      <div class="right"><strong>Zulassungsdienst Kennwerk</strong><br>Grüner Dyk 70<br>47803 Krefeld</div>
    </div>
    <div class="doc-block">
      <h3>Vollmachtgeber (Fahrzeughalter/in)</h3>
      <div class="pl">
        <div id="out-halter-name" class="out-line out-name"></div>
        <div id="out-halter-adresse" class="out-line out-muted"></div>
        <div id="out-halter-plz" class="out-line out-muted"></div>
      </div>
    </div>
    <div class="doc-block">
      <h3>Bevollmächtigte(r)</h3>
      <div class="pl">
        <div class="out-name">Omar Zouaoui (Zulassungsdienst Kennwerk)</div>
        <div class="out-muted">Grüner Dyk 70</div>
        <div class="out-muted">47803 Krefeld</div>
      </div>
    </div>
    <div class="doc-block">
      <p style="margin:0 0 16px">Hiermit bevollmächtige ich die oben genannte Person, mein Kraftfahrzeug bei der Zulassungsbehörde</p>
      <ul class="doc-list">
        <li>zuzulassen / umzumelden</li>
        <li>außer Betrieb zu setzen (abzumelden)</li>
        <li>Fahrzeugpapiere oder Ersatzpapiere zu beantragen und in Empfang zu nehmen</li>
        <li>Wunschkennzeichen zu reservieren</li>
      </ul>
    </div>
    <div class="doc-block" id="doc-kfz-block">
      <h3>Angaben zum Fahrzeug (falls bekannt)</h3>
      <div class="doc-kfz"><span>Kennzeichen / FIN:</span><span id="out-kfz" class="val"></span></div>
    </div>
    <div class="doc-consent" style="margin-bottom:24px">
      <strong>Einwilligung:</strong><br>
      Der/Die Bevollmächtigte ist berechtigt, Untervollmacht zu erteilen. Ich erkläre mich damit einverstanden, dass der bevollmächtigten Person meine Kraftfahrzeugsteuerrückstände sowie rückständige Gebühren und Auslagen aus vorhergehenden Zulassungsvorgängen mitgeteilt werden dürfen.
    </div>
    <div class="doc-block doc-sepa" id="doc-sepa-block">
      <h3 style="border-bottom:none; margin-bottom:12px; font-size:1rem;">SEPA-Lastschriftmandat für Kfz-Steuer</h3>
      <p style="font-size:0.75rem; margin-bottom:12px;">Ich ermächtige das zuständige Hauptzollamt, Zahlungen von meinem Konto mittels Lastschrift einzuziehen. Zugleich weise ich mein Kreditinstitut an, die vom Hauptzollamt auf mein Konto gezogenen Lastschriften einzulösen.</p>
      <div style="display:flex; gap:16px; margin-bottom:8px; font-size:0.875rem;">
        <div style="flex:1"><strong>Kontoinhaber:</strong> <span id="out-sepa-name" style="font-family:monospace;"></span></div>
      </div>
      <div style="font-size:0.875rem;"><strong>IBAN:</strong> <span id="out-sepa-iban" style="font-family:monospace;"></span></div>
    </div>
    <div class="doc-sign">
      <div class="col">
        <div id="out-ort-datum" class="out-line" style="margin-bottom:4px"></div>
        <div class="line" style="width:75%">Ort, Datum</div>
      </div>
      <div class="col" style="text-align:right">
        <div class="sig-area" style="margin-left:auto;width:75%">
          <img id="out-signature-img" src="" alt="" style="display:none;">
        </div>
        <div class="line" style="width:75%;margin-left:auto;text-align:center">Unterschrift des Vollmachtgebers</div>
      </div>
    </div>
  </div>
</div>

<script>
"""
if "pdf-wrap" not in html:
    html = html.replace("<script>", pdf_modal_html)

# 5. Modify Javascript Logic
js_replace = """  function updateProgress(percent) {
    document.getElementById('af-progress-bar').style.width = percent + '%';
  }

  // --- NEU: SPA LOGIK ---
  function syncDataToPDF() {
    var v = function(id){ var el = document.getElementById(id); return el ? el.value : ''; };
    document.getElementById('out-halter-name').textContent = v('af-name');
    document.getElementById('out-halter-adresse').textContent = v('af-strasse');
    document.getElementById('out-halter-plz').textContent = v('af-ort');
    
    var kfz = v('af-fin') || v('af-code-kz') || '';
    document.getElementById('out-kfz').textContent = kfz;

    document.getElementById('out-sepa-name').textContent = v('af-name');
    document.getElementById('out-sepa-iban').textContent = v('af-iban');
  }

  document.getElementById('auftragForm').addEventListener('input', syncDataToPDF);

  window.addEventListener('load', function(){
    var today = new Date();
    document.getElementById('out-ort-datum').textContent = 'Krefeld, den ' + today.toLocaleDateString('de-DE');
  });

  let signaturePad;
  function initSignaturePad() {
    if (signaturePad) return;
    const canvas = document.getElementById('sig-canvas');
    if(canvas) {
      signaturePad = new SignaturePad(canvas, {
        backgroundColor: 'rgba(255,255,255,0)',
        penColor: 'rgb(11,26,48)'
      });
      resizeCanvas();
      window.addEventListener('resize', resizeCanvas);
    }
  }
  function resizeCanvas() {
    const canvas = document.getElementById('sig-canvas');
    if(!canvas) return;
    const ratio = Math.max(window.devicePixelRatio || 1, 1);
    const w = canvas.offsetWidth;
    const h = canvas.offsetHeight;
    if(canvas.width !== w * ratio || canvas.height !== h * ratio) {
        canvas.width = w * ratio;
        canvas.height = h * ratio;
        canvas.getContext('2d').scale(ratio, ratio);
        if(signaturePad) signaturePad.clear();
    }
  }
  function clearSignature() {
    if(signaturePad) signaturePad.clear();
  }
  // -----------------------"""
if "syncDataToPDF" not in html:
    html = html.replace("  function updateProgress(percent) {\n    document.getElementById('af-progress-bar').style.width = percent + '%';\n  }", js_replace)

vorgang_original = """  document.getElementById('af-vorgang').addEventListener('change', function() {
    const val = this.value;
    const dynamicBlock = document.getElementById('b-dynamic');
    const dynamicFields = document.getElementById('dynamic-fields');
    const warning = document.getElementById('rubbel-warning');
    const kontakt = document.getElementById('b-kontakt');
    const submit = document.getElementById('b-submit');
    
    if (val && fieldsConfig[val]) {
      dynamicFields.innerHTML = fieldsConfig[val];
      dynamicBlock.style.display = 'block';
      warning.style.display = 'block';
      kontakt.style.display = 'block';
      submit.style.display = 'block';
      updateProgress(60);
    } else {"""

vorgang_replace = """  document.getElementById('af-vorgang').addEventListener('change', function() {
    const val = this.value;
    const dynamicBlock = document.getElementById('b-dynamic');
    const dynamicFields = document.getElementById('dynamic-fields');
    const warning = document.getElementById('rubbel-warning');
    const kontakt = document.getElementById('b-kontakt');
    const submit = document.getElementById('b-submit');
    const sepaBlock = document.getElementById('doc-sepa-block');
    
    if (val && fieldsConfig[val]) {
      dynamicFields.innerHTML = fieldsConfig[val];
      dynamicBlock.style.display = 'block';
      
      if (val !== 'Abmeldung') {
          warning.style.display = 'block';
          if (sepaBlock) sepaBlock.style.display = 'block';
      } else {
          warning.style.display = 'none';
          if (sepaBlock) sepaBlock.style.display = 'none';
      }
      
      kontakt.style.display = 'block';
      submit.style.display = 'block';
      setTimeout(initSignaturePad, 50);
      updateProgress(60);
    } else {"""
html = html.replace(vorgang_original, vorgang_replace)

submit_original = """  function submitAuftrag() {
    let isValid = true;
    
    // Einfache Validierung (alle visible required inputs)
    const inputs = document.querySelectorAll('#auftragForm input[required], #auftragForm select[required]');
    inputs.forEach(el => {
      if (el.offsetWidth > 0 && el.offsetHeight > 0) { // is visible
        el.classList.remove('invalid');
        if (!el.value.trim() && el.type !== 'checkbox' && el.type !== 'file') {
          el.classList.add('invalid');
          isValid = false;
        }
        if (el.type === 'checkbox' && !el.checked) {
          el.parentElement.classList.add('invalid');
          isValid = false;
        }
        // File validation kann ignoriert werden in WhatsApp flow, wir weisen nur darauf hin,
        // dass die Files parallel per WhatsApp geschickt werden müssen.
      }
    });

    const emailEl = document.getElementById('af-email');
    if (emailEl && emailEl.value.trim() && !isValidEmail(emailEl.value.trim())) {
      emailEl.classList.add('invalid');
      isValid = false;
    }

    if (!isValid) {
      alert("Bitte füllen Sie alle erforderlichen Felder aus.");
      return;
    }

    // Collect Data
    const vorgang = document.getElementById('af-vorgang').value;
    let text = `Hallo! Ich möchte einen neuen Auftrag erteilen:\\n\\nVorgang: *${vorgang}*\\n\\n`;
    
    const fieldsToCollect = [
      { id: 'af-name', label: 'Name' },
      { id: 'af-strasse', label: 'Straße' },
      { id: 'af-ort', label: 'Ort' },
      { id: 'af-telefon', label: 'Telefon' },
      { id: 'af-email', label: 'E-Mail' },
      { id: 'af-fin', label: 'FIN' },
      { id: 'af-code-zb1', label: 'Code ZB I' },
      { id: 'af-code-zb2', label: 'Code ZB II' },
      { id: 'af-code-kz', label: 'Code Kennzeichen' },
      { id: 'af-evb', label: 'eVB' },
      { id: 'af-iban', label: 'IBAN' }
    ];

    fieldsToCollect.forEach(f => {
      const el = document.getElementById(f.id);
      if (el && el.value.trim() && el.offsetWidth > 0) {
        text += `*${f.label}:* ${el.value.trim()}\\n`;
      }
    });
    
    text += `\\nBitte teilen Sie mir mit, wo ich die hochgeladenen Dokumente (Ausweis, ZB, COC etc.) hinsenden soll.`;

    const waLink = "https://wa.me/491728474357?text=" + encodeURIComponent(text);
    window.open(waLink, '_blank');
  }"""

submit_replace = """  async function submitAuftrag() {
    let isValid = true;
    
    const inputs = document.querySelectorAll('#auftragForm input[required], #auftragForm select[required]');
    inputs.forEach(el => {
      if (el.offsetWidth > 0 && el.offsetHeight > 0) { 
        el.classList.remove('invalid');
        if (!el.value.trim() && el.type !== 'checkbox' && el.type !== 'file') {
          el.classList.add('invalid');
          isValid = false;
        }
        if (el.type === 'checkbox' && !el.checked) {
          el.parentElement.classList.add('invalid');
          isValid = false;
        }
      }
    });

    const emailEl = document.getElementById('af-email');
    if (emailEl && emailEl.value.trim() && !isValidEmail(emailEl.value.trim())) {
      emailEl.classList.add('invalid');
      isValid = false;
    }

    if (!isValid) {
      alert("Bitte füllen Sie alle erforderlichen Felder aus.");
      return;
    }

    if (!signaturePad || signaturePad.isEmpty()) {
      alert("Bitte unterschreiben Sie die Vollmacht.");
      return;
    }

    syncDataToPDF(); 
    const dataURL = signaturePad.toDataURL('image/png');
    const sigImg = document.getElementById('out-signature-img');
    sigImg.src = dataURL;
    sigImg.style.display = 'inline-block';

    const modal = document.getElementById('wa-modal');
    modal.style.display = 'flex';

    const element = document.getElementById('pdf-content');
    const opt = {
      margin: 0,
      filename: 'Vollmacht_Zulassungsdienst.pdf',
      image: { type: 'jpeg', quality: 0.98 },
      html2canvas: { scale: 2 },
      jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
    };
    
    try {
      await html2pdf().set(opt).from(element).save();
    } catch(err) {
      console.error(err);
    }

    const vorgang = document.getElementById('af-vorgang').value;
    let text = "Hallo, hier sind die Daten für meinen Zulassungsauftrag. Die soeben heruntergeladene, unterschriebene Vollmacht (inkl. SEPA-Mandat) sowie die Fotos meines Ausweises und der weiteren Fahrzeugdokumente (z. B. TÜV-Bericht oder COC) lade ich gleich hier in den Chat hoch!\\n\\n";
    text += `Vorgang: *${vorgang}*\\n\\n`;
    
    const fieldsToCollect = [
      { id: 'af-name', label: 'Name' },
      { id: 'af-strasse', label: 'Straße' },
      { id: 'af-ort', label: 'Ort' },
      { id: 'af-telefon', label: 'Telefon' },
      { id: 'af-email', label: 'E-Mail' },
      { id: 'af-fin', label: 'FIN' },
      { id: 'af-code-zb1', label: 'Code ZB I' },
      { id: 'af-code-zb2', label: 'Code ZB II' },
      { id: 'af-code-kz', label: 'Code Kennzeichen' },
      { id: 'af-evb', label: 'eVB' },
      { id: 'af-iban', label: 'IBAN' }
    ];

    fieldsToCollect.forEach(f => {
      const el = document.getElementById(f.id);
      if (el && el.value.trim() && el.offsetWidth > 0) {
        text += `*${f.label}:* ${el.value.trim()}\\n`;
      }
    });

    const waLink = "https://wa.me/491728474357?text=" + encodeURIComponent(text);
    
    setTimeout(() => {
      window.location.href = waLink;
    }, 1500); 
  }"""
if "async function submitAuftrag" not in html:
    html = html.replace(submit_original, submit_replace)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated auftrag.html successfully.")
