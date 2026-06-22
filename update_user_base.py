import re

with open('user_base_code.txt', 'r') as f:
    v2 = f.read()

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    v1 = f.read()

# 1. CSS
v1_style = re.search(r'<style>(.*?)</style>', v1, flags=re.DOTALL).group(1)
v2_style_match = re.search(r'<style>(.*?)</style>', v2, flags=re.DOTALL)
new_v2_style = v2_style_match.group(1) + "\n/* --- IMPORTED FROM V1 --- */\n" + v1_style
v2 = v2.replace(v2_style_match.group(1), new_v2_style)

# 2. Pills Fonasa Isapre
v1_pills = '<div class="vg-glass-pills" style="margin-top:25px; margin-bottom:30px;"><span style="background:linear-gradient(135deg, #1d976c 0%, #93f9b9 100%); padding:8px 18px; border-radius:12px; color:#004d2a; font-weight:800; font-size:14px; box-shadow:0 10px 20px rgba(29, 151, 108, 0.3);"><i class="fa fa-check-circle" style="margin-right:5px;"></i> FONASA</span><span style="background:linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding:8px 18px; border-radius:12px; color:#003a66; font-weight:800; font-size:14px; box-shadow:0 10px 20px rgba(79, 172, 254, 0.3);"><i class="fa fa-check-circle" style="margin-right:5px;"></i> ISAPRE</span></div>'
v2_pills = re.search(r'<div class="vg-hero-pills".*?</div>', v2).group(0)
v2 = v2.replace(v2_pills, v1_pills)

# 3. Marquee (Patologías)
v1_marquee = re.search(r'<div class="vg-marquee-container">.*?</div>\s*</div>', v1, flags=re.DOTALL).group(0)
v2_trust = re.search(r'<section class="vg-trust-bar">.*?</section>', v2, flags=re.DOTALL).group(0)
v2 = v2.replace(v2_trust, v1_marquee)

# 4. Rangos de precios
price_btn = '<button onclick="document.getElementById(\'vg-price-modal\').style.display=\'flex\'" style="background:none; border:none; padding:0; margin:0 0 25px 0; font-size:15px; color:#8f55a0; text-decoration:underline; font-weight:800; cursor:pointer; text-align:left; display:block;"><i class="fa fa-tag" style="margin-right:5px;"></i> Ver Rangos de Precios</button>\n'
v2 = v2.replace('<a href="https://neumovital.cl/reserva-funcion-pulmonar/" class="vg-btn-outline">', price_btn + '<a href="https://neumovital.cl/reserva-funcion-pulmonar/" class="vg-btn-outline">')
v2 = v2.replace('<a href="https://neumovital.cl/reserva-rehabilitacion-pulmonar/" class="vg-btn-outline">', price_btn + '<a href="https://neumovital.cl/reserva-rehabilitacion-pulmonar/" class="vg-btn-outline">')

v1_modal = re.search(r'<div id="vg-price-modal".*?</div>\s*</div>\s*</div>\s*</div>', v1, flags=re.DOTALL).group(0)
# Append modal before <script> at the bottom
v2 = v2.replace('<script>', v1_modal + '\n<script>', 1) # Only first occurrence of <script> which is the audio script. Wait, there are two <script> tags.
# Better to append right before the first <script> tag
v2 = v2.replace('<script>var vgAudioPlaying', v1_modal + '\n<script>var vgAudioPlaying')

# 5, 6, 7. Founder, Testimonials, Alianzas, Footer
# In V1: Extract from <section class="vg-organic"> to <div id="vg-price-modal"
v1_tail = re.search(r'<section class="vg-organic">.*?(?=<div id="vg-price-modal")', v1, flags=re.DOTALL).group(0)

# In V2: We need to replace everything from <section class="vg-founder-editorial"> down to </section> before the <script>
# Let's use regex to find <section class="vg-founder-editorial"> to </section> of vg-footer-cta-bold
v2_tail_match = re.search(r'<section class="vg-founder-editorial">.*?</section>\s*</div>\s*<script>var vgAudioPlaying', v2, flags=re.DOTALL)
if v2_tail_match:
    v2 = v2.replace(v2_tail_match.group(0), v1_tail + '\n</div>\n<script>var vgAudioPlaying')
else:
    print("Could not find the tail in V2")

with open('propuestas/home/Propuesta-v2.txt', 'w') as f:
    f.write(v2)

print("Updates applied to the user's base code.")
