# 🎨 Sistema de Diseño y Estilos

Este documento define la identidad visual de Neumovital en el entorno digital.

## 1. Paleta de Colores

El esquema de colores busca transmitir salud, tranquilidad, profesionalismo y tecnología médica.

- **Morado Principal (Brand):** `#8f55a0`
  - Uso: Botones primarios, iconos destacados, fondos de overlays.
- **Morado Oscuro (Footer/Dark):** `#683a78`
  - Uso: Footer, acentos profundos.
- **Azul Claro (Accent):** `#46bfee`
  - Uso: Textos destacados, insignias (badges), iconos secundarios.
- **Verde WhatsApp:** `#25D366`
  - Uso: Botones de contacto directo.
- **Naranja Oscuro (Highlight):** `#e6683c`
  - Uso: Títulos especiales (ej. Instagram).
- **Fondos Claros:** `#ffffff` (Blanco) y `#f8fbfc` (Gris/Azul muy claro).
- **Textos:** 
  - Oscuro principal: `#111111`
  - Párrafos grises: `#666666`, `#555555`
  - Párrafos sobre fondos oscuros: `#e0e0e0`, `#d0d0d0`

## 2. Tipografía

Se utiliza la familia tipográfica **Outfit** desde Google Fonts para garantizar un aspecto moderno y limpio.

- **Fuente principal:** `Outfit, sans-serif`
- **Pesos utilizados:** 
  - Ligero: `300` (Subtítulos y párrafos descriptivos)
  - Regular: `400` (Textos de lectura)
  - Semibold: `600` (Insignias, etiquetas)
  - Extrabold: `800` (Botones, títulos de tarjetas)
  - Black: `900` (Títulos principales "Hero")

## 3. Componentes UI (UI Kit)

### Botones (`.vg-btn`)
- Fondo morado con sombra difuminada.
- Efecto hover con `transform: translateY(-5px) scale(1.05)`.
- Variantes: 
  - `.vg-glass-btn`: Botón con gradiente de `#46bfee` a `#8f55a0` (usado en el Hero).
  - `.vg-btn-whatsapp`: Botón verde estándar de WhatsApp.

### Insignias / Etiquetas (`.vg-glass-badge`)
- Fondo semitransparente azul claro: `rgba(70,191,238,0.2)`.
- Borde sutil y texto `#46bfee`.
- Utilizadas para destacar categorías (ej. "Atención Premium").

### Cajas de Cristal (Glassmorphism) (`.vg-glass-box`)
- Fondo: `rgba(255,255,255,0.08)`.
- Efecto: `backdrop-filter: blur(20px)`.
- Sombras profundas e iluminaciones (shine/glow) animadas rotativas.
- Utilizadas en el Hero para destacar el llamado a la acción.

### Tarjetas de Servicios (`.vg-card`)
- Borde superior redondeado fuertemente (`40px`).
- Imagen de fondo en la mitad superior (`.vg-card::before`).
- Efecto hover: Se elevan (`translateY(-10px)`) y la imagen de fondo hace un sutil zoom in (`scale(1.05)`).
- Número de fondo grande y semitransparente en la esquina superior derecha (`.vg-card-num`).
