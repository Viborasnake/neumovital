# 🏗️ Arquitectura Técnica

Todo el diseño y lógica de las propuestas recientes se ha condensado en un único archivo de código mixto (HTML/CSS/JS) para que el cliente pueda copiarlo y pegarlo directamente en un bloque "HTML sin formato" o "Texto" dentro de WordPress.

## 1. Convención de Nomenclatura (BEM adaptado)

- Todas las clases CSS personalizadas inician con el prefijo `vg-` (Ej: `vg-hero`, `vg-btn`, `vg-glass-box`). Esto crea un "espacio de nombres" (namespace) seguro que garantiza cero colisiones con clases existentes de WordPress o WPBakery.

## 2. Bloque CSS (`<style>`)

- **Estructura en línea:** Todo el CSS se incluye al inicio del bloque dentro de etiquetas `<style>`.
- **Media Queries (Responsive):** 
  - `max-width: 1200px`: Adaptaciones a tablets horizontales.
  - `max-width: 900px`: Quiebre principal para tablets verticales y móviles. Centrado absoluto de los elementos del Hero, apilamiento de componentes.
  - `max-width: 600px`: Refinamiento para teléfonos (tamaños de fuente más pequeños, reducciones de padding).

## 3. Lógica JavaScript (`<script>`)

Se incluyen pequeños bloques de JavaScript al final del documento con funciones específicas:

- **Sistema Text-to-Speech (`vgPlayText`):**
  - Utiliza la Web Speech API (`window.speechSynthesis`).
  - Permite leer en voz alta fragmentos de texto (ej. el Hero).
  - Maneja estados de pausa/reproducción y limpia el texto para evitar que se lean caracteres raros.
- **Autoplay de Videos de Fondo:**
  - Script anónimo (IIFE) que crea dinámicamente un elemento `<video autoplay loop muted playsinline>` y lo inyecta dentro del contenedor del banner para saltarse las restricciones de bloqueo de autoplay de los navegadores (como Safari).
- **Sistema de Modales (Pop-ups):**
  - Inyección dinámica de etiquetas `<video>` dentro del modal solo cuando este se abre por primera vez, ahorrando ancho de banda al cargar la página inicialmente.
