import re

def modify_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Elements to animate:
    # 1. .services-grid .item -> aos-fade-up
    content = re.sub(r'class="item"', r'class="item aos aos-fade-up"', content)
    # 2. .step -> aos-fade-up
    content = re.sub(r'class="step"', r'class="step aos aos-fade-up"', content)
    # 3. .price-card -> aos-fade-up
    content = re.sub(r'class="price-card"', r'class="price-card aos aos-fade-up"', content)
    # 4. .trust-card -> aos-fade-up
    content = re.sub(r'class="trust-card"', r'class="trust-card aos aos-fade-up"', content)
    # 5. .checker-box -> aos-fade-up
    content = re.sub(r'class="checker-box"', r'class="checker-box aos aos-fade-up"', content)
    # 6. .quote-card -> aos-fade-up
    content = re.sub(r'class="quote-card"', r'class="quote-card aos aos-fade-up"', content)
    # 7. .social-card -> aos-fade-up
    content = re.sub(r'class="social-card"', r'class="social-card aos aos-fade-up"', content)
    # 8. .review-hero -> aos-fade-up
    content = re.sub(r'class="review-hero"', r'class="review-hero aos aos-fade-up"', content)

    # Add the observer script right before </body>
    if 'IntersectionObserver' not in content:
        script = """
<!-- Animations Script -->
<script>
document.addEventListener("DOMContentLoaded", function() {
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        // Add a slight delay based on index if we want staggering, but IntersectionObserver 
        // doesn't inherently group them unless we do it manually. For simplicity, just add class.
        // We can do a small delay for staggered effect if multiple are intersecting at once:
        setTimeout(() => {
          entry.target.classList.add('is-visible');
        }, (index * 100)); // 100ms stagger
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.aos').forEach((el) => {
    observer.observe(el);
  });
});
</script>
</body>
"""
        content = content.replace('</body>', script)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

def modify_css():
    with open('styles/system.css', 'a', encoding='utf-8') as f:
        css = """

/* ════════ ANIMATIONS ON SCROLL ════════ */
.aos {
  opacity: 0;
  transition-property: opacity, transform;
  transition-duration: 0.6s;
  transition-timing-function: cubic-bezier(0.25, 0.8, 0.25, 1);
  will-change: opacity, transform;
}

/* Mobile first: smaller translate values */
.aos-fade-up {
  transform: translateY(30px);
}

.aos.is-visible {
  opacity: 1;
  transform: translateY(0) translateX(0) scale(1);
}

/* Optional: Adding delays for elements inside a container isn't easy without structural knowledge,
   but we stagger them via JS instead (see index.html script). */

@media (min-width: 768px) {
  .aos-fade-up {
    transform: translateY(50px);
  }
}
"""
        f.write(css)

if __name__ == "__main__":
    modify_html()
    modify_css()
    print("Animations added successfully!")
