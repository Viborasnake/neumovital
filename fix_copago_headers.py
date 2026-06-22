import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

text = text.replace('<i class="fa fa-heartbeat"></i> FONASA (Aprox)', '<i class="fa fa-heartbeat"></i> Copago FONASA')
text = text.replace('<i class="fa fa-shield"></i> ISAPRE (Aprox)', '<i class="fa fa-shield"></i> Copago ISAPRE')

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Headers updated to Copago.")
