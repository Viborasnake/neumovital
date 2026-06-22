# Informe Estratégico: Rediseño del Home de Neumovital

## 1. Objetivos Estratégicos

A partir del análisis profundo de las necesidades de la clínica, se han identificado los siguientes objetivos fundamentales para el rediseño del Home:

*   **Potenciar la Marca Personal:** Posicionar a Daniela Díaz Hinojosa como el eje articulador de la clínica, destacando su experiencia clínica, autoridad y su enfoque humano materializado en el Método Neumovital®.
*   **Mejorar la Jerarquía de Conversión:** Eliminar la confusión del diseño anterior. Guiar al usuario de manera intuitiva y directa hacia la reserva de horas.
*   **Impulsar el Laboratorio de Función Pulmonar:** Dar mayor visibilidad y tracción económica a la toma de exámenes, sin descuidar la Rehabilitación Pulmonar (el corazón del centro).
*   **Atraer al Paciente Ideal:** Captar pacientes crónicos (EPOC, Fibrosis, etc.) y posicionar a la clínica como el centro solucionador definitivo para médicos derivadores.

---

## 2. Board de Propuestas: Decisiones de Diseño y Arquitectura

Para materializar los objetivos estratégicos, se han desarrollado **dos propuestas de diseño funcional (Versión 1 y Versión 2)**. Ambas maquetas comparten una arquitectura de conversión robusta basada en embudos de venta médicos, pero difieren en su lenguaje visual para permitir elegir la identidad que mejor resuene con los pacientes.

A continuación, se detalla la reestructuración de las características (features) y las decisiones de diseño aplicadas a los bloques del Home:

### 2.1. Hero Section (El Primer Impacto)
*   **El Problema Anterior:** El usuario llegaba y no sabía exactamente qué hacer o si la clínica cubría sus necesidades económicas.
*   **Decisión de Diseño:** El mensaje central ahora apela a la emoción y el alivio: *"Vuelve a respirar, vuelve a vivir"*. Se integraron botones de acción primarios ("Agendar Evaluación") de inmediato. 
*   **Feature Estratégico (Pills de Cobertura):** Se añadieron "Pills" visuales de **FONASA e ISAPRE** directamente en la cabecera. Esto derriba la principal barrera económica de entrada desde el primer segundo de navegación.

### 2.2. Visibilidad Inmediata de Patologías
*   **El Problema Anterior:** Los pacientes crónicos debían buscar profundamente en la web para saber si su enfermedad específica era tratada.
*   **Decisión de Diseño:** Se reemplazó el texto estático y escondido por un bloque de alto impacto (Marquesina infinita en V1 / Pills Orgánicas con sombras profundas en V2). 
*   **Impacto:** Al ver rápidamente condiciones como *EPOC, Cáncer de Pulmón, Apnea del Sueño o Fibrosis Pulmonar*, se genera una autoidentificación inmediata en el paciente, aumentando el tiempo de retención.

### 2.3. Transparencia Comercial (Modal de Precios)
*   **El Problema Anterior:** La incertidumbre sobre el valor del copago ahuyenta a los pacientes en la etapa de consideración.
*   **Decisión de Diseño:** Se implementó un botón estratégico de *"Ver Rangos de Precios"* discretamente ubicado debajo de la descripción de cada servicio (Espirometría, Rehabilitación, etc.).
*   **Feature (Pop-up Modal):** Al hacer clic, se despliega una ventana modal interactiva con una tabla de tres columnas que detalla los copagos aproximados (Fonasa/Isapre). Se incluyó un "disclaimer" aclarando que son valores referenciales, lo que protege a la clínica legalmente mientras ofrece la transparencia que el mercado actual exige.

### 2.4. Potenciación de la Fundadora (Authority Building)
*   **El Problema Anterior:** Neumovital se percibía como "una clínica más", perdiendo el inmenso valor de la experiencia de su fundadora.
*   **Decisión de Diseño:** Se diseñó una sección dedicada exclusivamente a la Dra. Daniela Díaz H. 
*   **Feature:** Integración de una fotografía destacada, su título (Kinesióloga Especialista DENAKE), una cita personal sobre el trato humano y un enlace directo a la comunidad de Instagram. Esto humaniza la marca y construye autoridad clínica ("Authority Building").

### 2.5. Prueba Social (Testimonios Reales)
*   **El Problema Anterior:** Falta de validación por parte de terceros.
*   **Decisión de Diseño:** Se incorporó un **carrusel interactivo de testimonios (Swipe/Scroll horizontal)**. 
*   **Impacto:** Leer a otros pacientes decir *"Me devolvieron la vida"* o *"Llegué sin poder caminar una cuadra"*, acompañado de valoraciones visuales de 5 estrellas, es el gatillo mental (Social Proof) más potente para convencer a un paciente indeciso de agendar una evaluación.

### 2.6. Captación B2B (Alianza Estratégica para Médicos)
*   **El Problema Anterior:** La clínica dependía de referidos, pero la web no le hablaba a los médicos que derivan.
*   **Decisión de Diseño:** Se creó una sección disruptiva orientada al 100% a profesionales (Broncopulmonares, Internistas, Otorrinos). 
*   **Feature:** Un bloque (Banner oscuro en V1 / Tarjeta clínica asimétrica en V2) que posiciona a Neumovital como una extensión del consultorio del médico, prometiendo "Reportes Clínicos" y "Trato Directo", finalizando con un botón de *"Adhiérete a Neumovital"*.

### 2.7. Cierre Persuasivo (Footer CTA & Floating Button)
*   **El Problema Anterior:** El agendamiento manual por WhatsApp generaba fricción operativa y pérdida de métricas.
*   **Decisión de Diseño:** Se rediseñó el final de la página con un bloque masivo de alto contraste: *"Es el momento de tomar el control"*.
*   **Feature:** Se reemplazó el botón de WhatsApp por un enlace directo al sistema de reservas (`/appointment-booking/`). Además, se programó un **Botón Flotante (Floating CTA)** que acompaña al usuario mientras hace scroll, asegurando que el botón de "Agendar" esté siempre a un clic de distancia en dispositivos móviles.

---

## 3. Lenguaje Visual (V1 vs. V2)

Para abarcar diferentes percepciones psicológicas del paciente, las funcionalidades anteriores se vistieron con dos trajes estéticos distintos:

*   **Versión 1 (Rigor Tecnológico y Confianza):** Utiliza formas geométricas sólidas, líneas rectas, modales estructurados y banners oscuros. El diseño proyecta estatus premium, ideal para transmitir rigor científico, precisión en exámenes y alta tecnología de laboratorio.
*   **Versión 2 (Flujo Orgánico y Cercanía Humana):** Incorpora bordes ultra redondeados masivos, botones con forma asimétrica (blobs), secciones en "zigzag" fluidas y sombras muy suaves. Todo el diseño "fluye" como el aire, transmitiendo una sensación subconsciente de alivio, cuidado humano, empatía y rehabilitación suave.
