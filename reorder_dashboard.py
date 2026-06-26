import re

with open("dashboard_proyecto.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Inject CSS
css_to_add = """
        .dashboard-layout {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 40px;
            align-items: start;
        }

        @media(max-width: 1024px) {
            .dashboard-layout {
                grid-template-columns: 1fr;
            }
        }
"""
html = html.replace("    </style>", css_to_add + "    </style>")

# 2. Extract sections
# They are delimited by HTML comments
def extract_section(start_comment, end_comment=None):
    if end_comment:
        pattern = f"({start_comment}.*?)(?={end_comment})"
    else:
        # up to closing container
        pattern = f"({start_comment}.*?)(?=</div>\n\n</body>)"
    
    match = re.search(pattern, html, re.DOTALL)
    if match:
        content = match.group(1)
        return content
    return ""

docs = extract_section(r"<!-- DOCS & EXTRA SECTION -->", r"<!-- BENTO GRID: ESTRATEGIA -->")
estrategia = extract_section(r"<!-- BENTO GRID: ESTRATEGIA -->", r"<!-- MAIN HOME CARD -->")
entregables = extract_section(r"<!-- MAIN HOME CARD -->", r"<!-- ROADMAP VERTICAL -->")
roadmap = extract_section(r"<!-- ROADMAP VERTICAL -->")

# 3. Build new body
header_pattern = r"(</header>\n)"
header_match = re.search(header_pattern, html)
header_end = header_match.end()

new_layout = f"""
    <div class="dashboard-layout">
        <div class="layout-main">
{entregables}
{roadmap}
        </div>
        <div class="layout-sidebar">
{docs}
{estrategia}
        </div>
    </div>
"""

# 4. Remove old sections from HTML and insert new layout
# Replace everything from end of header to the end of container
# We'll just split
top_part = html[:header_end]
bottom_part = html[html.find("</div>\n\n</body>"):]

final_html = top_part + new_layout + bottom_part

with open("dashboard_proyecto.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Layout updated successfully.")
