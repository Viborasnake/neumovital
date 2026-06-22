import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

# 1. New HTML for the Doctors Banner
new_doctors_html = """<section class="vg-doctors-banner" style="padding:100px 5%; background:linear-gradient(135deg, #150924 0%, #081221 100%) !important; color:#ffffff !important; display:flex; align-items:center; justify-content:center; position:relative; overflow:hidden;"><div style="position:absolute; top:-50%; left:-10%; width:500px; height:500px; background:radial-gradient(circle, rgba(143, 85, 160, 0.25) 0%, transparent 70%); border-radius:50%; z-index:0;"></div><div style="position:absolute; bottom:-50%; right:-10%; width:600px; height:600px; background:radial-gradient(circle, rgba(70, 191, 238, 0.15) 0%, transparent 70%); border-radius:50%; z-index:0;"></div><div class="vg-doctors-banner-content" style="display:flex; align-items:center; gap:60px; max-width:1200px; width:100%; position:relative; z-index:10;"><div class="vg-doctors-banner-text" style="flex:1; max-width:600px; text-align:left;"><div style="display:inline-block; padding:8px 18px; background:rgba(70, 191, 238, 0.15); border:1px solid rgba(70, 191, 238, 0.3); border-radius:50px; color:#46bfee; font-weight:800; font-size:13px; text-transform:uppercase; letter-spacing:1px; margin-bottom:25px;"><i class="fa fa-user-md" style="margin-right:8px;"></i> Programa de Derivación</div><h2 style="font-size:42px; font-weight:900; margin-bottom:25px; line-height:1.15; text-shadow:0 10px 30px rgba(0,0,0,0.5);">Alianza Estratégica para Especialistas</h2><p style="font-size:19px; color:#d0d0d0 !important; line-height:1.7; margin-bottom:0; font-weight:300;">Somos el centro solucionador aliado para <strong style="color:#fff; font-weight:600;">Broncopulmonares, Geriatras e Internistas</strong>. Aseguramos continuidad en la atención y resultados confiables para tus pacientes.</p></div><div class="vg-doctors-banner-box" style="background:rgba(255,255,255,0.08); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); padding:45px 40px; border-radius:30px; max-width:440px; border:1px solid rgba(255,255,255,0.15); box-shadow:0 30px 60px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.2); text-align:left; position:relative; overflow:hidden;"><div style="position:absolute; top:0; left:-100%; width:50%; height:100%; background:linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); transform:skewX(-20deg); animation:shineBox 8s infinite;"></div><h3 style="font-size:24px; font-weight:800; margin-bottom:20px; color:#ffffff !important; display:flex; align-items:center;"><i class="fa fa-shield" style="color:#25D366; font-size:28px; margin-right:15px; text-shadow:0 0 15px rgba(37,211,102,0.4);"></i> Cobertura Transparente</h3><p style="font-size:17px; color:#cccccc !important; line-height:1.7; margin-bottom:30px;">Atendemos de forma ágil y expedita a través de sistemas de salud tanto públicos como privados.</p><div style="display:flex; gap:15px; flex-wrap:wrap;"><span style="background:linear-gradient(135deg, #1d976c 0%, #93f9b9 100%); padding:10px 20px; border-radius:12px; color:#004d2a; font-weight:800; font-size:15px; box-shadow:0 10px 20px rgba(29, 151, 108, 0.3);"><i class="fa fa-check-circle" style="margin-right:5px;"></i> FONASA</span><span style="background:linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding:10px 20px; border-radius:12px; color:#003a66; font-weight:800; font-size:15px; box-shadow:0 10px 20px rgba(79, 172, 254, 0.3);"><i class="fa fa-check-circle" style="margin-right:5px;"></i> ISAPRE</span></div></div></div></section>"""

# Find the old section and replace it
docs_pattern = r'(<section class="vg-doctors-banner".*?</section>)'
text = re.sub(docs_pattern, new_doctors_html, text, flags=re.DOTALL)

# Add the shine animation to the CSS if it doesn't exist
if "@keyframes shineBox" not in text:
    animation_css = "@keyframes shineBox{0%{left:-100%;}20%{left:200%;}100%{left:200%;}}"
    text = text.replace("</style>", animation_css + "</style>")

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Doctors Banner updated successfully!")
