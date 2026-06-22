html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NeumoVital - Strategic Discovery Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        :root {
            --primary: #8f55a0;
            --primary-hover: #7a468a;
            --secondary: #46bfee;
            --bg-body: #f8fbfc;
            --bg-card: #ffffff;
            --text-dark: #111111;
            --text-muted: #555555;
            --border: #eef2f5;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-body);
            color: var(--text-dark);
            line-height: 1.6;
            padding: 40px 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 50px;
        }

        h1 {
            font-size: 45px;
            font-weight: 900;
            color: var(--primary);
            margin-bottom: 10px;
            letter-spacing: -1px;
        }

        h1 span {
            color: var(--secondary);
        }

        .subtitle {
            font-size: 18px;
            color: var(--text-muted);
            font-weight: 500;
        }

        .section-block {
            background: var(--bg-card);
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 40px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.03);
            border-top: 5px solid var(--primary);
        }

        .section-block h2 {
            font-size: 26px;
            font-weight: 800;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 12px;
            color: var(--text-dark);
        }

        .section-block h2 i {
            color: var(--secondary);
        }

        /* Lists */
        ul.custom-list {
            list-style: none;
        }

        ul.custom-list li {
            margin-bottom: 20px;
            padding-left: 35px;
            position: relative;
            font-size: 16px;
            color: var(--text-muted);
            line-height: 1.7;
        }

        ul.custom-list li::before {
            content: '\f105';
            font-family: 'FontAwesome';
            position: absolute;
            left: 0;
            top: 2px;
            color: #ffffff;
            background: var(--primary);
            width: 20px;
            height: 20px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
        }

        ul.custom-list li strong {
            color: var(--text-dark);
            font-weight: 800;
            display: block;
            font-size: 17px;
            margin-bottom: 5px;
        }
        
        ul.features-list {
            list-style: none;
            margin-top: 10px;
            padding: 0;
        }
        ul.features-list li {
            margin-bottom: 15px;
            padding-left: 20px;
            position: relative;
            font-size: 14px;
            color: var(--text-muted);
            line-height: 1.5;
            border-left: 3px solid var(--secondary);
        }
        ul.features-list li strong {
            color: var(--primary);
            font-weight: 700;
        }

        /* Board Grid */
        .board-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
        }

        .board-card {
            background: var(--bg-body);
            border-radius: 15px;
            padding: 30px;
            border: 1px solid var(--border);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        .board-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(143, 85, 160, 0.08);
            border-color: var(--primary);
        }

        .board-card-header {
            border-bottom: 1px solid var(--border);
            padding-bottom: 15px;
            margin-bottom: 20px;
        }

        .board-card-title {
            font-size: 22px;
            font-weight: 800;
            color: var(--primary);
            letter-spacing: -0.5px;
        }

        .board-item {
            margin-bottom: 15px;
            font-size: 15px;
            color: var(--text-muted);
        }

        .board-item strong {
            display: block;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: var(--secondary);
            margin-bottom: 5px;
            font-weight: 800;
        }

        .board-links {
            margin-top: auto;
            padding-top: 25px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .board-links a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            text-decoration: none;
            padding: 12px 15px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 14px;
            transition: 0.3s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .link-current {
            background-color: #ffffff;
            color: #111111;
            border: 1px solid #d0d0d0;
        }

        .link-current:hover {
            background-color: #111111;
            color: #ffffff;
            border-color: #111111;
        }

        .link-proposal {
            background-color: var(--primary);
            color: #ffffff;
            box-shadow: 0 5px 15px rgba(143,85,160,0.2);
        }

        .link-proposal:hover {
            background-color: var(--primary-hover);
            transform: translateY(-2px);
        }
        
        .link-proposal-v2 {
            background-color: var(--secondary);
            color: #ffffff;
            box-shadow: 0 5px 15px rgba(70,191,238,0.2);
        }

        .link-proposal-v2:hover {
            background-color: #35a5d4;
            transform: translateY(-2px);
        }

        .status-badge {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 50px;
            font-size: 11px;
            font-weight: 800;
            margin-top: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .status-completed { background: rgba(37, 211, 102, 0.15); color: #1e8745; }
        .status-pending { background: rgba(230, 104, 60, 0.1); color: #e6683c; }

    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>Neumo<span>Vital</span></h1>
        <p class="subtitle">Dashboard Estratégico y Arquitectura de Conversión</p>
    </header>

    <div class="section-block">
        <h2><i class="fa fa-bullseye"></i> Objetivos Estratégicos del Rediseño</h2>
        <ul class="custom-list">
            <li><strong>Potenciar la Marca Personal:</strong> Posicionar a Daniela Díaz Hinojosa como el eje articulador de la clínica, capitalizando su autoridad en el área respiratoria.</li>
            <li><strong>Mejorar la Jerarquía de Conversión:</strong> Optimizar la estructura del Home para eliminar la confusión del usuario y guiarlo directamente hacia la plataforma de agendamiento online.</li>
            <li><strong>Impulso Económico al Diagnóstico:</strong> Existe un interés particular en potenciar económicamente el <i>Laboratorio de Función Pulmonar</i> (espirometrías, pruebas especializadas), sin descuidar la Rehabilitación Pulmonar que es el corazón de la clínica.</li>
            <li><strong>Validación Social y Captación B2B:</strong> Utilizar testimonios y el Método Neumovital® como prueba social irrefutable, y atraer a médicos derivadores como aliados estratégicos.</li>
        </ul>
    </div>

    <div class="section-block">
        <h2><i class="fa fa-trello"></i> Board del Proyecto (Mapa del Sitio)</h2>
        
        <div class="board-grid">
            
            <!-- TARJETA HOME -->
            <div class="board-card" style="grid-column: 1 / -1;">
                <div class="board-card-header">
                    <div class="board-card-title">Home / Inicio</div>
                    <span class="status-badge status-completed"><i class="fa fa-check"></i> Rediseñado</span>
                </div>
                
                <div style="display:flex; gap:30px; flex-wrap:wrap;">
                    <div style="flex:1; min-width:300px;">
                        <div class="board-item">
                            <strong>Objetivo</strong>
                            Landing page principal. Embudo de ventas enfocado en confianza y reserva de horas médicas.
                        </div>
                        <div class="board-item">
                            <strong>Nuevas Funcionalidades (Features) y Decisiones de Diseño</strong>
                            <ul class="features-list">
                                <li><strong>1. Hero & Cobertura:</strong> Mensaje de alivio ("Vuelve a respirar") con botones primarios inmediatos y distintivos de FONASA/ISAPRE para derribar barreras económicas de entrada.</li>
                                <li><strong>2. Visibilidad de Patologías:</strong> Se agregó un carrusel/pills de alto impacto para que el paciente crónico (EPOC, Cáncer, Fibrosis, Apnea) se autoidentifique rápidamente.</li>
                                <li><strong>3. Transparencia Comercial:</strong> Nuevo "Modal de Precios" accesible bajo cada servicio, desplegando copagos aproximados (Fonasa/Isapre) para reducir la fricción antes de agendar.</li>
                                <li><strong>4. Authority Building:</strong> Sección biográfica dedicada a la Dra. Daniela Díaz H., humanizando la clínica a través de su filosofía y experiencia clínica.</li>
                                <li><strong>5. Social Proof y Alianza Médica:</strong> Carrusel de testimonios reales y un banner exclusivo (B2B) orientado a captar a Médicos Especialistas derivadores.</li>
                                <li><strong>6. CTA Persuasivo:</strong> Botón de reserva flotante para móviles y un bloque masivo de cierre ("Toma el control"), estandarizando el flujo hacia el software de reservas.</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div style="flex:1; min-width:300px; display:flex; flex-direction:column; justify-content:center;">
                        <div class="board-item">
                            <strong>Identidad Visual de las Propuestas</strong>
                            <p style="font-size:14px; line-height:1.5;">
                                Se crearon dos vestuarios para la misma arquitectura funcional:<br><br>
                                <b>V1 (Rigor y Tecnología):</b> Formas geométricas, modales estructurados y banners oscuros. Proyecta estatus premium y precisión clínica.<br><br>
                                <b>V2 (Flujo Orgánico):</b> Bordes ultra redondeados, blobs y secciones zigzag fluidas. Transmite alivio, empatía y cuidado humano.
                            </p>
                        </div>
                        <div class="board-links">
                            <a href="https://neumovital.cl/" target="_blank" class="link-current"><i class="fa fa-link"></i> Link Actual (Original)</a>
                            <a href="https://neumovital.cl/propuesta-v1/" target="_blank" class="link-proposal"><i class="fa fa-eye"></i> Ver Propuesta V1</a>
                            <a href="https://neumovital.cl/propuesta-v2/" target="_blank" class="link-proposal-v2"><i class="fa fa-eye"></i> Ver Propuesta V2</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TARJETA DIAGNOSTICO -->
            <div class="board-card">
                <div class="board-card-header">
                    <div class="board-card-title">Diagnóstico</div>
                    <span class="status-badge status-pending"><i class="fa fa-clock-o"></i> Próximo Objetivo</span>
                </div>
                <div class="board-item">
                    <strong>Objetivo</strong>
                    Potenciar económicamente el Laboratorio de Función Pulmonar y Monitorización del Sueño.
                </div>
                <div class="board-item">
                    <strong>Contenido Estratégico</strong>
                    Detalle de exámenes (Espirometría, DLCO), tecnología de frontera, precisión diagnóstica.
                </div>
                <div class="board-links">
                    <a href="https://neumovital.cl/services/#PruebasyEstudios" target="_blank" class="link-current"><i class="fa fa-link"></i> Link Actual (Ancla)</a>
                </div>
            </div>

            <!-- TARJETA REHABILITACION -->
            <div class="board-card">
                <div class="board-card-header">
                    <div class="board-card-title">Rehabilitación</div>
                    <span class="status-badge status-pending"><i class="fa fa-clock-o"></i> Pendiente</span>
                </div>
                <div class="board-item">
                    <strong>Objetivo</strong>
                    El corazón clínico del centro. Mostrar el valor del tratamiento a largo plazo.
                </div>
                <div class="board-item">
                    <strong>Contenido Estratégico</strong>
                    Ingreso, sesiones y alta. Enfoque personalizado para recuperar tolerancia al ejercicio e independencia.
                </div>
                <div class="board-links">
                    <a href="https://neumovital.cl/services/#ServiciosClinicos" target="_blank" class="link-current"><i class="fa fa-link"></i> Link Actual (Ancla)</a>
                </div>
            </div>

            <!-- TARJETA NUESTRO CENTRO -->
            <div class="board-card">
                <div class="board-card-header">
                    <div class="board-card-title">Nuestro Centro & Profesionales</div>
                    <span class="status-badge status-pending"><i class="fa fa-clock-o"></i> Pendiente</span>
                </div>
                <div class="board-item">
                    <strong>Objetivo</strong>
                    Generar confianza institucional y respaldo clínico al Método Neumovital®.
                </div>
                <div class="board-item">
                    <strong>Contenido Estratégico</strong>
                    Misión, visión, instalaciones y perfiles del equipo médico/clínico.
                </div>
                <div class="board-links">
                    <a href="https://neumovital.cl/about-us/" target="_blank" class="link-current"><i class="fa fa-link"></i> Link Nuestro Centro</a>
                    <a href="https://neumovital.cl/our-staff/" target="_blank" class="link-current"><i class="fa fa-link"></i> Link Profesionales</a>
                </div>
            </div>

        </div>
    </div>

</div>

</body>
</html>"""

with open('dashboard_proyecto.html', 'w') as f:
    f.write(html)

print("Dashboard restaurado exitosamente.")
