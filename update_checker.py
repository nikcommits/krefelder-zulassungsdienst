import re

def update_checker():
    new_checker_html = """
    <div class="checker-box" id="checker-container">
      <!-- Q1 -->
      <div id="step-1" class="checker-step">
        <div class="q-label">Frage 1 von 4</div>
        <h3>Wurde Ihr Fahrzeugschein (Zulassungsbescheinigung Teil I) nach dem 01.01.2015 ausgestellt?</h3>
        <p class="checker-hint" style="margin-bottom:16px;">Nur dann besitzt der Schein den verdeckten Sicherheitscode zum Freirubbeln.</p>
        <div class="q-opts">
          <button class="opt opt-primary" onclick="nextStep(1, true)">Ja, nach 01.01.2015 <svg viewBox="0 0 448 512" fill="currentColor"><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.7 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/></svg></button>
          <button class="opt opt-ghost" onclick="showResult(false)">Nein, davor <svg viewBox="0 0 448 512" fill="currentColor"><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.7 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/></svg></button>
        </div>
      </div>

      <!-- Q2 -->
      <div id="step-2" class="checker-step hidden">
        <div class="q-label">Frage 2 von 4</div>
        <h3>Wurde Ihr Fahrzeugbrief (Zulassungsbescheinigung Teil II) nach dem 01.01.2018 ausgestellt?</h3>
        <p class="checker-hint" style="margin-bottom:16px;">Ab diesem Datum hat auch der Brief einen entsprechenden Sicherheitscode.</p>
        <div class="q-opts">
          <button class="opt opt-primary" onclick="nextStep(2, true)">Ja, nach 01.01.2018 <svg viewBox="0 0 448 512" fill="currentColor"><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.7 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/></svg></button>
          <button class="opt opt-ghost" onclick="showResult(false)">Nein, davor <svg viewBox="0 0 448 512" fill="currentColor"><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.7 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/></svg></button>
        </div>
      </div>

      <!-- Q3 -->
      <div id="step-3" class="checker-step hidden">
        <div class="q-label">Frage 3 von 4</div>
        <h3>Hast du die Kennzeichenschilder mit den freirubbelbaren Plaketten?</h3>
        <p class="checker-hint" style="margin-bottom:16px;">Gilt nur, wenn das Fahrzeug noch zugelassen ist.</p>
        <div class="q-opts">
          <button class="opt opt-primary" onclick="nextStep(3, true)">Ja / Fahrzeug ist abgemeldet <svg viewBox="0 0 448 512" fill="currentColor"><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.7 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/></svg></button>
          <button class="opt opt-ghost" onclick="showResult(false)">Nein <svg viewBox="0 0 448 512" fill="currentColor"><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.7 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/></svg></button>
        </div>
      </div>

      <!-- Q4 -->
      <div id="step-4" class="checker-step hidden">
        <div class="q-label">Frage 4 von 4</div>
        <h3>Hast du deinen gültigen Personalausweis oder Reisepass zur Hand?</h3>
        <div class="q-opts">
          <button class="opt opt-primary" onclick="showResult(true)">Ja, liegt bereit <svg viewBox="0 0 448 512" fill="#4ade80"><path d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z"/></svg></button>
          <button class="opt opt-ghost" onclick="showResult(false)">Nein, gerade nicht <svg viewBox="0 0 384 512" fill="#f87171"><path d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"/></svg></button>
        </div>
      </div>

      <!-- Result OK -->
      <div id="result-success" class="checker-step result hidden">
        <div class="badge badge-ok"><svg viewBox="0 0 448 512" fill="currentColor"><path d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z"/></svg></div>
        <h3>Perfekt! Einer digitalen 10-Minuten-Zulassung steht nichts im Weg.</h3>
        <p>Ihre Dokumente verfügen über die notwendigen verdeckten Sicherheitscodes für das i-Kfz-Verfahren.</p>
        <div style="margin-bottom:12px"><a href="auftrag.html" class="btn btn-orange glow btn-lg">Zum digitalen Auftragsformular</a></div>
        <div><button onclick="resetChecker()" class="link-reset">Test neustarten</button></div>
      </div>

      <!-- Result Manual -->
      <div id="result-manual" class="checker-step result hidden">
        <div class="badge badge-call" style="background:#fef08a;color:#ca8a04;"><svg viewBox="0 0 512 512" fill="currentColor"><path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zm0-384c13.3 0 24 10.7 24 24V264c0 13.3-10.7 24-24 24s-24-10.7-24-24V152c0-13.3 10.7-24 24-24zM224 352a32 32 0 1 1 64 0 32 32 0 1 1 -64 0z"/></svg></div>
        <h3>Klassische Zulassung erforderlich.</h3>
        <p>Leider sind Ihre Fahrzeugpapiere zu alt für die digitale Sofort-Zulassung (es fehlen die verdeckten Sicherheitscodes). Wir übernehmen die Anmeldung gern über unseren klassischen Zulassungsdienst für Sie!</p>
        <a href="https://wa.me/491728474357" class="btn btn-orange glow btn-lg" target="_blank">
          Klassischen Zulassungsdienst anfragen
        </a>
        <div style="margin-top:16px"><button onclick="resetChecker()" class="link-reset">Test neustarten</button></div>
      </div>
    </div>
"""

    new_script_html = """
<script>
  // Mobile menu toggle
  function toggleMenu(btn){
    var nav = document.getElementById('mobileNav');
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  function closeMenu(){
    document.getElementById('mobileNav').classList.remove('open');
    document.querySelector('.hamburger').setAttribute('aria-expanded','false');
  }

  // 10-Minuten Checker
  function nextStep(currentStep, answer){
    if(!answer) {
        showResult(false);
        return;
    }
    document.getElementById('step-' + currentStep).classList.add('hidden');
    document.getElementById('step-' + (currentStep + 1)).classList.remove('hidden');
  }
  function showResult(success){
    document.querySelectorAll('.checker-step').forEach(el => el.classList.add('hidden'));
    document.getElementById(success ? 'result-success' : 'result-manual').classList.remove('hidden');
  }
  function resetChecker(){
    document.querySelectorAll('.checker-step').forEach(el => el.classList.add('hidden'));
    document.getElementById('step-1').classList.remove('hidden');
  }
</script>
"""

    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Checker HTML
    checker_pattern = re.compile(r'<div class="checker-box" id="checker-container">.*?</div>\s*</div>\s*</section>', re.DOTALL)
    content = checker_pattern.sub(new_checker_html.strip().replace('\\', '\\\\') + '\n  </div>\n</section>', content)

    # Replace Script
    script_pattern = re.compile(r'<script>.*?// Mobile menu toggle.*?</script>\s*</body>', re.DOTALL)
    content = script_pattern.sub(new_script_html.strip().replace('\\', '\\\\') + '\n</body>', content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_checker()
    print("index.html updated successfully!")
