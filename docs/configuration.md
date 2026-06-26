# ⚙️ Configuración y Entorno

## 1. Entorno Base

- **CMS:** WordPress.
- **Tema Activo:** Healthflex (Tema médico especializado).
- **Page Builder:** WPBakery Page Builder.

## 2. Ajustes Específicos (WPBakery)

Dado que se están utilizando bloques de Raw HTML (`[vc_column_text]`) dentro de WPBakery, aplican las siguientes reglas:

- **Estructura Row:** Los contenedores principales (`[vc_row]`) deben estar configurados como `stretch_row_content_no_spaces` para permitir que el diseño ocupe el 100% del ancho de la pantalla sin márgenes residuales.
- **Clases customizadas:** A los `[vc_row]` se les ha añadido una clase custom CSS `.vc_custom_vg_base` que inyecta `padding: 0 !important; margin: 0 !important;` para neutralizar el espaciado predeterminado del tema (que a veces inserta 64px o 128px de padding a los `<section>`).

## 3. Sobrescritura de Estilos del Tema

Para evitar conflictos con la hoja de estilos nativa (`style.min.css` de Healthflex), todo el código propio (prefijo `.vg-`) utiliza `!important` en reglas críticas:
- Márgenes de elementos de WPBakery (Ej. `.wpb_content_element { margin-bottom: 0 !important; }`).
- Prevención de desbordamientos (`overflow-x: hidden`).
- Cambios forzados a colores de fondo (`background-color: transparent !important;`).
