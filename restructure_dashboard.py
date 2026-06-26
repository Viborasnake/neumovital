import re
import sys

def main():
    with open("dashboard_proyecto.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Extract the Objetivos block
    objetivos_regex = r'(<!-- BENTO GRID: ESTRATEGIA -->[\s\S]*?<h2 class="section-title"><i class="fa-solid fa-crosshairs"></i> Objetivos Estratégicos</h2>[\s\S]*?<div class="bento-grid">[\s\S]*?</div>\s*</div>)'
    objetivos_match = re.search(objetivos_regex, html)
    if not objetivos_match:
        print("Could not find Objetivos block")
        sys.exit(1)
    
    objetivos_block = objetivos_match.group(1)

    # Remove Objetivos block from its original location
    html = html.replace(objetivos_block, "")

    # Insert Objetivos block after PROGRESO GLOBAL
    progreso_end_regex = r'(<!-- PROGRESO GLOBAL -->[\s\S]*?<!-- Legend / Milestones -->[\s\S]*?</div>\s*</div>)'
    progreso_match = re.search(progreso_end_regex, html)
    if not progreso_match:
        print("Could not find Progreso Global block")
        sys.exit(1)

    progreso_block = progreso_match.group(1)
    new_progreso_and_objetivos = progreso_block + "\n\n" + objetivos_block
    html = html.replace(progreso_block, new_progreso_and_objetivos)

    # 2. Replace the Docs block
    docs_regex = r'(<!-- DOCS & EXTRA SECTION -->[\s\S]*?<h2 class="section-title"[^>]*>.*?Documentación y Referencias</h2>[\s\S]*?<div class="features-grid"[^>]*>[\s\S]*?</div>\s*(?:</div>)?)'
    docs_match = re.search(docs_regex, html)
    if docs_match:
        docs_block = docs_match.group(1)
        
        new_docs_block = """<!-- DOCS & EXTRA SECTION -->
            <div style="background: #f0fdfa; border: 1px solid #ccfbf1; border-radius: var(--radius-md); padding: 24px; margin-bottom: 30px; box-shadow: 0 10px 25px rgba(20, 184, 166, 0.1);">
                <h3 style="color: #0f766e; font-size: 18px; font-weight: 800; margin-bottom: 12px; display: flex; align-items: center; gap: 10px;">
                    <i class="fa-solid fa-folder-open" style="color: #14b8a6;"></i> Documentación Central
                </h3>
                <ul style="color: #115e59; font-size: 14px; margin-bottom: 15px; margin-left: 20px; line-height: 1.6;">
                    <li><strong>Informe Estratégico:</strong> Propuesta de valor y hallazgos. <a href="https://github.com/Viborasnake/neumovital/raw/main/discovery/Informe_Estrat%C3%A9gico_Redise%C3%B1o_del_Home_de_Neumovital.docx" target="_blank" style="color: #0d9488; font-weight: 700; text-decoration: none;"><i class="fa-solid fa-download"></i> Descargar</a></li>
                    <li><strong>Benchmark:</strong> Análisis de competidores. <a href="https://github.com/Viborasnake/neumovital/raw/main/discovery/Informe%20Benchmark%20Neumovital.docx" target="_blank" style="color: #0d9488; font-weight: 700; text-decoration: none;"><i class="fa-solid fa-download"></i> Descargar</a></li>
                    <li><strong>Discovery:</strong> Respuestas de Daniela y equipo. <a href="https://github.com/Viborasnake/neumovital/raw/main/discovery/Discovery%20Respuestas%20Cliente%20Neumovital%20(PRE%20CAMBIOS).docx" target="_blank" style="color: #0d9488; font-weight: 700; text-decoration: none;"><i class="fa-solid fa-download"></i> Descargar</a></li>
                </ul>
                <span class="rm-tag" style="background: #ccfbf1; color: #0f766e; border: 1px solid #99f6e4; font-weight: 700; font-size: 12px;"><i class="fa-brands fa-github"></i> En repositorio</span>
            </div>"""
        html = html.replace(docs_block, new_docs_block)
    else:
        print("Could not find Docs block")

    # 3. Insert Greeting
    greeting_html = """
    <div style="background: var(--surface); padding: 20px 25px; border-radius: var(--radius-md); border-left: 4px solid var(--primary); margin-bottom: 30px; font-size: 16px; color: var(--text-main); line-height: 1.6; box-shadow: var(--shadow-sm);">
        <strong>Estimado Rodrigo,</strong> te comparto el informe de avances.
    </div>
"""
    header_end_regex = r'(</header>)'
    html = re.sub(header_end_regex, r'\1' + greeting_html, html)

    with open("dashboard_proyecto.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Dashboard restructured successfully.")

if __name__ == "__main__":
    main()
