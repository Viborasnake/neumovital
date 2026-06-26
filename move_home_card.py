import re

with open("dashboard_proyecto.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract the collapsible features grid
features_grid_match = re.search(r'(<button class="btn btn-outline" style="margin-bottom: 25px;.*?</div>)', html, re.DOTALL)
features_grid = features_grid_match.group(1) if features_grid_match else ""

# 2. Extract the V1.1 feedback block
feedback_match = re.search(r'(<div style="background: var\(--bg-page\); padding: 20px; border-radius: var\(--radius-md\); border: 1px dashed var\(--border\); margin-bottom: 30px;">.*?</div>)', html, re.DOTALL)
feedback = feedback_match.group(1) if feedback_match else ""

# 3. Extract the Action button
btn_match = re.search(r'(<div class="action-links">.*?</div>)', html, re.DOTALL)
btn = btn_match.group(1) if btn_match else ""

# 4. Remove the whole MAIN HOME CARD section
# From <!-- MAIN HOME CARD --> to just before <!-- ROADMAP VERTICAL -->
html = re.sub(r'<!-- MAIN HOME CARD -->.*?<!-- ROADMAP VERTICAL -->', '<!-- ROADMAP VERTICAL -->', html, flags=re.DOTALL)

# 5. Inject into ITEM 0 rm-body and rm-footer
item_0_pattern = r'(<!-- ITEM 0: Inicio -->.*?<div class="rm-body">\s*<p>.*?</span></p>\n)'
def insert_content(match):
    original_body_start = match.group(1)
    
    # We want to change the margin-bottom of the feedback block from 30px to 20px for better fit
    adjusted_feedback = feedback.replace('margin-bottom: 30px;', 'margin-bottom: 20px;')
    
    new_content = f"{original_body_start}\n{features_grid}\n\n{adjusted_feedback}\n"
    return new_content

html = re.sub(item_0_pattern, insert_content, html, flags=re.DOTALL)

# Modify the footer to include the button
footer_pattern = r'(<div class="rm-footer">)\s*(<span style="font-size: 13px; font-weight: 600; color: #d97706;"><i class="fa-solid fa-spinner fa-spin"></i> Pendiente de Aprobación</span>)\s*(</div>)'
def replace_footer(match):
    start = match.group(1)
    span = match.group(2)
    end = match.group(3)
    
    return f'<div class="rm-footer" style="display: flex; flex-direction: column; gap: 15px;">\n{btn}\n{span}\n</div>'

html = re.sub(footer_pattern, replace_footer, html, count=1, flags=re.DOTALL)

with open("dashboard_proyecto.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Card integrated into roadmap successfully.")
