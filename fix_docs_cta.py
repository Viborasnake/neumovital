import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

old_paragraph = '<p style="font-size:19px; color:#d0d0d0 !important; line-height:1.7; margin-bottom:0; font-weight:300;">Somos el centro solucionador aliado para <strong style="color:#fff; font-weight:600;">Broncopulmonares, Geriatras e Internistas</strong>. Aseguramos continuidad en la atención y resultados confiables para tus pacientes.</p>'

new_content = old_paragraph + '<a href="#" class="vg-btn" style="margin-top:30px; display:inline-flex; align-items:center; padding:15px 35px; font-size:16px;">Reserva ahora <i class="fa fa-arrow-right" style="margin-left:10px;"></i></a>'

text = text.replace(old_paragraph, new_content)

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("CTA injected.")
