import re

with open('dashboard_proyecto.html', 'r') as f:
    html = f.read()

new_styles = '''
        ul.features-list { display:none; } /* removing old list */
        .feature-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 15px;
        }
        .feature-box {
            background: #ffffff;
            border-radius: 12px;
            padding: 25px;
            border: 1px solid var(--border);
            border-top: 4px solid var(--secondary);
            box-shadow: 0 10px 20px rgba(0,0,0,0.02);
            transition: 0.3s;
        }
        .feature-box:hover {
            box-shadow: 0 15px 30px rgba(143,85,160,0.08);
            transform: translateY(-3px);
        }
        .feature-box-title {
            font-size: 18px;
            font-weight: 900;
            color: var(--primary);
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
            letter-spacing: -0.5px;
        }
        .feature-box-desc {
            font-size: 14.5px;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 15px;
        }
        .feature-box-impact {
            font-size: 13px;
            font-weight: 700;
            color: #111;
            background: rgba(70, 191, 238, 0.1);
            border-left: 3px solid var(--secondary);
            padding: 8px 12px;
            border-radius: 0 6px 6px 0;
            margin-top:auto;
        }
        
        .v-card-container {
            display: flex;
            gap: 20px;
            margin-top: 15px;
        }
        .v-card {
            background: #f8fbfc;
            border-radius: 15px;
            padding: 25px;
            flex: 1;
            border: 1px solid var(--border);
        }
        .v-card h4 {
            font-size: 20px;
            font-weight: 900;
            margin-bottom: 10px;
            color: var(--text-dark);
        }
        .v-card p {
            font-size: 14px;
            color: var(--text-muted);
            line-height: 1.6;
        }
        .home-layout {
            display: flex;
            flex-direction: column;
            gap: 40px;
        }
'''

new_home_card = '''
                <div class="home-layout">
                    <!-- SECTION 1: ESTRATEGIA -->
                    <div>
                        <h3 style="font-size:22px; color:var(--text-dark); margin-bottom:10px; font-weight:900;"><i class="fa fa-cogs" style="color:var(--secondary);"></i> 1. Arquitectura y Funcionalidades (Features)</h3>
                        <p style="color:var(--text-muted); font-size:15px; margin-bottom:20px;">Cada sección fue diseñada para resolver un problema específico de conversión o comunicación que presentaba el sitio original.</p>
                        
                        <div class="feature-grid">
                            <div class="feature-box">
                                <div class="feature-box-title"><i class="fa fa-bolt"></i> Hero & Cobertura</div>
                                <div class="feature-box-desc"><strong>Problema:</strong> El usuario llegaba sin saber qué hacer ni si podría costearlo.<br><strong>Solución:</strong> Mensaje de alivio ("Vuelve a respirar") con CTAs inmediatos.</div>
                                <div class="feature-box-impact">Feature: Badges de FONASA/ISAPRE integrados en la cabecera.</div>
                            </div>
                            
                            <div class="feature-box">
                                <div class="feature-box-title"><i class="fa fa-stethoscope"></i> Patologías Visibles</div>
                                <div class="feature-box-desc"><strong>Problema:</strong> Falta de identificación del paciente crónico.<br><strong>Solución:</strong> Listado visual de alto impacto de patologías (EPOC, Apnea, Fibrosis).</div>
                                <div class="feature-box-impact">Feature: Marquesina infinita o Pills orgánicas de lectura rápida.</div>
                            </div>

                            <div class="feature-box">
                                <div class="feature-box-title"><i class="fa fa-money"></i> Transparencia Comercial</div>
                                <div class="feature-box-desc"><strong>Problema:</strong> La incertidumbre del copago ahuyentaba pacientes.<br><strong>Solución:</strong> Transparencia total en precios sin arriesgar promesas falsas.</div>
                                <div class="feature-box-impact">Feature: Pop-up interactivo con tabla de rangos y disclaimer.</div>
                            </div>

                            <div class="feature-box">
                                <div class="feature-box-title"><i class="fa fa-user-md"></i> Authority Building</div>
                                <div class="feature-box-desc"><strong>Problema:</strong> Percepción de ser "una clínica más".<br><strong>Solución:</strong> Humanizar la marca mediante la trayectoria de su fundadora.</div>
                                <div class="feature-box-impact">Feature: Sección biográfica Dra. Daniela Díaz con conexión a RRSS.</div>
                            </div>

                            <div class="feature-box">
                                <div class="feature-box-title"><i class="fa fa-handshake-o"></i> Captación B2B</div>
                                <div class="feature-box-desc"><strong>Problema:</strong> Dependencia de referidos sin hablarle al médico derivador.<br><strong>Solución:</strong> Posicionar a la clínica como una extensión de excelencia.</div>
                                <div class="feature-box-impact">Feature: Banner exclusivo ofreciendo "Reportes Clínicos".</div>
                            </div>

                            <div class="feature-box">
                                <div class="feature-box-title"><i class="fa fa-mouse-pointer"></i> Flujo de Cierre</div>
                                <div class="feature-box-desc"><strong>Problema:</strong> Fricción en el agendamiento manual (WhatsApp).<br><strong>Solución:</strong> Estandarización del flujo hacia el software de reservas.</div>
                                <div class="feature-box-impact">Feature: Floating CTA y bloque de alto contraste ("Toma el control").</div>
                            </div>
                        </div>
                    </div>

                    <!-- SECTION 2: LENGUAJE VISUAL -->
                    <div>
                        <h3 style="font-size:22px; color:var(--text-dark); margin-bottom:10px; font-weight:900;"><i class="fa fa-paint-brush" style="color:var(--secondary);"></i> 2. Identidad Visual de las Propuestas</h3>
                        <p style="color:var(--text-muted); font-size:15px; margin-bottom:20px;">Se crearon dos lenguajes estéticos (vestuarios) para la misma arquitectura funcional.</p>
                        
                        <div class="v-card-container">
                            <div class="v-card" style="border-top: 5px solid var(--primary);">
                                <h4>V1: Rigor y Tecnología</h4>
                                <p style="margin-bottom:20px;">Formas geométricas, modales estructurados y banners oscuros. Proyecta estatus premium y precisión clínica.</p>
                                <a href="https://neumovital.cl/propuesta-v1/" target="_blank" class="link-proposal" style="display:inline-block; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:700; text-transform:uppercase; font-size:13px; color:#fff; background:var(--primary);"><i class="fa fa-eye"></i> Ver V1</a>
                            </div>
                            <div class="v-card" style="border-top: 5px solid var(--secondary);">
                                <h4>V2: Flujo Orgánico</h4>
                                <p style="margin-bottom:20px;">Bordes ultra redondeados, blobs y secciones zigzag fluidas. Transmite alivio, empatía y cuidado humano.</p>
                                <a href="https://neumovital.cl/propuesta-v2/" target="_blank" class="link-proposal-v2" style="display:inline-block; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:700; text-transform:uppercase; font-size:13px; color:#fff; background:var(--secondary);"><i class="fa fa-eye"></i> Ver V2</a>
                            </div>
                        </div>
                    </div>
                </div>
'''

# 1. Inject CSS
html = html.replace('</style>', new_styles + '\n</style>')

# 2. Replace the old flex layout inside the Home Card
# The old layout starts with `<div style="display:flex; gap:30px; flex-wrap:wrap;">` and ends before `<!-- TARJETA DIAGNOSTICO -->`
# I'll use regex to replace it
html = re.sub(r'<div style="display:flex; gap:30px; flex-wrap:wrap;">.*?</div>\s*</div>\s*<!-- TARJETA DIAGNOSTICO -->', new_home_card + '\n</div>\n<!-- TARJETA DIAGNOSTICO -->', html, flags=re.DOTALL)

with open('dashboard_proyecto.html', 'w') as f:
    f.write(html)

print("Dashboard hierarchy updated successfully.")
