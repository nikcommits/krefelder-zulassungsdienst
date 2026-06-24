import sys

file_path = '/Users/aziz/Dev/02_Kundenprojekte/Zulassungsdienst/auftrag.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

target_str = '<label class="af-check"'

new_sig_html = """        <div class="af-field" style="text-align:left; max-width:600px; margin:0 auto 24px">
          <label style="display:block; font-weight:700; margin-bottom:8px;">Ihre Unterschrift für die Vollmacht *</label>
          <button type="button" id="open-sig-btn" class="af-submit" style="background:var(--paper-3); color:var(--ink); font-weight:600; padding:12px; font-size:1rem; box-shadow:none; border:1px solid var(--hair-2); display:flex; align-items:center; justify-content:center; gap:8px;" onclick="openSignatureModal()">
            <svg viewBox="0 0 640 512" fill="currentColor" width="20" height="20"><path d="M623.2 192c-51.8 3.5-125.7 54.7-163.1 88.5-26.6 24-46.6 5.8-21.9-22.4 14.2-16.2 70.6-67.6 70.6-92.6 0-15.4-21-13.4-35.4-9.8-37.2 9.4-71.9 30.4-100.7 56.5-22.3 20.2-41.8 43.3-57.9 68.5-7.7 12-39.3 84.5-47.4 87.8-12.9 5.4-26.9-21.2-31.8-30.6-13.8-26.4-24.7-54.5-34.7-82.5-23.9 23.9-46.6 33.5-72.5 14.8C29.1 348.4 0 401.4 0 401.4s30.7 21.3 49.4 6.9c20.3-15.6 34-39.5 48.5-59.8 8.8 22.9 33.6 92.6 70.7 86.3 36-6.1 65.2-95.6 78.6-126.5 19.2-44.4 56.7-99.1 105.8-114.2 0 22.7-49.6 70.9-65 86.4-21.1 21.2-13.3 51.5 15.3 49.7 32.1-2 116.6-77.3 156.3-82.4 16.7-2.2 24-15.2 24-31.1 0-26.4-87.5-26.4-104-15z"/></svg>
            Hier digital unterschreiben
          </button>
          <div id="sig-preview-wrap" style="display:none; text-align:center; margin-top:12px; border:1px solid #16a34a; border-radius:8px; padding:12px; background:#f0fdf4;">
            <img id="sig-preview-img" src="" alt="Ihre Unterschrift" style="max-height:80px; mix-blend-mode:multiply;">
          </div>
        </div>

"""

if 'id="open-sig-btn"' not in html:
    idx = html.find(target_str)
    if idx != -1:
        newline_idx = html.rfind('\\n', 0, idx)
        if newline_idx != -1:
            html = html[:newline_idx+1] + new_sig_html + html[newline_idx+1:]
        else:
            html = html[:idx] + new_sig_html + html[idx:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Signature block added successfully.")
    else:
        print("Could not find target_str")
else:
    print("Button already exists.")
