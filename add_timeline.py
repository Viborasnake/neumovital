import re

with open('dashboard_proyecto.html', 'r') as f:
    html = f.read()

# Update the header to indicate it's an "Avance"
html = html.replace('<p class="subtitle">Dashboard Estratégico y Arquitectura de Conversión</p>', 
                    '<p class="subtitle" style="display:inline-block; background:rgba(143, 85, 160, 0.1); color:var(--primary); padding:8px 20px; border-radius:50px; font-weight:800; font-size:14px; text-transform:uppercase; letter-spacing:1px; margin-top:10px;">Reporte de Avance y Próximos Pasos</p>')

# Find the header for the Board and inject the timeline banner
old_board_header = '<h2><i class="fa fa-trello"></i> Board del Proyecto (Mapa del Sitio)</h2>'
new_board_header = '''<h2><i class="fa fa-road"></i> Próximos Pasos (Roadmap de Desarrollo)</h2>
        <div style="background: rgba(70, 191, 238, 0.1); border-left: 4px solid var(--secondary); padding: 20px; border-radius: 8px; margin-bottom: 25px; display: flex; align-items: center; gap: 15px;">
            <i class="fa fa-calendar-check-o" style="color: var(--secondary); font-size: 28px;"></i>
            <div>
                <strong style="color: #111; display: block; font-size: 16px; margin-bottom: 5px;">Cronograma de Entregas (Inicio: Hoy)</strong>
                <span style="color: var(--text-muted); font-size: 15px; line-height: 1.5; display: block;">Se desarrollarán y entregarán aproximadamente <strong>2 páginas por semana</strong> a partir de hoy, siguiendo el orden de este listado. Esto garantiza revisiones ágiles y un avance constante del proyecto.</span>
            </div>
        </div>'''

html = html.replace(old_board_header, new_board_header)

with open('dashboard_proyecto.html', 'w') as f:
    f.write(html)
