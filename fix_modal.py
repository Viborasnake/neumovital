import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

modal_html = """<div id="vg-price-modal" class="vg-modal-overlay" onclick="if(event.target === this) this.style.display='none';"><div class="vg-modal-box"><span class="vg-modal-close" onclick="document.getElementById('vg-price-modal').style.display='none'">&times;</span><h3 style="font-size:24px; font-weight:800; color:#111111 !important; margin-bottom:10px;"><i class="fa fa-tag" style="color:#46bfee; margin-right:10px;"></i> Valores Referenciales</h3><p style="font-size:15px; color:#666 !important; margin-bottom:20px; line-height:1.5;">Estos valores son orientativos y pueden variar según su sistema de salud (FONASA/ISAPRE).</p><table class="vg-price-table"><tr><th>Servicio</th><th>Rango Aprox.</th></tr><tr><td>Rehabilitación Pulmonar (Sesión)</td><td>$25.000 - $45.000</td></tr><tr><td>Espirometría Básica</td><td>$15.000 - $30.000</td></tr><tr><td>Estudio de Sueño (Poligrafía)</td><td>$80.000 - $120.000</td></tr><tr><td>Test de Marcha de 6 Minutos</td><td>$20.000 - $35.000</td></tr></table><div style="margin-top:25px; text-align:center;"><a href="https://wa.me/56951516662" class="vg-btn" style="padding:12px 25px; font-size:14px; width:100%; box-sizing:border-box;"><i class="fa fa-whatsapp"></i> Consultar mi valor exacto</a></div></div></div>"""

if '<div id="vg-price-modal"' not in text:
    text = text.replace('</div><script>', modal_html + '</div><script>')
    with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
        f.write(text)
    print("Modal HTML injected successfully.")
else:
    print("Modal already present.")
