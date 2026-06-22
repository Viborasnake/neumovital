import re

with open('dashboard_proyecto.html', 'r') as f:
    html = f.read()

new_roadmap = '''
        <div class="roadmap-timeline">
            
            <!-- TARJETA: SOBRE NEUMOVITAL -->
            <div class="roadmap-item">
                <div class="roadmap-header">
                    <div class="roadmap-title">1. Sobre Neumovital</div>
                    <div class="roadmap-meta">
                        <span class="roadmap-date"><i class="fa fa-calendar"></i> Semana 1 (24 - 28 Jun)</span>
                        <span class="status-badge status-pending"><i class="fa fa-clock-o"></i> Editar</span>
                    </div>
                </div>
                <div class="board-item"><strong>Ruta:</strong> /sobre-neumovital</div>
                <div class="board-item"><strong>Contenido Estratégico:</strong> Detallar la misión, visión, valores (con enfoque humano), la historia de la clínica, la presentación de todo el equipo de profesionales y fotos de las instalaciones.</div>
                <div class="board-links"><a href="https://neumovital.cl/about-us/" target="_blank" class="link-current"><i class="fa fa-link"></i> Link Actual (Nuestro Centro)</a><a href="https://neumovital.cl/our-staff/" target="_blank" class="link-current"><i class="fa fa-link"></i> Link Actual (Profesionales)</a></div>
                <div class="progress-wrapper"><div class="progress-header"><span>Avance</span><span>0%</span></div><div class="progress-bar-container"><div class="progress-bar" style="width: 0%;"></div></div></div>
            </div>

            <!-- TARJETA: DANIELA DIAZ -->
            <div class="roadmap-item">
                <div class="roadmap-header">
                    <div class="roadmap-title">2. Daniela Díaz</div>
                    <div class="roadmap-meta">
                        <span class="roadmap-date"><i class="fa fa-calendar"></i> Semana 1 (24 - 28 Jun)</span>
                        <span class="status-badge status-pending" style="background: rgba(70, 191, 238, 0.1); color: #0288d1;"><i class="fa fa-plus-circle"></i> Página Nueva</span>
                    </div>
                </div>
                <div class="board-item"><strong>Ruta:</strong> /daniela-diaz</div>
                <div class="board-item"><strong>Contenido Estratégico:</strong> Página dedicada exclusivamente a la fundadora. Incluirá su perfil completo, biografía detallada, credenciales (DENAKE, postgrados), su filosofía de trabajo con el Método Neumovital®, material audiovisual y publicaciones.</div>
                <div class="progress-wrapper"><div class="progress-header"><span>Avance</span><span>0%</span></div><div class="progress-bar-container"><div class="progress-bar" style="width: 0%;"></div></div></div>
            </div>

            <!-- TARJETA: SERVICIOS -->
            <div class="roadmap-item">
                <div class="roadmap-header">
                    <div class="roadmap-title">3. Servicios</div>
                    <div class="roadmap-meta">
                        <span class="roadmap-date"><i class="fa fa-calendar"></i> Semana 2 (1 - 5 Jul)</span>
                        <span class="status-badge status-pending"><i class="fa fa-clock-o"></i> Editar</span>
                    </div>
                </div>
                <div class="board-item"><strong>Ruta:</strong> /servicios</div>
                <div class="board-item"><strong>Contenido Estratégico:</strong> Visión general de la oferta integral. Detalle de Rehabilitación Pulmonar, Laboratorio de Función Pulmonar (espirometría, DLCO, volúmenes) y "Otros Servicios" (monitorización del sueño), junto con CTAs de reserva.</div>
                <div class="board-links"><a href="https://neumovital.cl/services/" target="_blank" class="link-current"><i class="fa fa-link"></i> Link Actual (Servicios)</a></div>
                <div class="progress-wrapper"><div class="progress-header"><span>Avance</span><span>0%</span></div><div class="progress-bar-container"><div class="progress-bar" style="width: 0%;"></div></div></div>
            </div>

            <!-- TARJETA: PARA MEDICOS -->
            <div class="roadmap-item">
                <div class="roadmap-header">
                    <div class="roadmap-title">4. Para Médicos</div>
                    <div class="roadmap-meta">
                        <span class="roadmap-date"><i class="fa fa-calendar"></i> Semana 2 (1 - 5 Jul)</span>
                        <span class="status-badge status-pending" style="background: rgba(70, 191, 238, 0.1); color: #0288d1;"><i class="fa fa-plus-circle"></i> Página Nueva</span>
                    </div>
                </div>
                <div class="board-item"><strong>Ruta:</strong> /para-medicos</div>
                <div class="board-item"><strong>Contenido Estratégico:</strong> Dirigida a profesionales derivadores. Mostrará a Neumovital como centro aliado en diagnóstico y rehabilitación, cómo derivar pacientes, oportunidades de colaboración conjunta y contacto directo.</div>
                <div class="progress-wrapper"><div class="progress-header"><span>Avance</span><span>0%</span></div><div class="progress-bar-container"><div class="progress-bar" style="width: 0%;"></div></div></div>
            </div>

            <!-- TARJETA: PATOLOGIAS -->
            <div class="roadmap-item">
                <div class="roadmap-header">
                    <div class="roadmap-title">5. Patologías</div>
                    <div class="roadmap-meta">
                        <span class="roadmap-date"><i class="fa fa-calendar"></i> Semana 3 (8 - 12 Jul)</span>
                        <span class="status-badge status-pending" style="background: rgba(70, 191, 238, 0.1); color: #0288d1;"><i class="fa fa-plus-circle"></i> Página Nueva / Editar</span>
                    </div>
                </div>
                <div class="board-item"><strong>Ruta:</strong> /patologias</div>
                <div class="board-item"><strong>Contenido Estratégico:</strong> Enumerará las enfermedades tratadas (EPOC, EPI, Cáncer de Pulmón, Fibrosis Pulmonar, etc.), con una breve descripción de cada una y cómo la clínica ayuda en cada condición.</div>
                <div class="progress-wrapper"><div class="progress-header"><span>Avance</span><span>0%</span></div><div class="progress-bar-container"><div class="progress-bar" style="width: 0%;"></div></div></div>
            </div>

            <!-- TARJETA: FAQ -->
            <div class="roadmap-item">
                <div class="roadmap-header">
                    <div class="roadmap-title">6. Preguntas Frecuentes (FAQ)</div>
                    <div class="roadmap-meta">
                        <span class="roadmap-date"><i class="fa fa-calendar"></i> Semana 3 (8 - 12 Jul)</span>
                        <span class="status-badge status-pending" style="background: rgba(70, 191, 238, 0.1); color: #0288d1;"><i class="fa fa-plus-circle"></i> Página Nueva</span>
                    </div>
                </div>
                <div class="board-item"><strong>Ruta:</strong> /faq</div>
                <div class="board-item"><strong>Contenido Estratégico:</strong> Resolver dudas comunes sobre costos, proceso de agendamiento, atención por Fonasa/Isapre y duración de los tratamientos.</div>
                <div class="progress-wrapper"><div class="progress-header"><span>Avance</span><span>0%</span></div><div class="progress-bar-container"><div class="progress-bar" style="width: 0%;"></div></div></div>
            </div>

            <!-- TARJETA: CONTACTO -->
            <div class="roadmap-item">
                <div class="roadmap-header">
                    <div class="roadmap-title">7. Contacto</div>
                    <div class="roadmap-meta">
                        <span class="roadmap-date"><i class="fa fa-calendar"></i> Semana 4 (15 - 19 Jul)</span>
                        <span class="status-badge status-pending"><i class="fa fa-clock-o"></i> Editar</span>
                    </div>
                </div>
                <div class="board-item"><strong>Ruta:</strong> /contacto</div>
                <div class="board-item"><strong>Contenido Estratégico:</strong> Centralizar el formulario de consultas, visibilizar el teléfono y WhatsApp, correo electrónico, mapa de ubicación física y horarios de atención.</div>
                <div class="board-links"><a href="https://neumovital.cl/appointment-booking/" target="_blank" class="link-current"><i class="fa fa-link"></i> Link Actual (Reservas/Contacto)</a></div>
                <div class="progress-wrapper"><div class="progress-header"><span>Avance</span><span>0%</span></div><div class="progress-bar-container"><div class="progress-bar" style="width: 0%;"></div></div></div>
            </div>
            
        </div>
'''

# Find where <!-- TARJETA: SOBRE NEUMOVITAL --> starts and replace everything from there to the end of the board-grid.
# The end of the board-grid is marked by the closing </div> tags before </body>
html = re.sub(r'<!-- TARJETA: SOBRE NEUMOVITAL -->.*?(?=        </div>\n    </div>\n\n</div>\n\n</body>)', new_roadmap + '\n', html, flags=re.DOTALL)

with open('dashboard_proyecto.html', 'w') as f:
    f.write(html)

print("Roadmap HTML aplicado correctamente!")
