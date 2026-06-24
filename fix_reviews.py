import os

with open('index.html', 'r') as f:
    content = f.read()

# Replace quotes grid
old_grid_start = '<div class="quotes-grid">'
old_grid_end = '</div>\n    \n    <div style="text-align:center; margin-top:32px; margin-bottom:16px;">'

start_idx = content.find(old_grid_start)
end_idx = content.find(old_grid_end)

if start_idx != -1 and end_idx != -1:
    new_reviews = """<div class="quotes-grid">
      <div class="quote-card">
        <div class="stars">
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
        </div>
        <p>„Ich bin rundum zufrieden! Der Service war außergewöhnlich zuvorkommend und sehr hilfsbereit. Alle Probleme wurden sofort geklärt, sodass ich mir wirklich keine Sorgen machen musste. Man war stets erreichbar, und die gesamte Zulassung wurde für mich deutlich vereinfacht. Absolute Empfehlung!"</p>
        <div class="who"><div class="av" style="background:var(--orange)">MA</div><div><div class="nm">Maleika Azam</div><div class="src">Google Bewertung · vor 6 Monaten</div></div></div>
      </div>
      <div class="quote-card">
        <div class="stars">
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
        </div>
        <p>„Meine Versicherung hat mir den Zulassungsdienst empfohlen und ich bin mehr als begeistert. Alles reibungslos verlaufen und nur zu empfehlen. Ich wünsche ein schönes Silvester und einen guten Rutsch ins neue Jahr 2026"</p>
        <div class="who"><div class="av" style="background:var(--orange)">NK</div><div><div class="nm">Nadine Kraus</div><div class="src">Google Bewertung · vor 5 Monaten</div></div></div>
      </div>
      <div class="quote-card">
        <div class="stars">
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
          <svg viewBox="0 0 576 512" fill="currentColor"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L447.7 329.9l25.4 155.4c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7L287.9 437.4 137.6 510c-8 4.3-17.8 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l25.4-155.4L17.8 218.6c-6.4-6.4-8.7-15.9-5.9-24.5s10.3-15 19.3-16.3l153.2-22.6L246.3 13.5C250.3 5.2 258.7 0 287.9 0z"/></svg>
        </div>
        <p>„Ich bin total begeistert von diesem Service. Obwohl der Chef selbst eine Autopanne und dadurch einen sehr sehr stressigen Tag hatte, kam er noch abends um 22 Uhr, um die benötigten Unterlagen abzuholen. Am nächsten Abend hat er mir alles komplett erledigt zurück gebracht. Ich empfehle dieses Unternehmen zu 💯%...immer wieder gerne."</p>
        <div class="who"><div class="av" style="background:var(--orange)">CL</div><div><div class="nm">Carolin Lentzen</div><div class="src">Google Bewertung · vor 6 Monaten</div></div></div>
      </div>
"""
    content = content[:start_idx] + new_reviews + content[end_idx:]

with open('index.html', 'w') as f:
    f.write(content)

print("Done reviews.")
