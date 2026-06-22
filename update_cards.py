import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

# Card 1 replacement
old_card1_price = """<button onclick="document.getElementById('vg-price-modal').style.display='flex'" class="vg-btn" style="padding:10px 20px; font-size:13px; background-color:transparent !important; color:#8f55a0 !important; border:2px solid #8f55a0 !important; margin-bottom:15px; width:max-content; box-shadow:none !important; cursor:pointer;">Ver Rangos de Precios</button>"""
new_card1_price = """<button onclick="document.getElementById('vg-price-modal').style.display='flex'" style="background:none; border:none; padding:0; margin:0 0 25px 0; font-size:15px; color:#8f55a0; text-decoration:underline; font-weight:800; cursor:pointer; text-align:left;"><i class="fa fa-tag" style="margin-right:5px;"></i> Ver Rangos de Precios</button>"""

old_card1_cta = """<a href="https://neumovital.cl/reserva-funcion-pulmonar/" class="vg-card-link"><i class="fa fa-arrow-right"></i></a>"""
new_card1_cta = """<a href="https://neumovital.cl/reserva-funcion-pulmonar/" class="vg-btn" style="width:100%; text-align:center; padding:15px; font-size:15px; display:block; box-sizing:border-box;">Reservar Hora <i class="fa fa-arrow-right" style="margin-left:5px;"></i></a>"""

# Replace in text
text = text.replace(old_card1_price, new_card1_price)
text = text.replace(old_card1_cta, new_card1_cta)

# Card 2 CTA replacement (the price button is identical, so it's already replaced if AllowMultiple was implied, but string replace replaces all occurrences)
old_card2_cta = """<a href="https://neumovital.cl/reserva-rehabilitacion-pulmonar/" class="vg-card-link"><i class="fa fa-arrow-right"></i></a>"""
new_card2_cta = """<a href="https://neumovital.cl/reserva-rehabilitacion-pulmonar/" class="vg-btn" style="width:100%; text-align:center; padding:15px; font-size:15px; display:block; box-sizing:border-box;">Reservar Hora <i class="fa fa-arrow-right" style="margin-left:5px;"></i></a>"""
text = text.replace(old_card2_cta, new_card2_cta)

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Cards updated successfully!")
