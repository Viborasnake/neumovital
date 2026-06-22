import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

# 1. INJECT MODAL HTML (if not there)
modal_html = """<div id="vg-price-modal" class="vg-modal-overlay" onclick="if(event.target === this) this.style.display='none';"><div class="vg-modal-box"><span class="vg-modal-close" onclick="document.getElementById('vg-price-modal').style.display='none'">&times;</span><h3 style="font-size:24px; font-weight:800; color:#111111 !important; margin-bottom:10px;"><i class="fa fa-tag" style="color:#46bfee; margin-right:10px;"></i> Valores Referenciales</h3><p style="font-size:15px; color:#666 !important; margin-bottom:20px; line-height:1.5;">Estos valores son orientativos y pueden variar según su sistema de salud (FONASA/ISAPRE).</p><table class="vg-price-table"><tr><th>Servicio</th><th>Rango Aprox.</th></tr><tr><td>Rehabilitación Pulmonar (Sesión)</td><td>$25.000 - $45.000</td></tr><tr><td>Espirometría Básica</td><td>$15.000 - $30.000</td></tr><tr><td>Estudio de Sueño (Poligrafía)</td><td>$80.000 - $120.000</td></tr><tr><td>Test de Marcha de 6 Minutos</td><td>$20.000 - $35.000</td></tr></table><div style="margin-top:25px; text-align:center;"><a href="https://wa.me/56951516662" class="vg-btn" style="padding:12px 25px; font-size:14px; width:100%; box-sizing:border-box;"><i class="fa fa-whatsapp"></i> Consultar mi valor exacto</a></div></div></div>"""

if "vg-price-modal" not in text:
    text = text.replace('</div><script>', modal_html + '</div><script>')
    print("Modal injected.")
else:
    print("Modal already present.")

# 2. FIX CAROUSEL SCROLL CSS
# Current CSS: .vg-testim-carousel{ max-width: 1200px;margin: 0 auto;overflow-x: auto;scroll-snap-type: x mandatory;scroll-behavior: smooth;-webkit-overflow-scrolling: touch;padding-bottom: 20px;}
# Current Track: .vg-testim-track{ display: flex; flex-wrap: nowrap; gap: 30px; width: max-content; padding: 20px 10px; }

new_carousel_css = ".vg-testim-carousel{max-width:1200px;margin:0 auto;padding-bottom:20px;position:relative;}"
new_track_css = ".vg-testim-track{display:flex;flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch;scroll-snap-type:x mandatory;scroll-behavior:smooth;gap:30px;padding:20px 10px;width:100%;box-sizing:border-box;}"

# I will use regex to replace the old css since it might have spaces
text = re.sub(r'\.vg-testim-carousel\s*\{[^}]*\}', new_carousel_css, text)
text = re.sub(r'\.vg-testim-track\s*\{[^}]*\}', new_track_css, text)

# Also ensure scrollbars are applied to the track, not the carousel
text = text.replace('.vg-testim-carousel::-webkit-scrollbar', '.vg-testim-track::-webkit-scrollbar')

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Fixes applied.")
