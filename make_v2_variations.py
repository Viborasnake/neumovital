import re

with open('propuestas/home/Propuesta-v2.txt', 'r') as f:
    text = f.read()

# 1. PATHOLOGIES PILLS (Organic Style)
old_pathologies = re.search(r'<div class="vg-pathologies".*?</div>\s*</div>', text, flags=re.DOTALL)
if old_pathologies:
    new_path = '''
<style>
.vg-pathologies-pill-v2 { background: #ffffff !important; color: #8f55a0 !important; border: none !important; font-size: 16px; font-weight: 800; padding: 18px 30px; border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; box-shadow: 0 15px 35px rgba(143, 85, 160, 0.08) !important; transition: 0.4s ease; display: inline-flex; align-items: center; gap: 12px; }
.vg-pathologies-pill-v2:hover { transform: translateY(-8px) scale(1.05); box-shadow: 0 25px 50px rgba(143, 85, 160, 0.15) !important; background: #8f55a0 !important; color: #ffffff !important; border-radius: 20px; }
.vg-pathologies-pill-v2 i { color: #46bfee !important; font-size: 22px; transition: 0.4s; }
.vg-pathologies-pill-v2:hover i { color: #ffffff !important; }
</style>
<div class="vg-pathologies" style="text-align:center; margin-top:100px; margin-bottom:80px;">
    <h3 style="font-size:26px; font-weight:900; color:#111 !important; margin-bottom:40px; letter-spacing:-1px;">Especialistas en la recuperación de:</h3>
    <div class="vg-pathologies-grid" style="display:flex; justify-content:center; flex-wrap:wrap; gap:20px; max-width:900px; margin:0 auto;">
        <span class="vg-pathologies-pill-v2"><i class="fa fa-lungs"></i> EPOC</span>
        <span class="vg-pathologies-pill-v2"><i class="fa fa-ribbon"></i> Cáncer de Pulmón</span>
        <span class="vg-pathologies-pill-v2"><i class="fa fa-wave-square"></i> Fibrosis Pulmonar</span>
        <span class="vg-pathologies-pill-v2"><i class="fa fa-bed"></i> Apnea del Sueño</span>
    </div>
</div>
'''
    text = text.replace(old_pathologies.group(0), new_path)

# 2. DOCTORS BANNER (Alianzas)
old_doctors = re.search(r'<section class="vg-doctors-banner".*?</section>', text, flags=re.DOTALL)
if old_doctors:
    new_docs = '''
<section class="vg-doctors-v2" style="padding:120px 5%; background-color:#ffffff;">
    <div style="max-width:1200px; margin:0 auto; background:#f8fbfc; border-radius:50px; box-shadow:0 30px 60px rgba(0,0,0,0.05); overflow:hidden; display:flex; flex-wrap:wrap; border: 1px solid rgba(143,85,160,0.1);">
        <div style="width:50%; padding:80px 60px; min-width:400px; box-sizing:border-box;">
            <div style="display:inline-block; padding:8px 20px; background:#e0f2fe; color:#46bfee; border-radius:50px; font-weight:800; font-size:14px; text-transform:uppercase; letter-spacing:1px; margin-bottom:25px;">Red de Derivación</div>
            <h2 style="font-size:clamp(35px, 4vw, 45px); font-weight:900; color:#111; margin-bottom:25px; line-height:1.1; letter-spacing:-1px;">Alianza Estratégica para <span style="color:#8f55a0;">Especialistas</span></h2>
            <p style="font-size:18px; color:#555; margin-bottom:40px; line-height:1.7;">Si eres Broncopulmonar, Otorrino o Internista, confía la rehabilitación funcional de tus pacientes a un equipo clínico de excelencia. Mantenemos comunicación directa sobre la evolución.</p>
            <div style="display:flex; gap:15px; margin-bottom:50px; flex-wrap:wrap;">
                <span style="background:#fff; padding:10px 20px; border-radius:15px; color:#8f55a0; font-weight:700; font-size:15px; box-shadow:0 10px 20px rgba(0,0,0,0.03);"><i class="fa fa-file-medical-alt" style="color:#46bfee; margin-right:8px;"></i> Reportes Clínicos</span>
                <span style="background:#fff; padding:10px 20px; border-radius:15px; color:#8f55a0; font-weight:700; font-size:15px; box-shadow:0 10px 20px rgba(0,0,0,0.03);"><i class="fa fa-handshake-o" style="color:#46bfee; margin-right:8px;"></i> Trato Directo</span>
            </div>
            <a href="#" class="vg-btn-primary" style="box-shadow:none !important; border-radius:100px;">Adhiérete a Neumovital <i class="fa fa-arrow-right"></i></a>
        </div>
        <div style="width:50%; min-width:400px; background-image:url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80'); background-size:cover; background-position:center; position:relative;">
             <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:linear-gradient(90deg, #f8fbfc 0%, transparent 30%);"></div>
        </div>
    </div>
</section>
'''
    text = text.replace(old_doctors.group(0), new_docs)

# 3. FOOTER CTA
old_footer = re.search(r'<section class="vg-footer-cta".*?</section>', text, flags=re.DOTALL)
if old_footer:
    new_foot = '''
<section class="vg-footer-v2" style="background:#8f55a0; padding:150px 5%; position:relative; overflow:hidden; text-align:center; border-radius: 80px 80px 0 0; margin-top:-40px; z-index:10; box-shadow: 0 -20px 50px rgba(0,0,0,0.1);">
    <div style="position:absolute; top:-100px; left:-50px; width:400px; height:400px; background:rgba(255,255,255,0.03); border-radius:40% 60% 70% 30% / 40% 50% 60% 50%; animation:organicShape 15s infinite;"></div>
    <div style="position:absolute; bottom:-150px; right:-100px; width:500px; height:500px; background:rgba(70,191,238,0.15); border-radius:70% 30% 50% 50% / 30% 30% 70% 70%; animation:organicShapeReverse 20s infinite;"></div>
    
    <div style="position:relative; z-index:10; max-width:850px; margin:0 auto;">
        <h2 style="font-size:clamp(45px, 6vw, 80px); font-weight:900; color:#ffffff; margin-bottom:30px; line-height:1.1; letter-spacing:-2px;">Es el momento de <span style="color:#e0f2fe; border-bottom: 4px solid #46bfee;">tomar el control</span>.</h2>
        <p style="font-size:24px; color:rgba(255,255,255,0.9); margin-bottom:60px; font-weight:300;">Tu salud pulmonar no puede esperar. Recupera tu calidad de vida en manos de especialistas.</p>
        <a href="https://neumovital.cl/appointment-booking/" class="vg-btn-white" style="font-size: 18px; padding: 22px 50px; border-radius: 100px;">
            <i class="fa fa-calendar-check-o" style="font-size: 24px; color:#46bfee;"></i> Reservar Hora
        </a>
    </div>
</section>
'''
    text = text.replace(old_footer.group(0), new_foot)

# 4. PRICE MODAL
old_modal = re.search(r'<div id="vg-price-modal".*?</div>\s*</div>\s*</div>\s*</div>', text, flags=re.DOTALL)
if old_modal:
    new_mod = '''
<style>
.vg-modal-box-v2 { background: #ffffff; border-radius: 40px; padding: 50px; max-width: 650px; width: 100%; position: relative; overflow: hidden; border-top: 10px solid #8f55a0; box-shadow: 0 30px 60px rgba(0,0,0,0.3); animation: vgModalPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; text-align: left; }
.vg-modal-box-v2::before { content: ''; position: absolute; top: -100px; right: -100px; width: 300px; height: 300px; background: rgba(70, 191, 238, 0.08); border-radius: 50%; z-index: 0; pointer-events:none; }
.vg-price-table-v2 { width: 100%; border-collapse: collapse; margin-top: 30px; position:relative; z-index:1; }
.vg-price-table-v2 th, .vg-price-table-v2 td { padding: 18px 20px; text-align: left; }
.vg-price-table-v2 th { background: rgba(143, 85, 160, 0.08); color: #8f55a0; font-weight: 900; text-transform: uppercase; font-size: 14px; letter-spacing:1px; }
.vg-price-table-v2 th:first-child { border-radius: 15px 0 0 0; }
.vg-price-table-v2 th:last-child { border-radius: 0 15px 0 0; }
.vg-price-table-v2 tr { border-bottom: 1px solid #f0f0f0; transition:0.3s; }
.vg-price-table-v2 tr:hover { background: #f8fbfc; }
.vg-price-table-v2 td { color: #444; font-size: 16px; font-weight:500; }
.vg-price-table-v2 td i { color:#46bfee; margin-right:8px; }
</style>
<div id="vg-price-modal" class="vg-modal-overlay">
    <div class="vg-modal-box-v2">
        <div class="vg-modal-close" onclick="document.getElementById('vg-price-modal').style.display='none'"><i class="fa fa-times-circle"></i></div>
        <div style="position:relative; z-index:1;">
            <h2 style="font-size:32px; font-weight:900; color:#111; margin-bottom:10px; letter-spacing:-1px;">Rangos de Precios</h2>
            <p style="color:#666; font-size:16px; margin-bottom:20px;">Conoce los copagos aproximados según tu sistema de salud.</p>
            <div style="overflow-x:auto;">
                <table class="vg-price-table-v2">
                    <tr><th>Servicio</th><th>Copago FONASA</th><th>Copago ISAPRE</th></tr>
                    <tr><td><i class="fa fa-lungs"></i> Rehabilitación Pulmonar</td><td>$6.500 - $12.000</td><td>$8.000 - $18.000</td></tr>
                    <tr><td><i class="fa fa-wind"></i> Espirometría Basal</td><td>$5.000 - $8.000</td><td>$7.000 - $15.000</td></tr>
                    <tr><td><i class="fa fa-bed"></i> Estudio de Sueño</td><td>$45.000 - $60.000</td><td>$50.000 - $85.000</td></tr>
                </table>
            </div>
            <p style="font-size:13px; color:#999; margin-top:25px; font-style:italic;"><i class="fa fa-info-circle"></i> * Valores meramente referenciales. El copago final dependerá del tramo de Fonasa o el plan específico de tu Isapre.</p>
        </div>
    </div>
</div>
'''
    text = text.replace(old_modal.group(0), new_mod)

with open('propuestas/home/Propuesta-v2.txt', 'w') as f:
    f.write(text)

