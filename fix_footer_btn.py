import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

old_footer_cta = '<a href="https://wa.me/56951516662" class="vg-btn-whatsapp"><i class="fa fa-whatsapp"></i> RESERVAR HORA</a><p class="vg-whatsapp-text">WhatsApp Directo:+569 5151 6662</p>'
new_footer_cta = '<a href="https://neumovital.cl/appointment-booking/" class="vg-btn" style="padding:18px 50px; font-size:18px;">RESERVAR HORA <i class="fa fa-calendar-check-o" style="margin-left:10px;"></i></a><p class="vg-whatsapp-text" style="margin-top:20px; font-size:15px;"><i class="fa fa-whatsapp"></i> ¿Dudas? Escríbenos al <a href="https://wa.me/56951516662" style="color:#ffffff; text-decoration:underline;">+569 5151 6662</a></p>'

text = text.replace(old_footer_cta, new_footer_cta)

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Footer CTA updated.")
