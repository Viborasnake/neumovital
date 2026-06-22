import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

text = text.replace('https://www.instagram.com/neumovital/', 'https://www.instagram.com/dani.neumovital/')

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("IG link updated globally.")
