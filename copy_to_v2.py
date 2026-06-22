import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    v1 = f.read()

with open('propuestas/home/Propuesta-v2.txt', 'r') as f:
    v2 = f.read()

# 1. CSS
# Extract all CSS from V1 (everything between <style> and </style>)
v1_style = re.search(r'<style>(.*?)</style>', v1, flags=re.DOTALL).group(1)

# In V2, we will keep V2's CSS and append V1's CSS so we have all classes available.
# Wait, V1's body/global styles might break V2's hero. Let's just extract the specific CSS we need, 
# or just append V1's CSS at the bottom of V2's CSS.
# Let's extract specific CSS blocks from V1 using regex or just string splitting.
# Instead of doing that, I'll extract the HTML blocks from V1 and inject them into V2. 
# And for CSS, I will append the ENTIRE V1 style block just before </style> in V2. 
# V2's classes are prefixed with vg-split-, vg-zigzag-, vg-trust-, vg-founder-, etc.
# V1 has vg-hero, vg-services, vg-organic. So they won't conflict much.
# Wait, V1 has .vg-wrapper and .vg-btn. V2 has .vg-btn-primary and .vg-btn-outline. No conflict!

v2_style_match = re.search(r'<style>(.*?)</style>', v2, flags=re.DOTALL)
if v2_style_match:
    v2_style_inner = v2_style_match.group(1)
    new_v2_style = v2_style_inner + "\n/* --- IMPORTED FROM V1 --- */\n" + v1_style
    v2 = v2.replace(v2_style_inner, new_v2_style)


# 2. PILLS FONASA ISAPRE
# In V1: <div class="vg-glass-pills">...</div>
# In V2: We need to put this inside the hero, before the buttons.
pills_html = '<div class="vg-glass-pills" style="margin-bottom:30px;"><span style="background:linear-gradient(135deg, #1d976c 0%, #93f9b9 100%); padding:8px 18px; border-radius:12px; color:#004d2a; font-weight:800; font-size:14px; box-shadow:0 10px 20px rgba(29, 151, 108, 0.3);"><i class="fa fa-check-circle" style="margin-right:5px;"></i> FONASA</span><span style="background:linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding:8px 18px; border-radius:12px; color:#003a66; font-weight:800; font-size:14px; box-shadow:0 10px 20px rgba(79, 172, 254, 0.3);"><i class="fa fa-check-circle" style="margin-right:5px;"></i> ISAPRE</span></div>'
if '<div class="vg-hero-actions">' in v2:
    v2 = v2.replace('<div class="vg-hero-actions">', pills_html + '\n<div class="vg-hero-actions">')

# 3. PILLS PATOLOGIAS QUE ATENDEMOS (Marquee)
# V1 HTML: <div class="vg-marquee-container">...</div>
# V2: Replace <div class="vg-trust-bar">...</div>
v1_marquee = re.search(r'<div class="vg-marquee-container">.*?</div>\s*</div>', v1, flags=re.DOTALL).group(0)
v2_trust_bar = re.search(r'<div class="vg-trust-bar">.*?</div>\s*</div>', v2, flags=re.DOTALL).group(0)
v2 = v2.replace(v2_trust_bar, v1_marquee)

# 4. RANGOS DE PRECIOS
# In V1, it's the modal at the bottom, and buttons on cards.
# First, extract modal from V1
v1_modal = re.search(r'<div id="vg-price-modal".*?</div>\s*</div>\s*</div>\s*</div>', v1, flags=re.DOTALL).group(0)
# Append modal to the very end of V2, before the <script>
v2 = v2.replace('<script>', v1_modal + '\n<script>')

# Add the "Ver Rangos de Precios" button to V2's zig-zag sections.
# V2 has <a href="#" class="vg-btn-outline">Ver Exámenes</a> etc. We will add the price button right above it.
price_btn = '<button onclick="document.getElementById(\'vg-price-modal\').style.display=\'flex\'" style="background:none; border:none; padding:0; margin:0 0 25px 0; font-size:15px; color:#8f55a0; text-decoration:underline; font-weight:800; cursor:pointer; text-align:left; display:block;"><i class="fa fa-tag" style="margin-right:5px;"></i> Ver Rangos de Precios</button>'
v2 = v2.replace('<a href="#" class="vg-btn-outline">', price_btn + '\n<a href="#" class="vg-btn-outline">')

# 5 & 6 & 7. Potenciar Fundadora, Testimonials, Alianzas, Footer
# In V1, these are the sections: .vg-organic, .vg-testimonials, .vg-doctors-banner, .vg-instagram, .vg-footer-cta
# We will extract ALL of this from V1 starting from <section class="vg-organic"> up to the modal.
v1_tail = re.search(r'<section class="vg-organic">.*?(?=<div id="vg-price-modal")', v1, flags=re.DOTALL).group(0)

# In V2, we will delete from <section class="vg-founder-editorial"> down to </section> before the <script> (which is the footer-cta-bold)
# Basically, replace everything after </section> of zigzag with v1_tail
# The zigzag ends with </div>\n</div>\n</section>
v2_tail_match = re.search(r'(</section>\s*)<section class="vg-founder-editorial">.*?(?=<script>)', v2, flags=re.DOTALL)
if v2_tail_match:
    v2 = v2.replace(v2_tail_match.group(0), v2_tail_match.group(1) + v1_tail)

with open('propuestas/home/Propuesta-v2.txt', 'w') as f:
    f.write(v2)

print("V2 updated with V1 components successfully.")
