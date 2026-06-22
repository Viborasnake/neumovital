import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

# 1. ADD SHINE EFFECT TO HERO GLASS BOX
old_glass_box = '<div class="vg-glass-box">'
shine_div = '<div style="position:absolute; top:0; left:-100%; width:50%; height:100%; background:linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent); transform:skewX(-20deg); animation:shineBox 8s infinite; pointer-events:none; z-index:0;"></div>'
# We also need to ensure the text and buttons inside stay above the shine, so we wrap the content or rely on z-index.
# The shine div has z-index:0. The other elements should naturally sit above it if they are block elements, but just in case, we can add it safely.
# Also ensure vg-glass-box has overflow:hidden.
# Let's check if vg-glass-box is defined in css. If so, adding overflow:hidden to the class is safer.
css_glass_box_match = re.search(r'\.vg-glass-box\s*\{([^}]+)\}', text)
if css_glass_box_match:
    old_css = css_glass_box_match.group(0)
    if 'overflow: hidden' not in old_css and 'overflow:hidden' not in old_css:
        new_css = old_css.replace('{', '{overflow: hidden; ')
        text = text.replace(old_css, new_css)

new_glass_box = old_glass_box + shine_div
text = text.replace(old_glass_box, new_glass_box)

# 2. CHANGE "RESERVA AHORA" to "RESERVAR HORA" in the footer
text = text.replace('<a href="https://wa.me/56951516662" class="vg-btn-whatsapp"><i class="fa fa-whatsapp"></i> RESERVA AHORA</a>', '<a href="https://wa.me/56951516662" class="vg-btn-whatsapp"><i class="fa fa-whatsapp"></i> RESERVAR HORA</a>')

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Updates applied.")
