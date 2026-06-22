import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

old_css = '.vg-hero-quote{justify-content:center;}'
new_css = '.vg-hero-quote{flex-direction:column;justify-content:center;align-items:center;}.vg-quote-avatar{width:140px;height:140px;margin-right:0 !important;margin-bottom:20px;}'

text = text.replace(old_css, new_css)

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Responsive CSS updated.")
