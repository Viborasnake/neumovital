import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

# 1. Update the buttons
old_btn = '<a href="https://neumovital.cl/precios" class="vg-btn" style="padding:10px 20px; font-size:13px; background-color:transparent !important; color:#8f55a0 !important; border:2px solid #8f55a0 !important; margin-bottom:15px; width:max-content; box-shadow:none !important;">Ver Rangos de Precios</a>'
new_btn = '<button onclick="document.getElementById(\'vg-price-modal\').style.display=\'flex\'" class="vg-btn" style="padding:10px 20px; font-size:13px; background-color:transparent !important; color:#8f55a0 !important; border:2px solid #8f55a0 !important; margin-bottom:15px; width:max-content; box-shadow:none !important; cursor:pointer;">Ver Rangos de Precios</button>'

text = text.replace(old_btn, new_btn)

# 2. Add Modal CSS to the end of <style>
modal_css = """
/* --- POPUP MODAL --- */
.vg-modal-overlay { display: none; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.6); backdrop-filter: blur(5px); -webkit-backdrop-filter: blur(5px); z-index: 999999; align-items: center; justify-content: center; padding: 20px; }
.vg-modal-box { background: #fff; border-radius: 20px; padding: 40px; max-width: 500px; width: 100%; position: relative; box-shadow: 0 25px 50px rgba(0,0,0,0.2); animation: vgModalPop 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; text-align: left; }
.vg-modal-close { position: absolute; top: 15px; right: 20px; font-size: 28px; cursor: pointer; color: #999; transition: 0.3s; line-height: 1; }
.vg-modal-close:hover { color: #ff4757; }
@keyframes vgModalPop { 0% { transform: scale(0.8); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
.vg-price-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
.vg-price-table th, .vg-price-table td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #f0f0f0; }
.vg-price-table th { background: #f8fbfc; color: #8f55a0; font-weight: 800; text-transform: uppercase; font-size: 13px; }
.vg-price-table td { color: #555; font-size: 15px; }
"""
if "vg-modal-overlay" not in text:
    text = text.replace("</style>", minified_css := re.sub(r'\s+', ' ', modal_css).replace('} ', '}').replace(' {', '{').replace('; ', ';') + "</style>")

# 3. Add Modal HTML before the ending </div> of .vg-wrapper
# The ending is </div><script>
modal_html = """<div id="vg-price-modal" class="vg-modal-overlay" onclick="if(event.target === this) this.style.display='none';"><div class="vg-modal-box"><span class="vg-modal-close" onclick="document.getElementById('vg-price-modal').style.display='none'">&times;</span><h3 style="font-size:24px; font-weight:800; color:#111111 !important; margin-bottom:10px;"><i class="fa fa-tag" style="color:#46bfee; margin-right:10px;"></i> Valores Referenciales</h3><p style="font-size:15px; color:#666 !important; margin-bottom:20px; line-height:1.5;">Estos valores son orientativos y pueden variar según su sistema de salud (FONASA/ISAPRE).</p><table class="vg-price-table"><tr><th>Servicio</th><th>Rango Aprox.</th></tr><tr><td>Rehabilitación Pulmonar (Sesión)</td><td>$25.000 - $45.000</td></tr><tr><td>Espirometría Básica</td><td>$15.000 - $30.000</td></tr><tr><td>Estudio de Sueño (Poligrafía)</td><td>$80.000 - $120.000</td></tr><tr><td>Test de Marcha de 6 Minutos</td><td>$20.000 - $35.000</td></tr></table><div style="margin-top:25px; text-align:center;"><a href="https://wa.me/56951516662" class="vg-btn" style="padding:12px 25px; font-size:14px; width:100%; box-sizing:border-box;"><i class="fa fa-whatsapp"></i> Consultar mi valor exacto</a></div></div></div>"""
# Ensure it's totally minified
minified_html = re.sub(r'\n\s*', '', modal_html)

if "vg-price-modal" not in text:
    text = text.replace('</div><script>', minified_html + '</div><script>')

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Modal added successfully!")
