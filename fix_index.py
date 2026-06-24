import os, re

filepath = 'index.html'
with open(filepath, 'r') as f:
    content = f.read()

# 1. Logo
logo_old = """      <a href="#" class="logo" aria-label="Krefelder Zulassungsdienst Startseite">
        <div class="badge">D</div>
        <div>
          <div class="top"><span class="pill">24/7</span> Abhol &amp; Bring Service</div>
          <div class="name"><span class="text-red">Krefelder</span> <span>Zulassungsdienst</span></div>
        </div>
      </a>"""
logo_new = """      <a href="#" class="logo" aria-label="Zulassungsdienst Ostwall Startseite">
        <div class="logo-top-text">ZULASSUNGSDIENST</div>
        <div class="logo-plate">
          <div class="logo-plate-blue">
            <svg viewBox="0 0 100 100" class="logo-eu-stars">
              <g fill="#ffcc00">
                <circle cx="50" cy="15" r="5"/><circle cx="67.5" cy="19.7" r="5"/><circle cx="80.3" cy="32.5" r="5"/><circle cx="85" cy="50" r="5"/><circle cx="80.3" cy="67.5" r="5"/><circle cx="67.5" cy="80.3" r="5"/><circle cx="50" cy="85" r="5"/><circle cx="32.5" cy="80.3" r="5"/><circle cx="19.7" cy="67.5" r="5"/><circle cx="15" cy="50" r="5"/><circle cx="19.7" cy="32.5" r="5"/><circle cx="32.5" cy="19.7" r="5"/>
              </g>
            </svg>
            <span class="logo-d">D</span>
          </div>
          <div class="logo-plate-text">OSTWALL</div>
        </div>
      </a>"""
content = content.replace(logo_old, logo_new)

# 2. Colors
content = content.replace('--red', '--orange')
content = content.replace('text-red', 'text-orange')
content = content.replace('btn-red', 'btn-orange')
content = content.replace('glow-red', 'glow-orange')
content = content.replace('ico-red', 'ico-orange')

# 3. Phones
content = content.replace('015204638064', '01732803507')
content = content.replace('4915204638064', '491732803507')
content = content.replace('0152 046 380 64', '0173 280 3507')

# 4. Reviews
new_reviews = """    <div class="quotes-grid">
      <div class="quote-card">
        <div class="stars">
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
        </div>
        <p>„Ich bin mit dem Service absolut zufrieden. Leider gab es seitens der Stadt Probleme... Aber es wurde mehrmals probiert und am nächsten Tag wurde auch extra beim Straßenverkehrsamt nach dem Grund gefragt. Also 1A Service und es wird sich wirklich Mühe gegeben. Absolute Empfehlung."</p>
        <div class="who"><div class="av" style="background:var(--orange)">OS</div><div><div class="nm">Oliver Strobel</div><div class="src">Google Local Guide · vor 8 Monaten</div></div></div>
      </div>
      <div class="quote-card">
        <div class="stars">
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
        </div>
        <p>„Ich kann sie wärmstens empfehlen. Meine Fahrzeugzulassung war in weniger als 24 Stunden erledigt. Ein freundliches und hilfsbereites Team..."</p>
        <div class="who"><div class="av" style="background:var(--orange)">MŞ</div><div><div class="nm">murat şentürk</div><div class="src">Google Local Guide · vor 3 Monaten</div></div></div>
      </div>
      <div class="quote-card">
        <div class="stars">
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
        </div>
        <p>„Klasse Service! Kam hier mit meinen Unterlagen hin und habe die abgegeben. Die Sofort-Zulassung hat super geklappt."</p>
        <div class="who"><div class="av" style="background:var(--orange)">DL</div><div><div class="nm">Douti Lamboni</div><div class="src">Google Bewertung · vor 7 Monaten</div></div></div>
      </div>
      <div class="quote-card">
        <div class="stars">
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
        </div>
        <p>„Ich bin absolut begeistert vom Zulassungsdienst! Der Service war top, super freundlich und vor allem extrem schnell – so unkompliziert habe ich eine Kfz-Zulassung noch nie erlebt. Alles wurde professionell erledigt."</p>
        <div class="who"><div class="av" style="background:var(--orange)">TW</div><div><div class="nm">Till Wirbelauer</div><div class="src">Google Bewertung · vor 10 Monaten</div></div></div>
      </div>
      <div class="quote-card">
        <div class="stars">
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
        </div>
        <p>„Sehr frundlich sehr schnel auch die einwohner parkschein mitt erledigen einfach Respekt. Danke nochmal für alles. Gerne wider"</p>
        <div class="who"><div class="av" style="background:var(--orange)">RK</div><div><div class="nm">Remzi Keser</div><div class="src">Google Bewertung · vor 6 Monaten</div></div></div>
      </div>
      <div class="quote-card">
        <div class="stars">
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
        </div>
        <p>„Immer sehr hilfsbereit. Kann ich nur empfehlen. Top service!"</p>
        <div class="who"><div class="av" style="background:var(--orange)">GN</div><div><div class="nm">Gh Nju</div><div class="src">Google Bewertung · vor 3 Monaten</div></div></div>
      </div>
    </div>
    
    <div style="text-align:center; margin-top:32px; margin-bottom:16px;">
      <a href="https://share.google/nexC2D69iQ7lRoy7I" target="_blank" rel="noopener" class="btn btn-orange glow">
        Schauen Sie sich unsere weiteren Bewertungen an oder hinterlassen Sie eine Bewertung
      </a>
    </div>"""

pattern = r'<div class="quotes-grid">.*?</div>\s*</div>\s*<div class="social-grid">'
content = re.sub(pattern, new_reviews + '\n\n    <div class="social-grid">', content, flags=re.DOTALL)

with open(filepath, 'w') as f:
    f.write(content)
