import re

with open('dashboard_proyecto.html', 'r') as f:
    html = f.read()

new_cards = '''
            <!-- TARJETA: SOBRE NEUMOVITAL -->
            <div class="board-card">
                <div class="board-card-header">
                    <div class="board-card-title">Sobre Neumovital</div>
                    <span class="status-badge status-pending"><i class="fa fa-clock-o"></i> Editar</span>
                </div>
                <div class="board-item">
                    <strong>Ruta</strong>
                    /sobre-neumovital
                </div>
                <div class="board-item">
                    <strong>Contenido Estratégico</strong>
                    Detallar la misión, visión, valores (con enfoque humano), la historia de la clínica, la presentación de todo el equipo de profesionales y fotos de las instalaciones.
                </div>
            </div>

            <!-- TARJETA: DANIELA DIAZ -->
            <div class="board-card">
                <div class="board-card-header">
                    <div class="board-card-title">Daniela Díaz</div>
                    <span class="status-badge status-pending" style="background: rgba(70, 191, 238, 0.1); color: #0288d1;"><i class="fa fa-plus-circle"></i> Página Nueva</span>
                </div>
                <div class="board-item">
                    <strong>Ruta</strong>
                    /daniela-diaz
                </div>
                <div class="board-item">
                    <strong>Contenido Estratégico</strong>
                    Página dedicada exclusivamente a la fundadora. Incluirá su perfil completo, biografía detallada, credenciales (DENAKE, postgrados), su filosofía de trabajo con el Método Neumovital®, material audiovisual y publicaciones.
                </div>
            </div>

            <!-- TARJETA: SERVICIOS -->
            <div class="board-card">
                <div class="board-card-header">
                    <div class="board-card-title">Servicios</div>
                    <span class="status-badge status-pending"><i class="fa fa-clock-o"></i> Editar</span>
                </div>
                <div class="board-item">
                    <strong>Ruta</strong>
                    /servicios
                </div>
                <div class="board-item">
                    <strong>Contenido Estratégico</strong>
                    Visión general de la oferta integral. Detalle de Rehabilitación Pulmonar, Laboratorio de Función Pulmonar (espirometría, DLCO, volúmenes) y "Otros Servicios" (monitorización del sueño), junto con CTAs de reserva.
                </div>
            </div>

            <!-- TARJETA: PARA MEDICOS -->
            <div class="board-card">
                <div class="board-card-header">
                    <div class="board-card-title">Para Médicos</div>
                    <span class="status-badge status-pending" style="background: rgba(70, 191, 238, 0.1); color: #0288d1;"><i class="fa fa-plus-circle"></i> Página Nueva</span>
                </div>
                <div class="board-item">
                    <strong>Ruta</strong>
                    /para-medicos
                </div>
                <div class="board-item">
                    <strong>Contenido Estratégico</strong>
                    Dirigida a profesionales derivadores. Mostrará a Neumovital como centro aliado en diagnóstico y rehabilitación, cómo derivar pacientes, oportunidades de colaboración conjunta y contacto directo.
                </div>
            </div>

            <!-- TARJETA: PATOLOGIAS -->
            <div class="board-card">
                <div class="board-card-header">
                    <div class="board-card-title">Patologías</div>
                    <span class="status-badge status-pending" style="background: rgba(70, 191, 238, 0.1); color: #0288d1;"><i class="fa fa-plus-circle"></i> Página Nueva / Editar</span>
                </div>
                <div class="board-item">
                    <strong>Ruta</strong>
                    /patologias
                </div>
                <div class="board-item">
                    <strong>Contenido Estratégico</strong>
                    Enumerará las enfermedades tratadas (EPOC, EPI, Cáncer de Pulmón, Fibrosis Pulmonar, etc.), con una breve descripción de cada una y cómo la clínica ayuda en cada condición.
                </div>
            </div>

            <!-- TARJETA: FAQ -->
            <div class="board-card">
                <div class="board-card-header">
                    <div class="board-card-title">Preguntas Frecuentes</div>
                    <span class="status-badge status-pending" style="background: rgba(70, 191, 238, 0.1); color: #0288d1;"><i class="fa fa-plus-circle"></i> Página Nueva</span>
                </div>
                <div class="board-item">
                    <strong>Ruta</strong>
                    /faq
                </div>
                <div class="board-item">
                    <strong>Contenido Estratégico</strong>
                    Resolver dudas comunes sobre costos, proceso de agendamiento, atención por Fonasa/Isapre y duración de los tratamientos.
                </div>
            </div>

            <!-- TARJETA: CONTACTO -->
            <div class="board-card">
                <div class="board-card-header">
                    <div class="board-card-title">Contacto</div>
                    <span class="status-badge status-pending"><i class="fa fa-clock-o"></i> Editar</span>
                </div>
                <div class="board-item">
                    <strong>Ruta</strong>
                    /contacto
                </div>
                <div class="board-item">
                    <strong>Contenido Estratégico</strong>
                    Centralizar el formulario de consultas, visibilizar el teléfono y WhatsApp, correo electrónico, mapa de ubicación física y horarios de atención.
                </div>
            </div>
'''

# Find where <!-- TARJETA DIAGNOSTICO --> starts and replace everything from there to the end of the grid (before </div>\n    </div>\n\n</div>\n\n</body>)
html = re.sub(r'<!-- TARJETA DIAGNOSTICO -->.*?(?=        </div>\n    </div>\n\n</div>\n\n</body>)', new_cards, html, flags=re.DOTALL)

with open('dashboard_proyecto.html', 'w') as f:
    f.write(html)

print("Tarjetas actualizadas!")
