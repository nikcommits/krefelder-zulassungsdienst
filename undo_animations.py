import re

def undo_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove classes
    content = content.replace('class="item aos aos-fade-up"', 'class="item"')
    content = content.replace('class="step aos aos-fade-up"', 'class="step"')
    content = content.replace('class="price-card aos aos-fade-up"', 'class="price-card"')
    content = content.replace('class="trust-card aos aos-fade-up"', 'class="trust-card"')
    content = content.replace('class="checker-box aos aos-fade-up"', 'class="checker-box"')
    content = content.replace('class="quote-card aos aos-fade-up"', 'class="quote-card"')
    content = content.replace('class="social-card aos aos-fade-up"', 'class="social-card"')
    content = content.replace('class="review-hero aos aos-fade-up"', 'class="review-hero"')

    # 2. Remove script
    script_pattern = re.compile(r'<!-- Animations Script -->\s*<script>.*?</script>\s*</body>', re.DOTALL)
    content = script_pattern.sub('</body>', content)
    
    # 3. Remove v=2 from logo
    content = content.replace('assets/images/Kennwerk-Logo.png?v=2', 'assets/images/Kennwerk-Logo.png')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

def undo_css():
    with open('styles/system.css', 'r', encoding='utf-8') as f:
        content = f.read()
    
    css_pattern = re.compile(r'/\* ════════ ANIMATIONS ON SCROLL ════════ \*/.*', re.DOTALL)
    content = css_pattern.sub('', content)
    
    with open('styles/system.css', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    undo_html()
    undo_css()
    print("Animations reverted.")
