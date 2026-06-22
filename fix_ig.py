import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

old_social = '<div class="vg-social-icons"><a href="https://www.linkedin.com/" target="_blank" title="Perfil de LinkedIn"><i class="fa fa-linkedin"></i></a></div>'
new_social = '<div class="vg-social-icons"><a href="https://www.instagram.com/neumovital/" target="_blank" title="Instagram Neumovital"><i class="fa fa-instagram"></i></a></div>'

text = text.replace(old_social, new_social)

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("IG swapped.")
