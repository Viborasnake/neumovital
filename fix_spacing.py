with open('propuestas/home/Propuesta-v2.txt', 'r') as f:
    text = f.read()

# The exact injected block started with:
# <div class="vg-pathologies" style="text-align:center; margin-bottom:60px;">
# Let's replace it to include margin-top: 80px;

old_html = '<div class="vg-pathologies" style="text-align:center; margin-bottom:60px;">'
new_html = '<div class="vg-pathologies" style="text-align:center; margin-top:80px; margin-bottom:60px;">'

text = text.replace(old_html, new_html)

with open('propuestas/home/Propuesta-v2.txt', 'w') as f:
    f.write(text)

