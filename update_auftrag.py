import re

def build_new_html():
    new_form_html = """
    <!-- Progress Bar -->
    <div class="af-progress-wrap" style="background:var(--paper-3);border-radius:10px;height:12px;margin-bottom:32px;overflow:hidden">
      <div id="af-progress-bar" style="background:var(--orange);height:100%;width:20%;transition:width 0.4s ease"></div>
    </div>

    <form id="auftragForm" onsubmit="submitAuftrag();return false" novalidate>
      
      <!-- Block 1: Vorgang -->
      <div class="af-block" id="b-vorgang">
        <div class="af-block-head">
          <div class="af-block-num">1</div>
          <h2>Was möchtest du erledigen?</h2>
        </div>
        <div class="af-field">
          <label>Art des Vorgangs *</label>
          <select id="af-vorgang" required onchange="updateProgress(40)">
            <option value="">Bitte wählen...</option>
            <option value="Neuzulassung">Neuzulassung</option>
            <option value="Ummeldung">Ummeldung</option>
            <option value="Abmeldung">Abmeldung</option>
          </select>
        </div>
      </div>

      <!-- Rubbel-Anleitung (Nur bei Zulassung / Ummeldung / Abmeldung relevant) -->
      <div id="rubbel-warning" style="display:none; background:#fef08a; border:1px solid #eab308; border-radius:8px; padding:20px; margin-bottom:24px; color:#854d0e;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
          <svg viewBox="0 0 512 512" fill="currentColor" width="32" height="32" style="flex-shrink:0"><path d="M256 32c14.2 0 27.3 7.5 34.5 19.8l216 368c7.3 12.4 7.3 27.7 .2 40.1S486.3 480 472 480H40c-14.3 0-27.6-7.7-34.7-20.1s-7-27.8 .2-40.1l216-368C228.7 39.5 241.8 32 256 32zm0 128c-13.3 0-24 10.7-24 24V296c0 13.3 10.7 24 24 24s24-10.7 24-24V184c0-13.3-10.7-24-24-24zm32 224a32 32 0 1 0 -64 0 32 32 0 1 0 64 0z"/></svg>
          <h3 style="margin:0; font-size:1.2rem; font-weight:900;">Achtung beim Freilegen der Sicherheitscodes!</h3>
        </div>
        <p style="margin:0 0 16px; font-size:0.95rem; line-height:1.5;">Bitte legen Sie die Codes auf dem Fahrzeugschein, dem Brief und den Kennzeichen extrem vorsichtig frei (abziehen oder vorsichtig rubbeln). <strong>Wenn der Code beschädigt wird, wird das Dokument komplett ungültig und Sie müssen persönlich zur Zulassungsstelle!</strong></p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(150px, 1fr)); gap:16px;">
          <div>
            <div style="background:#fef9c3; height:100px; border:1px dashed #ca8a04; display:flex; align-items:center; justify-content:center; border-radius:8px; font-size:0.8rem; font-weight:bold; text-align:center;">[Platzhalter Bild: Code ZB I]</div>
            <p style="text-align:center; font-size:0.8rem; margin-top:8px; font-weight:600;">Code ZB I (Schein)</p>
          </div>
          <div>
            <div style="background:#fef9c3; height:100px; border:1px dashed #ca8a04; display:flex; align-items:center; justify-content:center; border-radius:8px; font-size:0.8rem; font-weight:bold; text-align:center;">[Platzhalter Bild: Code ZB II]</div>
            <p style="text-align:center; font-size:0.8rem; margin-top:8px; font-weight:600;">Code ZB II (Brief)</p>
          </div>
          <div>
            <div style="background:#fef9c3; height:100px; border:1px dashed #ca8a04; display:flex; align-items:center; justify-content:center; border-radius:8px; font-size:0.8rem; font-weight:bold; text-align:center;">[Platzhalter Bild: Kennzeichen]</div>
            <p style="text-align:center; font-size:0.8rem; margin-top:8px; font-weight:600;">Kennzeichen-Plakette</p>
          </div>
        </div>
      </div>

      <!-- Dynamischer Block: Dokumente & Daten -->
      <div id="b-dynamic" class="af-block" style="display:none;">
        <div class="af-block-head">
          <div class="af-block-num">2</div>
          <h2>Benötigte Unterlagen & Daten</h2>
        </div>
        
        <div class="af-grid" id="dynamic-fields">
          <!-- Felder werden per JS eingefügt -->
        </div>
      </div>

      <!-- Block 3: Kontaktdaten -->
      <div class="af-block" id="b-kontakt" style="display:none;">
        <div class="af-block-head">
          <div class="af-block-num">3</div>
          <h2>Deine Kontaktdaten</h2>
        </div>
        <div class="af-grid">
          <div class="af-field full">
            <label>Vorname / Nachname *</label>
            <input type="text" id="af-name" required onchange="updateProgress(100)">
          </div>
          <div class="af-field">
            <label>Straße + Hausnummer *</label>
            <input type="text" id="af-strasse" required>
          </div>
          <div class="af-field">
            <label>PLZ / Ort *</label>
            <input type="text" id="af-ort" required>
          </div>
          <div class="af-field">
            <label>Telefonnummer *</label>
            <input type="tel" id="af-telefon" required>
          </div>
          <div class="af-field">
            <label>E-Mail Adresse *</label>
            <input type="email" id="af-email" required>
          </div>
        </div>
      </div>

      <!-- Submit Area -->
      <div class="submit-area" id="b-submit" style="display:none;">
        <label class="af-check" style="text-align:left;display:inline-flex;max-width:600px;margin:0 auto 24px">
          <input type="checkbox" id="af-dsgvo" required>
          <span>Ich stimme der Verarbeitung meiner Daten zur Auftragsabwicklung gemäß der <a href="datenschutz.html" style="text-decoration:underline;color:var(--orange)">Datenschutzerklärung</a> zu. *</span>
        </label>

        <p class="submit-tip">Nach dem Klick öffnet sich WhatsApp mit deinen Angaben und Bildern — du tippst nur noch auf Senden.</p>
        
        <button type="submit" class="af-submit" style="max-width:400px;margin:0 auto;width:100%">
          <svg viewBox="0 0 448 512" fill="currentColor"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.2-157zM223.9 438.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.5-186.6 184.5zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/></svg>
          Auftrag per WhatsApp senden
        </button>
      </div>

    </form>
"""

    new_script_html = """
<script>
  // Dynamische Felder Konfiguration
  const fieldsConfig = {
    'Neuzulassung': `
      <div class="af-field full"><label>Fahrzeug-Identifikationsnummer (FIN) *</label><input type="text" id="af-fin" required maxlength="17"></div>
      <div class="af-field"><label>Zulassungsbescheinigung Teil II (Brief) *</label><input type="file" id="af-file-zb2" accept="image/*,.pdf" required></div>
      <div class="af-field"><label>Sicherheitscode ZB II (Brief) *</label><input type="text" id="af-code-zb2" required></div>
      <div class="af-field"><label>COC-Papier *</label><input type="file" id="af-file-coc" accept="image/*,.pdf" required></div>
      <div class="af-field"><label>Personalausweis (Vorder- & Rückseite) *</label><input type="file" id="af-file-ausweis" accept="image/*,.pdf" required multiple></div>
      <div class="af-field"><label>eVB-Nummer (Versicherung) *</label><input type="text" id="af-evb" required placeholder="7-stellig"></div>
      <div class="af-field full"><label>IBAN (für Kfz-Steuer) *</label><input type="text" id="af-iban" required placeholder="DE..."></div>
    `,
    'Ummeldung': `
      <div class="af-field"><label>Sicherheitscode ZB I (Schein) *</label><input type="text" id="af-code-zb1" required></div>
      <div class="af-field"><label>Sicherheitscode ZB II (Brief) *</label><input type="text" id="af-code-zb2" required></div>
      <div class="af-field"><label>Aktueller TÜV/HU-Bericht *</label><input type="file" id="af-file-tuev" accept="image/*,.pdf" required></div>
      <div class="af-field"><label>Sicherheitscodes alte Kennzeichen *</label><input type="text" id="af-code-kz" required placeholder="unter den Plaketten"></div>
      <div class="af-field"><label>eVB-Nummer *</label><input type="text" id="af-evb" required></div>
      <div class="af-field"><label>IBAN (Kfz-Steuer) *</label><input type="text" id="af-iban" required placeholder="DE..."></div>
    `,
    'Abmeldung': `
      <div class="af-field full"><label>Sicherheitscode ZB I (Schein) *</label><input type="text" id="af-code-zb1" required></div>
      <div class="af-field full"><label>Sicherheitscodes abgemeldete Kennzeichen *</label><input type="text" id="af-code-kz" required></div>
    `
  };

  function updateProgress(percent) {
    document.getElementById('af-progress-bar').style.width = percent + '%';
  }

  document.getElementById('af-vorgang').addEventListener('change', function() {
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
    } else {
      dynamicBlock.style.display = 'none';
      warning.style.display = 'none';
      kontakt.style.display = 'none';
      submit.style.display = 'none';
      dynamicFields.innerHTML = '';
      updateProgress(20);
    }
  });

  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function submitAuftrag() {
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
  }
</script>
"""

    with open('auftrag.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Form
    form_pattern = re.compile(r'<form id="auftragForm".*?</form>', re.DOTALL)
    content = form_pattern.sub(new_form_html.strip().replace('\\', '\\\\'), content)

    # Replace Script
    script_pattern = re.compile(r'<script>.*?</script>\s*</body>', re.DOTALL)
    content = script_pattern.sub(new_script_html.strip().replace('\\', '\\\\') + '\n</body>', content)

    with open('auftrag.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    build_new_html()
    print("auftrag.html updated successfully!")
