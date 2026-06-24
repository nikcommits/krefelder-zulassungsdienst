import re

def update_vollmacht():
    with open('vollmacht.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add form fields before the Datum & Ort field
    sepa_fields = """
          <div class="vm-field sep">
            <label>SEPA-Lastschriftmandat für Kfz-Steuer</label>
            <p class="hint">Erforderlich für die Zulassungsstelle (Hauptzollamt).</p>
            <input type="text" id="input-sepa-name" placeholder="Vor- und Nachname (Kontoinhaber)" style="margin-bottom:8px" oninput="updatePreview()">
            <input type="text" id="input-sepa-iban" placeholder="IBAN (DE...)" style="margin-bottom:8px" oninput="updatePreview()">
            <input type="text" id="input-sepa-bic" placeholder="BIC (optional)" style="margin-bottom:8px" oninput="updatePreview()">
            <label style="display:flex;align-items:flex-start;gap:8px;font-weight:400;font-size:.8rem;margin-top:12px;cursor:pointer">
              <input type="checkbox" id="input-sepa-check" style="width:16px;height:16px;margin-top:2px">
              <span>Ich erteile hiermit dem Hauptzollamt ein SEPA-Basismandat zum Einzug der Kraftfahrzeugsteuer. *</span>
            </label>
          </div>

          <div class="vm-field sep">
            <label>Datum &amp; Ort</label>"""
    
    content = content.replace('<div class="vm-field sep">\n            <label>Datum &amp; Ort</label>', sepa_fields)

    # 2. Add PDF preview block
    old_consent = """<div class="doc-consent">
          <strong>Einwilligung:</strong><br>
          Der/Die Bevollmächtigte ist berechtigt, Untervollmacht zu erteilen. Ich erkläre mich damit einverstanden, dass der bevollmächtigten Person meine Kraftfahrzeugsteuerrückstände sowie rückständige Gebühren und Auslagen aus vorhergehenden Zulassungsvorgängen mitgeteilt werden dürfen.<br><br>
          <strong>SEPA-Lastschriftmandat:</strong> Ich habe das für die Zulassung erforderliche SEPA-Lastschriftmandat zum Einzug der Kraftfahrzeugsteuer ausgefüllt und unterschrieben beigelegt.
        </div>"""

    new_consent = """<div class="doc-consent" style="margin-bottom:24px">
          <strong>Einwilligung:</strong><br>
          Der/Die Bevollmächtigte ist berechtigt, Untervollmacht zu erteilen. Ich erkläre mich damit einverstanden, dass der bevollmächtigten Person meine Kraftfahrzeugsteuerrückstände sowie rückständige Gebühren und Auslagen aus vorhergehenden Zulassungsvorgängen mitgeteilt werden dürfen.
        </div>

        <div class="doc-block" style="border:1px solid #d1d5db; border-radius:8px; padding:16px; margin-bottom:40px; background:#f9fafb;">
          <h3 style="border-bottom:none; margin-bottom:12px; font-size:1rem;">SEPA-Lastschriftmandat für Kfz-Steuer</h3>
          <p style="font-size:0.75rem; margin-bottom:12px;">Ich ermächtige das zuständige Hauptzollamt, Zahlungen von meinem Konto mittels Lastschrift einzuziehen. Zugleich weise ich mein Kreditinstitut an, die vom Hauptzollamt auf mein Konto gezogenen Lastschriften einzulösen.</p>
          <div style="display:flex; gap:16px; margin-bottom:8px; font-size:0.875rem;">
            <div style="flex:1"><strong>Kontoinhaber:</strong> <span id="out-sepa-name" style="font-family:monospace;">__________________</span></div>
            <div style="flex:1"><strong>BIC:</strong> <span id="out-sepa-bic" style="font-family:monospace;">__________________</span></div>
          </div>
          <div style="font-size:0.875rem;"><strong>IBAN:</strong> <span id="out-sepa-iban" style="font-family:monospace;">____________________________________</span></div>
        </div>"""
    
    content = content.replace(old_consent, new_consent)

    # 3. Update JS preview
    old_js = "document.getElementById('out-ort-datum').textContent      = v('input-ort-datum')      || '___________________________';"
    new_js = """document.getElementById('out-ort-datum').textContent      = v('input-ort-datum')      || '___________________________';
    document.getElementById('out-sepa-name').textContent = v('input-sepa-name') || '__________________';
    document.getElementById('out-sepa-iban').textContent = v('input-sepa-iban') || '____________________________________';
    document.getElementById('out-sepa-bic').textContent = v('input-sepa-bic') || '__________________';"""
    content = content.replace(old_js, new_js)

    # 4. Update Validation
    old_validation = """    var required = ['input-halter-name','input-halter-adresse','input-halter-plz'];
    var missing = false;
    required.forEach(function(id){
      var el = document.getElementById(id);
      if(!el.value.trim()){ el.classList.add('invalid'); missing = true; }
      else { el.classList.remove('invalid'); }
    });
    if(missing){
      alert('Bitte fülle Name, Straße und PLZ/Ort des Fahrzeughalters aus.');
      document.getElementById(required[0]).focus();
      return;
    }"""
    
    new_validation = """    var required = ['input-halter-name','input-halter-adresse','input-halter-plz', 'input-sepa-name', 'input-sepa-iban'];
    var missing = false;
    required.forEach(function(id){
      var el = document.getElementById(id);
      if(!el.value.trim()){ el.classList.add('invalid'); missing = true; }
      else { el.classList.remove('invalid'); }
    });
    var chk = document.getElementById('input-sepa-check');
    if(!chk.checked){ chk.parentElement.style.color = 'red'; missing = true; }
    else { chk.parentElement.style.color = ''; }

    if(missing){
      alert('Bitte fülle alle Pflichtfelder sowie die SEPA-Informationen aus und akzeptiere das Mandat.');
      return;
    }"""

    content = content.replace(old_validation, new_validation)

    with open('vollmacht.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_vollmacht()
    print("vollmacht.html updated successfully!")
