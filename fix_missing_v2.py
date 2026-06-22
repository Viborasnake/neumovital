import re

with open('propuestas/home/Propuesta-v2.txt', 'r') as f:
    v2 = f.read()

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    v1 = f.read()

# 1. Price Modal
v1_modal = re.search(r'<div id="vg-price-modal".*?</div>\s*</div>\s*</div>\s*</div>', v1, flags=re.DOTALL)
if v1_modal:
    modal_html = v1_modal.group(0)
    # Check if it's already there to avoid duplicates
    if 'id="vg-price-modal"' not in v2:
        v2 = v2.replace('<script>var vgAudioPlaying', modal_html + '\n<script>var vgAudioPlaying')
        print("Injected price modal.")

# 2. Pills Patologias
v1_pathologies = re.search(r'<div class="vg-pathologies".*?</div>\s*</div>', v1, flags=re.DOTALL)
if v1_pathologies:
    pathologies_html = v1_pathologies.group(0)
    if 'Patologías que Atendemos' not in v2:
        # Inject right before the zigzag services section
        v2 = v2.replace('<section class="vg-zigzag-section" id="servicios">', pathologies_html + '\n<section class="vg-zigzag-section" id="servicios">')
        print("Injected pills patologias.")

with open('propuestas/home/Propuesta-v2.txt', 'w') as f:
    f.write(v2)

