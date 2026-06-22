import re

with open('propuestas/home/Propuesta-v2.txt', 'r') as f:
    v2 = f.read()

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    v1 = f.read()

v1_tail = re.search(r'<section class="vg-organic">.*?(?=<div id="vg-price-modal")', v1, flags=re.DOTALL).group(0)

# Replace everything from <section class="vg-founder-editorial"> up to </div>\n<script>var vgAudioPlaying
# Using greedy .* instead of .*? to capture all the intermediate sections up to the closing div before the script.
v2_tail_match = re.search(r'<section class="vg-founder-editorial">.*</div>\s*(<script>var vgAudioPlaying)', v2, flags=re.DOTALL)

if v2_tail_match:
    # We replace everything from founder to the div, with v1_tail + </div>
    v2 = v2[:v2_tail_match.start()] + v1_tail + '\n</div>\n' + v2_tail_match.group(1) + v2[v2_tail_match.end():]
    print("Tail matched and replaced successfully.")
else:
    print("Still could not find tail.")

with open('propuestas/home/Propuesta-v2.txt', 'w') as f:
    f.write(v2)

