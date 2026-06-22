with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

# I will find the carousel CSS and HTML and strip their newlines
import re

# 1. Strip newlines from the CSS part
# The CSS I added starts at /* --- TESTIMONIALS CAROUSEL --- */ and ends at </style>
css_pattern = r'(/\* --- TESTIMONIALS CAROUSEL --- \*/.*?</style>)'
css_match = re.search(css_pattern, text, re.DOTALL)
if css_match:
    css_block = css_match.group(1)
    # Remove all newlines and excess spaces
    minified_css = re.sub(r'\s+', ' ', css_block).replace('} ', '}').replace(' {', '{').replace('; ', ';')
    text = text.replace(css_block, minified_css)

# 2. Strip newlines from the HTML part
html_pattern = r'(<section class="vg-testimonials".*?</section>)'
html_match = re.search(html_pattern, text, re.DOTALL)
if html_match:
    html_block = html_match.group(1)
    minified_html = re.sub(r'\n\s*', '', html_block)
    text = text.replace(html_block, minified_html)

# Also ensure no newlines in the doctors banner that I added before
docs_pattern = r'(<section class="vg-doctors-banner".*?</section>)'
docs_match = re.search(docs_pattern, text, re.DOTALL)
if docs_match:
    docs_block = docs_match.group(1)
    minified_docs = re.sub(r'\n\s*', '', docs_block)
    text = text.replace(docs_block, minified_docs)
    
# And the pathologies I added before
path_pattern = r'(<div class="vg-pathologies".*?</div>\s*</div>)'
path_match = re.search(path_pattern, text, re.DOTALL)
if path_match:
    path_block = path_match.group(1)
    minified_path = re.sub(r'\n\s*', '', path_block)
    text = text.replace(path_block, minified_path)

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Minified successfully!")
