import os

with open("dashboard_proyecto.html", "r", encoding="utf-8") as f:
    html = f.read()

bad_chunk = """<button class="btn btn-outline" style="margin-bottom: 25px; width: 100%; justify-content: center; font-size: 15px; background: var(--bg-page); border: 1px dashed var(--border); cursor: pointer;" onclick="const g = document.getElementById('features-grid-collapsible'); const b = document.getElementById('toggle-features-text'); const i = document.getElementById('toggle-features-icon'); if(g.style.display==='none'){g.style.display='grid'; b.innerText='Ocultar funcionalidades'; i.style.transform='rotate(180deg)';}else{g.style.display='none'; b.innerText='Ver detalle de funcionalidades (9)'; i.style.transform='rotate(0deg)';}">
            <i class="fa-solid fa-layer-group" style="color: var(--primary);"></i> <span id="toggle-features-text" style="margin: 0 8px; font-weight: 700;">Ver detalle de funcionalidades (9)</span> <i id="toggle-features-icon" class="fa-solid fa-chevron-down" style="transition: transform 0.3s;"></i>
        </button>

        <div id="features-grid-collapsible" class="features-grid" style="display: none;">
            <div class="feature-item" style="position: relative;">
                <div style="position: absolute; top: 15px; right: 15px; color: #10b981; font-size: 18px;"><i class="fa-solid fa-circle-check"></i></div>

<div style="background: var(--bg-page); padding: 20px; border-radius: var(--radius-md); border: 1px dashed var(--border); margin-bottom: 20px;">
            <h4 style="font-size: 16px; margin-bottom: 10px; color: var(--primary);"><i class="fa-solid fa-wrench"></i> Ajustes aplicados en versión 1.1 (Feedback Cliente)</h4>
            <ul style="font-size: 14px; color: var(--text-muted); margin-left: 20px; line-height: 1.8;">
                <li><strong>Imágenes:</strong> Cambio de fotos genéricas por imágenes exclusivas de Daniela Díaz.</li>
                <li><strong>Identidad:</strong> Reemplazo del ícono de pulmón por la versión oficial proporcionada.</li>
                <li><strong>Autoridad:</strong> Corrección de título a "MSc Klga. DANIELA DIAZ HINOJOSA FUNDADORA NEUMOVITAL".</li>
                <li><strong>Contenido:</strong> Se ocultó/pausó (standby) la sección de "Nuestra especialidad y patologías".</li>
                <li><strong>Servicios:</strong> Imágenes de fondo estáticas más evidentes en tarjetas (ej. Pletismógrafo para diagnóstico).</li>
                <li><em>Fixes técnicos:</em> Ajuste de gradientes, centrado móvil y corrección de superposición de video.</li>
            </ul>
        </div>
                    </div>
                    <div class="rm-footer" style="display: flex; flex-direction: column; gap: 15px;">
<div class="action-links">
            <p style="width: 100%; font-size: 14px; font-weight: 700; color: var(--text-main); margin-bottom: 5px;">Versión Definitiva Aprobada:</p>
            <a href="https://neumovital.cl/propuesta-v1-1/" target="_blank" class="btn btn-primary" style="width: 100%; justify-content: center; font-size: 16px; padding: 16px;"><i class="fa-solid fa-rocket"></i> Ver Propuesta V1.1: Ajustes</a>
        </div>
<span style="font-size: 13px; font-weight: 600; color: #d97706;"><i class="fa-solid fa-spinner fa-spin"></i> Pendiente de Aprobación</span>
</div>"""


good_chunk = """<button class="btn btn-outline" style="margin-bottom: 25px; width: 100%; justify-content: center; font-size: 15px; background: var(--bg-page); border: 1px dashed var(--border); cursor: pointer;" onclick="const g = document.getElementById('features-grid-collapsible'); const b = document.getElementById('toggle-features-text'); const i = document.getElementById('toggle-features-icon'); if(g.style.display==='none'){g.style.display='grid'; b.innerText='Ocultar funcionalidades'; i.style.transform='rotate(180deg)';}else{g.style.display='none'; b.innerText='Ver detalle de funcionalidades (9)'; i.style.transform='rotate(0deg)';}">
                            <i class="fa-solid fa-layer-group" style="color: var(--primary);"></i> <span id="toggle-features-text" style="margin: 0 8px; font-weight: 700;">Ver detalle de funcionalidades (9)</span> <i id="toggle-features-icon" class="fa-solid fa-chevron-down" style="transition: transform 0.3s;"></i>
                        </button>

                        <div id="features-grid-collapsible" class="features-grid" style="display: none;">
                            <div class="feature-item" style="position: relative;">
                                <div style="position: absolute; top: 15px; right: 15px; color: #10b981; font-size: 18px;"><i class="fa-solid fa-circle-check"></i></div>
                                <div class="feat-title"><i class="fa-solid fa-bolt"></i> Hero & Cobertura</div>
                                <div class="feat-desc">Mensaje de alivio inmediato con botones y badges de FONASA/ISAPRE para derribar barreras de costo.</div>
                                <div class="feat-badge">Feature: <strong>Integración Badges</strong></div>
                            </div>
                            <div class="feature-item" style="position: relative;">
                                <div style="position: absolute; top: 15px; right: 15px; color: #10b981; font-size: 18px;"><i class="fa-solid fa-circle-check"></i></div>
                                <div class="feat-title"><i class="fa-solid fa-stethoscope"></i> Patologías Visibles</div>
                                <div class="feat-desc">Listado visual de alto impacto para que el paciente crónico se autoidentifique rápidamente.</div>
                                <div class="feat-badge">Feature: <strong>Pills Orgánicas</strong></div>
                            </div>
                            <div class="feature-item" style="position: relative;">
                                <div style="position: absolute; top: 15px; right: 15px; color: #10b981; font-size: 18px;"><i class="fa-solid fa-circle-check"></i></div>
                                <div class="feat-title"><i class="fa-solid fa-money-bill-wave"></i> Precios Ref.</div>
                                <div class="feat-desc">Reducción de incertidumbre mediante la publicación en tabla de copagos aprox de Fonasa e Isapre.</div>
                                <div class="feat-badge">Feature: <strong>Modal de Precios</strong></div>
                            </div>
                            <div class="feature-item" style="position: relative;">
                                <div style="position: absolute; top: 15px; right: 15px; color: #10b981; font-size: 18px;"><i class="fa-solid fa-circle-check"></i></div>
                                <div class="feat-title"><i class="fa-solid fa-award"></i> Authority Building</div>
                                <div class="feat-desc">Humanizar la marca mediante la trayectoria de su fundadora y el Método Neumovital.</div>
                                <div class="feat-badge">Feature: <strong>Sección Biográfica</strong></div>
                            </div>
                            <div class="feature-item" style="position: relative;">
                                <div style="position: absolute; top: 15px; right: 15px; color: #10b981; font-size: 18px;"><i class="fa-solid fa-circle-check"></i></div>
                                <div class="feat-title"><i class="fa-solid fa-handshake"></i> Captación B2B</div>
                                <div class="feat-desc">Posicionar a la clínica como una extensión de excelencia para médicos especialistas.</div>
                                <div class="feat-badge">Feature: <strong>Banner Derivadores</strong></div>
                            </div>
                            <div class="feature-item" style="position: relative;">
                                <div style="position: absolute; top: 15px; right: 15px; color: #10b981; font-size: 18px;"><i class="fa-solid fa-circle-check"></i></div>
                                <div class="feat-title"><i class="fa-solid fa-arrow-pointer"></i> Flujo de Cierre</div>
                                <div class="feat-desc">Estandarización del flujo hacia el software de reservas eliminando fricción.</div>
                                <div class="feat-badge">Feature: <strong>Floating CTA</strong></div>
                            </div>
                            <div class="feature-item" style="position: relative;">
                                <div style="position: absolute; top: 15px; right: 15px; color: #10b981; font-size: 18px;"><i class="fa-solid fa-circle-check"></i></div>
                                <div class="feat-title"><i class="fa-brands fa-instagram"></i> Integración RRSS</div>
                                <div class="feat-desc">Visibilizar el ecosistema digital mediante enlaces directos o integración con el Instagram de la clínica.</div>
                                <div class="feat-badge">Feature: <strong>Social Links</strong></div>
                            </div>
                            <div class="feature-item" style="position: relative;">
                                <div style="position: absolute; top: 15px; right: 15px; color: #10b981; font-size: 18px;"><i class="fa-solid fa-circle-check"></i></div>
                                <div class="feat-title"><i class="fa-solid fa-microchip"></i> Mejoras Tecnológicas</div>
                                <div class="feat-desc">Optimización de velocidad de carga, diseño responsive adaptable y SEO técnico on-page.</div>
                                <div class="feat-badge">Feature: <strong>Performance</strong></div>
                            </div>
                            <div class="feature-item" style="position: relative;">
                                <div style="position: absolute; top: 15px; right: 15px; color: #10b981; font-size: 18px;"><i class="fa-solid fa-circle-check"></i></div>
                                <div class="feat-title"><i class="fa-solid fa-layer-group"></i> Nuevas Secciones</div>
                                <div class="feat-desc">Implementación visual del Método Neumovital, carruseles de testimonios y validación social.</div>
                                <div class="feat-badge">Feature: <strong>Arquitectura UX</strong></div>
                            </div>
                        </div>

                        <div style="background: var(--bg-page); padding: 20px; border-radius: var(--radius-md); border: 1px dashed var(--border); margin-bottom: 20px;">
                            <h4 style="font-size: 16px; margin-bottom: 10px; color: var(--primary);"><i class="fa-solid fa-wrench"></i> Ajustes aplicados en versión 1.1 (Feedback Cliente)</h4>
                            <ul style="font-size: 14px; color: var(--text-muted); margin-left: 20px; line-height: 1.8;">
                                <li><strong>Imágenes:</strong> Cambio de fotos genéricas por imágenes exclusivas de Daniela Díaz.</li>
                                <li><strong>Identidad:</strong> Reemplazo del ícono de pulmón por la versión oficial proporcionada.</li>
                                <li><strong>Autoridad:</strong> Corrección de título a "MSc Klga. DANIELA DIAZ HINOJOSA FUNDADORA NEUMOVITAL".</li>
                                <li><strong>Contenido:</strong> Se ocultó/pausó (standby) la sección de "Nuestra especialidad y patologías".</li>
                                <li><strong>Servicios:</strong> Imágenes de fondo estáticas más evidentes en tarjetas (ej. Pletismógrafo para diagnóstico).</li>
                                <li><em>Fixes técnicos:</em> Ajuste de gradientes, centrado móvil y corrección de superposición de video.</li>
                            </ul>
                        </div>
                    </div>
                    <div class="rm-footer" style="display: flex; flex-direction: column; gap: 15px;">
                        <div class="action-links">
                            <p style="width: 100%; font-size: 14px; font-weight: 700; color: var(--text-main); margin-bottom: 5px;">Versión Definitiva Aprobada:</p>
                            <a href="https://neumovital.cl/propuesta-v1-1/" target="_blank" class="btn btn-primary" style="width: 100%; justify-content: center; font-size: 16px; padding: 16px;"><i class="fa-solid fa-rocket"></i> Ver Propuesta V1.1: Ajustes</a>
                        </div>
                        <span style="font-size: 13px; font-weight: 600; color: #d97706; align-self: flex-start;"><i class="fa-solid fa-spinner fa-spin"></i> Pendiente de Aprobación</span>
                    </div>"""

if bad_chunk in html:
    html = html.replace(bad_chunk, good_chunk)
    print("Replaced chunk perfectly.")
else:
    print("Error: Could not find exact chunk in html.")

with open("dashboard_proyecto.html", "w", encoding="utf-8") as f:
    f.write(html)
