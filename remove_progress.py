import re

with open('dashboard_proyecto.html', 'r') as f:
    html = f.read()

# The block to remove is:
#                         <div class="progress-group">
#                             <div class="progress-text"><span>Progreso</span><span>0%</span></div>
#                             <div class="progress-track"><div class="progress-fill"></div></div>
#                         </div>

# We can use a regex that matches this exact block
html = re.sub(
    r'\s*<div class="progress-group">\s*<div class="progress-text"><span>Progreso</span><span>0%</span></div>\s*<div class="progress-track"><div class="progress-fill"></div></div>\s*</div>',
    '',
    html
)

# And also clean up the CSS related to it if we want, but it's not strictly necessary. Let's just remove the HTML blocks.

with open('dashboard_proyecto.html', 'w') as f:
    f.write(html)

print("Removed progress groups from HTML")
