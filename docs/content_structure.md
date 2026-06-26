# 📝 Estructura de Contenido

La página de inicio de Neumovital (Propuesta v1.1) está diseñada como una experiencia inmersiva "One-Page" o Landing Page extensa enfocada a la conversión.

## 1. Arquitectura de Secciones

1. **Hero Section (Portada):**
   - Slider de imágenes de fondo (recepción, entrada, equipamiento).
   - Texto principal llamativo con palabras clave coloreadas ("Rehabilitación Pulmonar").
   - Botón de "Escuchar Sección" (Texto a voz).
   - Componente "Glassmorphism" con convenio FONASA/ISAPRE y CTA (Call to Action) principal a la agendamiento.
   - Sello rotatorio decorativo "MÉTODO NEUMOVITAL".

2. **Marquee (Cinta pasante):**
   - Cinta morada con texto infinito en movimiento ("Evaluación Función Pulmonar", "Rehabilitación", etc.) para dar dinamismo.

3. **Sección de Servicios (Cards):**
   - Tarjetas grandes de servicios principales (Ej: Diagnóstico Respiratorio, Rehabilitación Pulmonar).

4. **Sección Orgánica (Fundadora / Clínica):**
   - Imagen con forma asimétrica (blob) animada.
   - Texto enfocado en los profesionales y la tecnología ("Tecnología y experiencia...").
   - Íconos sociales (Instagram, WhatsApp, Mail).

5. **Testimonios (Slider):**
   - Tarjetas deslizables horizontalmente (Scroll-snap).
   - Reseñas de pacientes con calificación en estrellas.

6. **Sección de Video ("Nuestro Centro"):**
   - Video de fondo ocupando el 100% del contenedor.
   - Overlay morado (Gradient) que contiene texto persuasivo.
   - Botón que abre un modal reproduciendo un video del centro.

7. **Sección de Instagram (Comunidad):**
   - Malla de videos (Reels) integrados.
   - Diseño limpio en fondo claro.

8. **Footer CTA:**
   - Llamado a la acción masivo final en morado oscuro.
   - Botón gigante de WhatsApp.

## 2. Gestión de Assets (Multimedia)

- **Imágenes de fondo:** Todas servidas desde el WordPress (`wp-content/uploads/2026/06/`).
- **Videos:** Servidos como `.mp4` para máxima compatibilidad y autoplay (ej: `centro-rehabilitacion-pulmonar-numovital.mp4`).
- **Iconos:** Basados en FontAwesome (`<i class="fa fa-..."></i>`).
