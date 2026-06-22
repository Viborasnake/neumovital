import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

old_table = '<table class="vg-price-table"><tr><th>Servicio</th><th>Rango Aprox.</th></tr><tr><td>Rehabilitación Pulmonar (Sesión)</td><td>$25.000 - $45.000</td></tr><tr><td>Espirometría Básica</td><td>$15.000 - $30.000</td></tr><tr><td>Estudio de Sueño (Poligrafía)</td><td>$80.000 - $120.000</td></tr><tr><td>Test de Marcha de 6 Minutos</td><td>$20.000 - $35.000</td></tr></table>'

new_table = '<div style="overflow-x:auto;"><table class="vg-price-table" style="width:100%; text-align:left; border-collapse:collapse; font-size:14px; margin-bottom:10px;"><tr style="background:#f4f7fb; border-bottom:2px solid #dce4ec;"><th style="padding:12px 10px; color:#111;">Servicio</th><th style="padding:12px 10px; color:#1d976c;"><i class="fa fa-heartbeat"></i> FONASA (Aprox)</th><th style="padding:12px 10px; color:#4facfe;"><i class="fa fa-shield"></i> ISAPRE (Aprox)</th></tr><tr style="border-bottom:1px solid #eee;"><td style="padding:12px 10px; font-weight:600;">Rehabilitación Pulmonar (Sesión)</td><td style="padding:12px 10px;">$12.000 - $18.000</td><td style="padding:12px 10px;">$8.000 - $25.000</td></tr><tr style="border-bottom:1px solid #eee;"><td style="padding:12px 10px; font-weight:600;">Espirometría Básica</td><td style="padding:12px 10px;">$8.000 - $15.000</td><td style="padding:12px 10px;">$5.000 - $18.000</td></tr><tr style="border-bottom:1px solid #eee;"><td style="padding:12px 10px; font-weight:600;">Estudio de Sueño</td><td style="padding:12px 10px;">$45.000 - $65.000</td><td style="padding:12px 10px;">$25.000 - $70.000</td></tr><tr><td style="padding:12px 10px; font-weight:600;">Test de Marcha (6 Min)</td><td style="padding:12px 10px;">$10.000 - $18.000</td><td style="padding:12px 10px;">$6.000 - $20.000</td></tr></table></div><p style="font-size:12px; color:#888; text-align:center; font-style:italic;">* Valores de copago meramente referenciales. Dependen del tramo Fonasa o plan Isapre.</p>'

text = text.replace(old_table, new_table)

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Prices updated.")
