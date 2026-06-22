import re

with open('dashboard_proyecto.html', 'r') as f:
    html = f.read()

# The body replacement
new_body = '''<body>

<div class="container">
    <header>
        <h1>Neumo<span>Vital</span></h1>
        <p class="subtitle">Dashboard Estratégico y Arquitectura de Conversión</p>
    </header>

    <!-- OBJETIVOS -->
    <div class="section-block">
        <h2><i class="fa fa-bullseye"></i> Objetivos Estratégicos del Rediseño</h2>
        <ul class="custom-list">
            <li><strong>Potenciar la Marca Personal:</strong> Posicionar a Daniela Díaz Hinojosa como el eje articulador de la clínica, capitalizando su autoridad en el área respiratoria.</li>
            <li><strong>Mejorar la Jerarquía de Conversión:</strong> Optimizar la estructura del Home para eliminar la confusión del usuario y guiarlo directamente hacia la plataforma de agendamiento online.</li>
            <li><strong>Impulso Económico al Diagnóstico:</strong> Existe un interés particular en potenciar económicamente el <i>Laboratorio de Función Pulmonar</i> (espirometrías, pruebas especializadas), sin descuidar la Rehabilitación Pulmonar que es el corazón de la clínica.</li>
            <li><strong>Validación Social y B2B:</strong> Utilizar testimonios reales como prueba irrefutable del éxito del Método Neumovital® y captar a médicos derivadores posicionando la clínica como un centro solucionador.</li>
        </ul>
    </div>

    <!-- BOARD EXTENSO -->
    <div class="section-block">
        <h2><i class="fa fa-trello"></i> Board de Propuestas: Decisiones de Diseño y Funcionalidades</h2>
        <p style="margin-bottom: 30px; font-size: 16px; color: var(--text-muted); line-height: 1.8;">
            Para materializar los objetivos estratégicos, se han desarrollado dos propuestas de diseño funcionales. Ambas maquetas comparten una arquitectura de conversión robusta basada en embudos de venta médicos, pero difieren en su lenguaje visual para permitir elegir la identidad que mejor resuene con los pacientes.
        </p>
        
        <div class="board-grid" style="grid-template-columns: 1fr; gap: 30px;">
            
            <div class="board-card" style="display:flex; flex-direction:column; gap:10px;">
                <div class="board-card-header" style="margin-bottom:10px;">
                    <div class="board-card-title">1. Hero Section (El Primer Impacto)</div>
                </div>
                <div class="board-item"><strong>Problema Anterior</strong>El usuario llegaba y no sabía exactamente qué hacer o si la clínica cubría sus necesidades económicas.</div>
                <div class="board-item"><strong>Decisión de Diseño</strong>El mensaje central ahora apela a la emoción y el alivio: <i>"Vuelve a respirar, vuelve a vivir"</i>. Se integraron botones de acción primarios de inmediato.</div>
                <div class="board-item"><strong>Feature Destacado (Pills de Cobertura)</strong>Se añadieron "Pills" visuales de FONASA e ISAPRE directamente en la cabecera. Esto derriba la principal barrera económica de entrada desde el primer segundo.</div>
            </div>

            <div class="board-card" style="display:flex; flex-direction:column; gap:10px;">
                <div class="board-card-header" style="margin-bottom:10px;">
                    <div class="board-card-title">2. Visibilidad Inmediata de Patologías</div>
                </div>
                <div class="board-item"><strong>Problema Anterior</strong>Los pacientes crónicos debían buscar profundamente en la web para saber si su enfermedad específica era tratada.</div>
                <div class="board-item"><strong>Decisión de Diseño</strong>Se reemplazó el texto estático por un bloque visual de alto impacto (Marquesina infinita en V1 o Pills Orgánicas en V2).</div>
                <div class="board-item"><strong>Impacto en Conversión</strong>Al ver rápidamente condiciones como EPOC, Cáncer de Pulmón o Fibrosis Pulmonar, se genera una autoidentificación inmediata en el paciente.</div>
            </div>

            <div class="board-card" style="display:flex; flex-direction:column; gap:10px;">
                <div class="board-card-header" style="margin-bottom:10px;">
                    <div class="board-card-title">3. Transparencia Comercial (Modal de Precios)</div>
                </div>
                <div class="board-item"><strong>Problema Anterior</strong>La incertidumbre sobre el valor del copago ahuyenta a los pacientes en la etapa de consideración.</div>
                <div class="board-item"><strong>Decisión de Diseño</strong>Implementación de un botón estratégico de "Ver Rangos de Precios" debajo de cada servicio.</div>
                <div class="board-item"><strong>Feature Destacado (Pop-up Modal)</strong>Al hacer clic, se despliega una ventana interactiva con una tabla comparativa de copagos aproximados (Fonasa/Isapre) y un disclaimer legal.</div>
            </div>

            <div class="board-card" style="display:flex; flex-direction:column; gap:10px;">
                <div class="board-card-header" style="margin-bottom:10px;">
                    <div class="board-card-title">4. Authority Building (Dra. Daniela Díaz)</div>
                </div>
                <div class="board-item"><strong>Problema Anterior</strong>Neumovital se percibía como "una clínica más", perdiendo el inmenso valor humano y clínico de su fundadora.</div>
                <div class="board-item"><strong>Decisión de Diseño</strong>Creación de una sección completa dedicada exclusivamente a ella.</div>
                <div class="board-item"><strong>Feature Destacado</strong>Integración de fotografía profesional, credenciales médicas, cita personal sobre el trato humano y conexión directa a la comunidad en Instagram.</div>
            </div>

            <div class="board-card" style="display:flex; flex-direction:column; gap:10px;">
                <div class="board-card-header" style="margin-bottom:10px;">
                    <div class="board-card-title">5. Prueba Social y Captación B2B</div>
                </div>
                <div class="board-item"><strong>Testimonios Interactivos</strong>Se incorporó un carrusel deslizable con testimonios reales de pacientes. El "Social Proof" (leer a alguien decir "Me devolvieron la vida") es el gatillo mental más potente.</div>
                <div class="board-item"><strong>Alianza Estratégica Médica</strong>Creación de una sección orientada al 100% a profesionales derivadores. El bloque ofrece "Reportes Clínicos" y posiciona a la clínica como un aliado estratégico para el médico tratante.</div>
            </div>

            <div class="board-card" style="display:flex; flex-direction:column; gap:10px;">
                <div class="board-card-header" style="margin-bottom:10px;">
                    <div class="board-card-title">6. Cierre Persuasivo y Botón Flotante</div>
                </div>
                <div class="board-item"><strong>Problema Anterior</strong>El agendamiento manual generaba fricción operativa y pérdida de métricas en Analytics.</div>
                <div class="board-item"><strong>Decisión de Diseño</strong>Bloque masivo de alto contraste al final del sitio ("Es el momento de tomar el control") con un botón dirigido directo al software de reservas.</div>
                <div class="board-item"><strong>Feature Destacado (Floating CTA)</strong>Se programó un botón flotante dinámico que aparece al hacer scroll, asegurando que agendar esté siempre a un clic.</div>
            </div>

        </div>
    </div>
    
    <!-- LENGUAJE VISUAL / LINKS -->
    <div class="section-block">
        <h2><i class="fa fa-paint-brush"></i> Lenguaje Visual: Versión 1 vs. Versión 2</h2>
        <div class="board-grid">
            <div class="board-card">
                <div class="board-card-title" style="margin-bottom:15px; font-size:20px;">Propuesta V1: Rigor y Tecnología</div>
                <div class="board-item" style="margin-bottom:25px;">Utiliza formas geométricas sólidas, líneas rectas, modales estructurados y banners oscuros. El diseño proyecta estatus premium, ideal para transmitir rigor científico, precisión en exámenes y alta tecnología de laboratorio.</div>
                <div class="board-links" style="margin-top:auto;">
                    <a href="https://neumovital.cl/propuesta-v1/" target="_blank" class="link-proposal"><i class="fa fa-eye"></i> Ver Propuesta V1</a>
                </div>
            </div>
            <div class="board-card">
                <div class="board-card-title" style="margin-bottom:15px; font-size:20px;">Propuesta V2: Flujo Orgánico</div>
                <div class="board-item" style="margin-bottom:25px;">Incorpora bordes ultra redondeados, botones asimétricos (blobs), secciones en zigzag fluidas y sombras suaves. Todo "fluye" como el aire, transmitiendo una sensación subconsciente de alivio, empatía y rehabilitación suave.</div>
                <div class="board-links" style="margin-top:auto;">
                    <a href="https://neumovital.cl/propuesta-v2/" target="_blank" class="link-proposal" style="background:#46bfee;"><i class="fa fa-eye"></i> Ver Propuesta V2</a>
                </div>
            </div>
        </div>
    </div>

</div>

</body>'''

# Replace everything from <body> to </body>
new_html = re.sub(r'<body>.*</body>', new_body, html, flags=re.DOTALL)

with open('dashboard_proyecto.html', 'w') as f:
    f.write(new_html)

print("Dashboard actualizado exitosamente.")
