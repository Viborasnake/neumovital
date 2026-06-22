import re

# ==========================================
# COMMON SCRIPTS & CSS
# ==========================================
js = '''<script>
var vgAudioPlaying = false;var vgCurrentBtn = null;function vgPlayText(textId, btnElement){if ('speechSynthesis' in window){if (vgAudioPlaying && vgCurrentBtn === btnElement){window.speechSynthesis.pause();            btnElement.innerHTML = '<i class="fa fa-play"></i> Escuchar Sección';btnElement.classList.remove('playing');vgAudioPlaying = false;vgCurrentBtn = null;return;}window.speechSynthesis.cancel();if (vgCurrentBtn && vgCurrentBtn !== btnElement){vgCurrentBtn.innerHTML = '<i class="fa fa-play"></i> Escuchar Sección';vgCurrentBtn.classList.remove('playing');}var textContainer = document.getElementById(textId);if (!textContainer) return;var text = textContainer.innerText || textContainer.textContent;text = text.replace(/[—\-_|]/g, '. ');text = text.replace(/[®"']/g, '');text = text.replace(/\n+/g, '. ');text = text.replace(/\s+/g, ' ');var msg = new SpeechSynthesisUtterance();msg.text = text;msg.lang = 'es-CL';msg.rate = 0.95;msg.pitch = 1;btnElement.innerHTML = '<i class="fa fa-pause"></i> Pausar Audio';btnElement.classList.add('playing');vgAudioPlaying = true;vgCurrentBtn = btnElement;msg.onend = function(){if (vgCurrentBtn === btnElement){btnElement.innerHTML = '<i class="fa fa-play"></i> Escuchar Sección';btnElement.classList.remove('playing');vgAudioPlaying = false;vgCurrentBtn = null;}};msg.onerror = function(){if (vgCurrentBtn === btnElement){btnElement.innerHTML = '<i class="fa fa-play"></i> Escuchar Sección';btnElement.classList.remove('playing');vgAudioPlaying = false;vgCurrentBtn = null;}};window.speechSynthesis.speak(msg);}else{alert("Lo sentimos, tu navegador actual no soporta lectura por voz.");}}

window.addEventListener("scroll", function() {
    var cta = document.querySelector(".vg-floating-cta");
    if(cta) {
        var scrollY = window.scrollY || window.pageYOffset;
        if(scrollY > 300) {
            cta.classList.add("show-cta");
        } else {
            cta.classList.remove("show-cta");
        }
    }
});
</script>'''

wrapper_start = '[vc_row color_set="light_section" full_width="stretch_row_content_no_spaces" css=".vc_custom_vg_base{background-color:#ffffff !important;padding:0 !important;margin:0 !important;}"][vc_column][vc_column_text]'
wrapper_end = '[/vc_column_text][/vc_column][/vc_row]'
floating_cta_html = '<a href="#agendar" class="vg-floating-cta"><i class="fa fa-calendar-check-o"></i> <span>Agendar Hora</span></a>'

# ==========================================
# V1 CONTENT
# ==========================================
css_v1 = '''<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800;900&display=swap');
.vg-wrapper{font-family:'Outfit', sans-serif !important;overflow-x:hidden;background-color:#ffffff !important;position:relative;z-index:auto;width:100vw;left:50%;right:50%;margin-left:-50vw;margin-right:-50vw;}
.vg-play-btn{align-self:flex-start;max-width:350px;width:max-content;background-color:#ffffff !important;border:1px solid #d0d0d0 !important;color:#8f55a0 !important;padding:10px 24px;border-radius:50px !important;font-size:12px;font-weight:800;cursor:pointer;transition:0.3s;display:inline-flex;align-items:center;justify-content:center;gap:8px;outline:none;margin-bottom:25px;text-transform:uppercase;letter-spacing:1px;font-family:'Outfit', sans-serif !important;box-shadow:0 5px 15px rgba(0,0,0,0.05) !important;}
.vg-play-btn:hover{background-color:#8f55a0 !important;color:#fff !important;border-color:#8f55a0 !important;transform:translateY(-2px);}
.vg-play-btn.playing{background-color:#ff4757 !important;color:#fff !important;border-color:#ff4757 !important;animation:pulseRed 1.5s infinite;}
@keyframes pulseRed{0%{box-shadow:0 0 0 0 rgba(255, 71, 87, 0.4);}70%{box-shadow:0 0 0 15px rgba(255, 71, 87, 0);}100%{box-shadow:0 0 0 0 rgba(255, 71, 87, 0);}}
.vg-hero{position:relative;padding:180px 5%;background-color:transparent !important;overflow:hidden !important;display:flex;align-items:center;justify-content:center;}
.vg-slider-bg{position:absolute;top:0;left:0;width:100%;height:100%;background-size:cover;background-position:center center;z-index:0;opacity:0;animation:fadeSlider 18s infinite;}
.bg-img-1{background-image:url('https://neumovital.cl/wp-content/uploads/2025/07/15A1197_pp-scaled.jpg');animation-delay:0s;}
.bg-img-2{background-image:url('https://neumovital.cl/wp-content/uploads/2025/07/20250626_132653-scaled.jpg');animation-delay:6s;}
.bg-img-3{background-image:url('https://neumovital.cl/wp-content/uploads/2025/07/20250626_133426-1-scaled.jpg');animation-delay:12s;}
@keyframes fadeSlider{0%{opacity:0;transform:scale(1);}10%{opacity:1;}33.33%{opacity:1;}43.33%{opacity:0;transform:scale(1.05);}100%{opacity:0;}}
.vg-overlay-dark{position:absolute;top:0;left:0;width:100%;height:100%;background:linear-gradient(135deg, rgba(60, 30, 90, 0.85) 0%, rgba(20, 60, 100, 0.6) 100%);z-index:1;}
.vg-bg-text{position:absolute;top:50%;left:50%;transform:translate(-50%, -50%);font-size:25vw;font-weight:900;color:rgba(255, 255, 255, 0.04) !important;z-index:2;line-height:1;white-space:nowrap;pointer-events:none;}
.vg-hero-content{position:relative;z-index:10;width:100%;max-width:1200px;margin:0 auto;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;}
.vg-title{font-size:clamp(45px, 5.5vw, 80px);font-weight:900;color:#ffffff !important;line-height:1.1;margin-bottom:20px;letter-spacing:-2px;text-align:left;}
.vg-title span{color:#e0f2fe !important;}
.vg-subtitle{font-size:22px;font-weight:300;color:#e0e0e0 !important;line-height:1.6;margin-bottom:40px;text-align:left;}
.vg-hero-quote{display:flex;align-items:center;margin-bottom:40px;}
.vg-quote-avatar{width:70px;height:70px;border-radius:50%;object-fit:cover;margin-right:20px;border:2px solid #46bfee !important;box-shadow:0 5px 15px rgba(0,0,0,0.3) !important;flex-shrink:0;}
.vg-quote-text{display:flex;flex-direction:column;text-align:left;}
.vg-hero-quote .vg-subtitle{margin-bottom:5px;font-style:italic;font-weight:400;color:#ffffff !important;}
.vg-quote-author{font-size:13px;color:#46bfee !important;font-weight:700;text-transform:uppercase;letter-spacing:1px;}
.vg-btn{background-color:#8f55a0 !important;color:#ffffff !important;padding:18px 40px;border-radius:50px;font-size:16px;font-weight:800;text-transform:uppercase;letter-spacing:1px;text-decoration:none;display:inline-block;transition:all 0.4s ease;box-shadow:0 15px 30px rgba(143, 85, 160, 0.3) !important;}
.vg-btn:hover{transform:translateY(-5px) scale(1.05);box-shadow:0 25px 40px rgba(143, 85, 160, 0.5) !important;color:#ffffff !important;}
.vg-glass-box{background-color:rgba(255, 255, 255, 0.08) !important;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.2) !important;border-radius:30px;padding:50px 40px;max-width:450px;box-shadow:0 30px 60px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.4) !important;text-align:left;margin-top:0;position:relative;overflow:hidden;}
.vg-glass-box::before{content:"";position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);animation:rotateGlow 10s linear infinite;pointer-events:none;}
@keyframes rotateGlow{0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}
.vg-glass-badge{display:inline-block;padding:6px 15px;background:rgba(70, 191, 238, 0.2) !important;color:#46bfee !important;border-radius:50px;font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:1px;margin-bottom:25px;border:1px solid rgba(70, 191, 238, 0.3) !important;}
.vg-glass-title{color:#ffffff !important;font-size:28px;font-weight:800;line-height:1.2;margin-bottom:15px;}
.vg-glass-desc{color:#d0d0d0 !important;font-size:17px;line-height:1.6;margin-bottom:30px;}
.vg-glass-pills{display:flex;gap:15px;}
.vg-pill{background:rgba(255,255,255,0.05) !important;border:1px solid rgba(255,255,255,0.15) !important;padding:8px 18px;border-radius:12px;color:#ffffff !important;font-size:14px;font-weight:600;display:flex;align-items:center;gap:8px;}
.vg-pill i{color:#25D366 !important;}
.vg-glass-btn{display:flex;justify-content:space-between;align-items:center;width:100%;background-image:linear-gradient(135deg, #46bfee 0%, #8f55a0 100%) !important;color:#ffffff !important;padding:18px 30px;border-radius:20px;font-size:16px;font-weight:800;text-transform:uppercase;letter-spacing:1px;text-decoration:none;transition:all 0.4s ease;box-shadow:0 15px 30px rgba(143, 85, 160, 0.3) !important;box-sizing:border-box;}
.vg-glass-btn:hover{transform:translateY(-5px);box-shadow:0 25px 40px rgba(143, 85, 160, 0.5) !important;color:#ffffff !important;}
.vg-glass-btn i{background:rgba(255,255,255,0.2);width:35px;height:35px;display:flex;align-items:center;justify-content:center;border-radius:50%;}
.vg-marquee-container{width:100%;overflow:hidden !important;background-color:#8f55a0 !important;padding:25px 0;position:relative;z-index:20;margin-top:0px;box-shadow:0 10px 30px rgba(0,0,0,0.1) !important;}
.vg-marquee{display:flex;width:fit-content;animation:marqueeScroll 25s linear infinite;}
.vg-marquee span{font-size:22px;font-weight:800;color:#ffffff !important;text-transform:uppercase;letter-spacing:2px;padding:0 40px;white-space:nowrap;}
.vg-marquee span i{color:#46bfee !important;margin-right:15px;}
.vg-icon-top{height:140px;width:auto;margin-bottom:-15px;display:block;opacity:0.9;}
@keyframes marqueeScroll{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}
.vg-services{padding:120px 5%;max-width:1300px;margin:0 auto;background-color:#ffffff !important;overflow:hidden !important;}
.vg-section-header{text-align:center;margin-bottom:80px;}
.vg-section-header h2{font-size:50px;font-weight:900;color:#111111 !important;letter-spacing:-1px;}
.vg-cards-grid{display:grid;grid-template-columns:repeat(auto-fit, minmax(350px, 1fr));gap:40px;}
.vg-card{background-color:#ffffff !important;border-radius:40px;padding:60px 40px;box-shadow:0 20px 50px rgba(0,0,0,0.04) !important;border:1px solid #f0f0f0 !important;position:relative;overflow:hidden !important;z-index:1;transition:all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);display:flex;flex-direction:column;}
.vg-card::after{content:"";position:absolute;top:0;left:0;width:100%;height:100%;background-image:linear-gradient(135deg, #46bfee 0%, #8f55a0 100%) !important;opacity:0;z-index:-1;transition:all 0.6s ease;}
.vg-card:hover{transform:translateY(-20px);box-shadow:0 40px 70px rgba(143, 85, 160, 0.2) !important;border-color:transparent !important;}
.vg-card:hover::after{opacity:1;}
.vg-card-num{font-size:150px;font-weight:900;color:rgba(0,0,0,0.03) !important;position:absolute;top:-20px;right:20px;line-height:1;transition:0.6s ease;}
.vg-card:hover .vg-card-num{color:rgba(255,255,255,0.1) !important;}
.vg-card h3{font-size:34px;font-weight:800;color:#111111 !important;margin-bottom:20px;position:relative;transition:0.6s ease;}
.vg-card p{font-size:18px;color:#666666 !important;line-height:1.7;margin-bottom:30px;transition:0.6s ease;flex:1;}
.vg-card:hover h3, .vg-card:hover p{color:#ffffff !important;}
.vg-card-link{display:inline-flex;align-items:center;justify-content:center;width:60px;height:60px;border-radius:50%;background-color:#f4f7f6 !important;color:#111111 !important;font-size:20px;text-decoration:none;transition:0.4s ease;}
.vg-card:hover .vg-card-link{background-color:#ffffff !important;color:#8f55a0 !important;transform:scale(1.1) rotate(-45deg);}
.vg-btn-outline-dark{border:2px solid #e0e0e0 !important;color:#555555 !important;padding:12px 25px;border-radius:8px;font-size:15px;font-weight:700;text-transform:uppercase;letter-spacing:1px;text-decoration:none;display:inline-block;transition:all 0.3s ease;text-align:center;}
.vg-card:hover .vg-btn-outline-dark{border-color:#ffffff !important; color:#ffffff !important;}
.vg-organic{padding:100px 5% 100px 5%;background-color:#f8fbfc !important;display:flex;flex-direction:column;align-items:center;overflow:hidden !important;}
.vg-organic-inner{max-width:1300px;width:100%;display:flex;flex-wrap:wrap;align-items:center;}
.vg-organic-img{width:45%;position:relative;}
.vg-organic-img img{width:100%;border-radius:40% 60% 70% 30% / 40% 50% 60% 50%;box-shadow:20px 20px 60px rgba(70,191,238,0.2) !important;animation:blobMorph 10s ease-in-out infinite alternate;object-fit:cover;aspect-ratio:4/5;}
@keyframes blobMorph{0%{border-radius:40% 60% 70% 30% / 40% 50% 60% 50%;}100%{border-radius:60% 40% 30% 70% / 60% 30% 70% 40%;}}
.vg-organic-text{width:50%;padding-left:5%;display:flex;flex-direction:column;}
.vg-organic-text h4{color:#8f55a0 !important;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:10px;}
.vg-organic-text h2{font-size:50px;font-weight:900;line-height:1.1;color:#111111 !important;margin-bottom:30px;}
.vg-founder-actions{display:flex;align-items:center;gap:20px;flex-wrap:wrap;}
.vg-social-icons{display:flex;gap:15px;}
.vg-social-icons a{display:flex;justify-content:center;align-items:center;width:45px;height:45px;border-radius:50%;background-color:rgba(143, 85, 160, 0.1) !important;color:#8f55a0 !important;font-size:20px;text-decoration:none;transition:all 0.3s ease;}
.vg-social-icons a:hover{background-color:#8f55a0 !important;color:#ffffff !important;transform:translateY(-5px);box-shadow:0 10px 20px rgba(143, 85, 160, 0.3) !important;}
.vg-instagram{padding:100px 2% 150px 2%;background-color:#ffffff !important;display:flex;align-items:center;justify-content:center;}
.vg-ig-inner{max-width:1500px;width:100%;display:flex;flex-direction:column;align-items:center;background:#f8fbfc !important;border-radius:40px;padding:60px 30px;box-shadow:0 20px 50px rgba(0,0,0,0.03) !important;border:1px solid rgba(70,191,238,0.1) !important;}
.vg-ig-text{width:100%;text-align:center;margin-bottom:50px;}
.vg-ig-text h4{color:#e6683c !important;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:15px;display:flex;align-items:center;justify-content:center;gap:10px;}
.vg-ig-text h4 i{font-size:24px;}
.vg-ig-text h2{font-size:45px;font-weight:900;line-height:1.1;color:#111111 !important;margin-bottom:25px;}
.vg-ig-text p{font-size:18px;color:#666666 !important;line-height:1.7;margin-bottom:40px;max-width:800px;margin-left:auto;margin-right:auto;}
.vg-ig-videos-grid{display:grid;grid-template-columns:repeat(4, 1fr);gap:20px;width:100%;justify-items:center;}
.vg-ig-videos-grid iframe{width:100%;max-width:100%;height:500px;border-radius:12px;box-shadow:0 15px 35px rgba(0,0,0,0.1) !important;background:#ffffff;}
.vg-footer-cta{background:linear-gradient(135deg, #8f55a0 0%, #46bfee 100%) !important;padding:120px 5%;text-align:center;position:relative;overflow:hidden !important;}
.vg-footer-content{position:relative;z-index:10;}
.vg-footer-content h2{font-size:clamp(40px, 5vw, 70px);font-weight:900;color:#ffffff !important;margin-bottom:40px;letter-spacing:-2px;}
.vg-btn-whatsapp{background-color:#25D366 !important;color:#ffffff !important;padding:20px 45px;border-radius:100px;font-size:18px;font-weight:900;text-decoration:none;display:inline-flex;align-items:center;box-shadow:0 20px 50px rgba(37, 211, 102, 0.4) !important;transition:0.4s ease;border:2px solid transparent !important;}
.vg-btn-whatsapp i{font-size:28px;margin-right:15px;}
.vg-btn-whatsapp:hover{transform:translateY(-10px);box-shadow:0 30px 60px rgba(37, 211, 102, 0.6) !important;color:#25D366 !important;background-color:#ffffff !important;border:2px solid #ffffff !important;}
.vg-whatsapp-text{color:rgba(255,255,255,0.8) !important;margin-top:30px;font-size:16px;font-weight:600;}
.vg-stamp-wrapper{position:relative;z-index:10;}
.vg-stamp{position:absolute;top:-60px;right:-60px;width:150px;height:150px;z-index:20;display:flex;align-items:center;justify-content:center;pointer-events:none;background:rgba(143, 85, 160, 0.15) !important;border-radius:50%;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.2) !important;box-shadow:0 15px 35px rgba(0,0,0,0.2) !important;}
.vg-stamp-svg{position:absolute;top:0;left:0;width:100%;height:100%;animation:rotateStamp 60s linear infinite;}
@keyframes rotateStamp{0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}
.vg-stamp-icon{font-size:35px;color:#46bfee !important;text-shadow:0 0 15px rgba(70, 191, 238, 0.4) !important;}
.vg-floating-cta{position:fixed;bottom:30px;left:30px;background-color:#8f55a0 !important;color:#fff !important;padding:16px 30px;border-radius:50px;font-weight:800;font-size:16px;box-shadow:0 10px 30px rgba(143, 85, 160, 0.4) !important;z-index:9999;display:flex;align-items:center;gap:12px;text-decoration:none;text-transform:uppercase;letter-spacing:1px;transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);opacity:0;visibility:hidden;transform:translateY(30px) scale(0.8);pointer-events:none;}
.vg-floating-cta.show-cta{opacity:1;visibility:visible;transform:translateY(0) scale(1);pointer-events:auto;animation:attentionWobble 3.5s infinite 1s;}
.vg-floating-cta:hover{transform:translateY(-5px) scale(1.05) !important;box-shadow:0 15px 40px rgba(143, 85, 160, 0.6) !important;color:#fff !important;background-color:#7a468a !important;animation:none !important;}
.vg-floating-cta i{font-size:20px;}
@keyframes attentionWobble{0%{transform:rotate(0deg) scale(1);box-shadow:0 0 0 0 rgba(143,85,160,0.7);}5%{transform:rotate(-15deg) scale(1.15);box-shadow:0 0 0 15px rgba(143,85,160,0);}10%{transform:rotate(15deg) scale(1.15);}15%{transform:rotate(-15deg) scale(1.15);}20%{transform:rotate(15deg) scale(1.15);}25%{transform:rotate(0deg) scale(1);box-shadow:0 0 0 0 rgba(143,85,160,0);}100%{transform:rotate(0deg) scale(1);}}
/* --- V1 RESPONSIVE FIXES --- */
@media (max-width:1200px){
.vg-ig-videos-grid{grid-template-columns:repeat(2, 1fr);}
}
@media (max-width:900px){
.vg-organic-img, .vg-organic-text{width:100%;padding:0;display:flex;flex-direction:column;align-items:center;text-align:center;}
.vg-organic-img{margin-bottom:50px;}
.vg-hero-content{flex-direction:column;text-align:center;}
.vg-title{font-size:55px;text-align:center;}
.vg-subtitle{text-align:center;margin-left:auto;margin-right:auto;}
.vg-quote-text{text-align:center;}
.vg-hero-quote{justify-content:center; flex-direction:column; gap:15px; margin-left:auto; margin-right:auto;}
.vg-quote-avatar{margin-right:0 !important; margin-bottom:10px !important;}
.vg-glass-box{margin-top:40px; margin-left:auto; margin-right:auto;text-align:center;display:flex;flex-direction:column;align-items:center;}
.vg-glass-pills{justify-content:center;}
.vg-ig-inner{padding:40px 20px;}
.vg-ig-text{margin-bottom:40px;}
.vg-founder-actions{justify-content:center;}
.vg-play-btn{margin-left:auto; margin-right:auto; margin-bottom:30px;}
.vg-stamp{display:none !important;}
.vg-icon-top{margin-left:auto; margin-right:auto;}
.vg-pathologies .vg-pill { margin-bottom:10px; }
.vg-doctors-banner { text-align:center; flex-direction:column; }
.vg-doctors-banner > div { width:100%; max-width:100% !important; }
}
@media (max-width:600px){
.vg-hero{padding:100px 5% 80px !important;}
.vg-title{font-size:38px !important; margin-bottom:15px;}
.vg-subtitle{font-size:18px !important; margin-bottom:30px;}
.vg-floating-cta{bottom:20px;left:20px;padding:16px;border-radius:50%;}
.vg-floating-cta span{display:none;}
.vg-floating-cta i{font-size:24px;margin:0;}
.vg-ig-videos-grid{grid-template-columns:1fr;}
.vg-glass-box{padding:30px 20px !important; width:100%;}
.vg-glass-title{font-size:24px !important;}
.vg-glass-desc{font-size:16px !important;}
.vg-glass-btn{padding:15px 20px !important; font-size:14px !important;}
.vg-pill{font-size:12px !important; padding:6px 12px !important;}
.vg-section-header h2{font-size:36px !important;}
.vg-footer-content h2{font-size:36px !important;}
.vg-btn-whatsapp{padding:15px 30px !important; font-size:16px !important;width:100%;justify-content:center;}
.vg-btn-whatsapp i{font-size:24px !important;}
.vg-organic-text h2{font-size:36px !important;}
.vg-cards-grid{grid-template-columns:1fr;}
}
</style>
'''

html_v1 = '''<div class="vg-wrapper">
<section class="vg-hero">
<div class="vg-slider-bg bg-img-1">&nbsp;</div>
<div class="vg-slider-bg bg-img-2">&nbsp;</div>
<div class="vg-slider-bg bg-img-3">&nbsp;</div>
<div class="vg-overlay-dark">&nbsp;</div>
<div class="vg-bg-text">RESPIRA</div>
<div class="vg-hero-content">
<div style="flex:1;min-width:300px;padding-right:5%;text-align:left;position:relative;display:flex;flex-direction:column;"><button class="vg-play-btn" onclick="vgPlayText('text-hero-v1', this)"><i class="fa fa-play"></i> Escuchar Sección</button>
<div id="text-hero-v1"><img decoding="async" src="https://neumovital.cl/wp-content/uploads/2026/06/neumotival-pulmon.png" class="vg-icon-top" alt="Neumovital">
<h1 class="vg-title">Vuelve a <span>respirar</span>,<br />vuelve a <span>vivir</span>.</h1>
<div class="vg-hero-quote"><img decoding="async" src="https://neumovital.cl/wp-content/uploads/2025/06/IMG_6607_SnapseedCopy-scaled.jpeg" class="vg-quote-avatar" alt="Daniela Díaz Hinojosa">
<div class="vg-quote-text">
<p class="vg-subtitle">&#8220;No asumas que el cansancio es irreversible.&#8221;</p>
<p><span class="vg-quote-author">Dra. Daniela Díaz H. Fundadora Método Neumovital&reg;</span></div>
</div>
</div>
</div>
<div class="vg-stamp-wrapper" style="position:relative;z-index:10;">
<div class="vg-glass-box">
<div id="text-glass-v1" style="margin-bottom: 40px;">
<div class="vg-glass-badge"><i class="fa fa-stethoscope"></i> Atención Premium</div>
<h3 class="vg-glass-title">Tu salud pulmonar en manos expertas</h3>
<p class="vg-glass-desc">Clínica especializada en Rehabilitación y Diagnóstico. Evaluamos tu capacidad y te ayudamos a recuperarla.</p>
<div class="vg-glass-pills">
<div class="vg-pill"><i class="fa fa-check-circle"></i> Fonasa</div>
<div class="vg-pill"><i class="fa fa-check-circle"></i> Isapre</div>
</div>
</div>
<a href="#agendar" class="vg-glass-btn">Agendar Evaluación <i class="fa fa-chevron-right"></i></a></div>
<div class="vg-stamp">
<svg class="vg-stamp-svg" viewBox="0 0 100 100" width="100" height="100">
<path id="curve" fill="transparent" d="M 50,50 m -35,0 a 35,35 0 1,1 70,0 a 35,35 0 1,1 -70,0"></path>
<text width="100" style="font-size:12px; font-weight:800; letter-spacing:3px; fill:#ffffff; text-transform:uppercase;"><textPath href="#curve" startOffset="0%">&bull; Método Neumovital &bull; Método Neumovital </textPath></text>
</svg>
<i class="fa fa-asterisk vg-stamp-icon"></i></div>
</div>
</div>
</section>
<div class="vg-marquee-container">
<div class="vg-marquee"><span><i class="fa fa-check"></i> Espirometría</span><span><i class="fa fa-check"></i> Difusión de Monóxido (DLCO)</span><span><i class="fa fa-check"></i> Volúmenes Pulmonares</span><span><i class="fa fa-check"></i> Presiones Máximas (PIM/PEM)</span><span><i class="fa fa-check"></i> Test de Marcha 6 Minutos</span><span><i class="fa fa-check"></i> Poligrafía del Sueño</span><span><i class="fa fa-check"></i> Rehabilitación Respiratoria</span><span><i class="fa fa-check"></i> Entrenamiento Muscular</span><span><i class="fa fa-check"></i> Espirometría</span><span><i class="fa fa-check"></i> Difusión de Monóxido (DLCO)</span></div>
</div>
<section class="vg-services">
<div class="vg-section-header">
<h2>Nuestras Especialidades</h2>
</div>
<div class="vg-pathologies" style="text-align:center; margin-bottom:80px;">
    <h3 style="font-size:24px; font-weight:800; color:#8f55a0 !important; margin-bottom:20px;">Patologías que Atendemos</h3>
    <div class="vg-glass-pills" style="justify-content:center; flex-wrap:wrap; gap:10px;">
        <div class="vg-pill" style="background:#f0f4f8 !important; color:#333 !important; border:none !important;"><i class="fa fa-lungs" style="color:#46bfee !important;"></i> EPOC</div>
        <div class="vg-pill" style="background:#f0f4f8 !important; color:#333 !important; border:none !important;"><i class="fa fa-ribbon" style="color:#46bfee !important;"></i> Cáncer de Pulmón</div>
        <div class="vg-pill" style="background:#f0f4f8 !important; color:#333 !important; border:none !important;"><i class="fa fa-wave-square" style="color:#46bfee !important;"></i> Fibrosis Pulmonar</div>
        <div class="vg-pill" style="background:#f0f4f8 !important; color:#333 !important; border:none !important;"><i class="fa fa-bed" style="color:#46bfee !important;"></i> Apnea del Sueño</div>
        <div class="vg-pill" style="background:#f0f4f8 !important; color:#333 !important; border:none !important;"><i class="fa fa-virus" style="color:#46bfee !important;"></i> Secuelas Respiratorias</div>
    </div>
</div>
<div class="vg-cards-grid">
<div class="vg-card">
<div class="vg-card-num">01</div>
<h3 style="color:#8f55a0 !important;">Rehabilitación Pulmonar</h3>
<p>El corazón de nuestro centro. Recupera tu tolerancia al esfuerzo y vuelve a tus actividades diarias con nuestro programa de entrenamiento supervisado.</p>
<div style="margin-top:auto; display:flex; flex-direction:column; gap:15px; align-items:flex-start;">
    <a href="#" class="vg-btn-outline-dark">Rangos de Precios</a>
    <a href="#" class="vg-card-link" style="align-self:flex-end;"><i class="fa fa-arrow-right"></i></a>
</div>
</div>
<div class="vg-card">
<div class="vg-card-num">02</div>
<h3>Laboratorio de Función Pulmonar</h3>
<p>Evaluación exacta con pletismógrafo de última generación (Espirometrías, DLCO y Volúmenes Pulmonares) para diagnósticos precisos en reposo.</p>
<div style="margin-top:auto; display:flex; flex-direction:column; gap:15px; align-items:flex-start;">
    <a href="#" class="vg-btn-outline-dark">Rangos de Precios</a>
    <a href="#" class="vg-card-link" style="align-self:flex-end;"><i class="fa fa-arrow-right"></i></a>
</div>
</div>
<div class="vg-card">
<div class="vg-card-num">03</div>
<h3>Estudio de Sueño (Poligrafía)</h3>
<p>Monitoreo avanzado en la comodidad de tu hogar para detectar apnea del sueño y trastornos respiratorios nocturnos.</p>
<div style="margin-top:auto; display:flex; flex-direction:column; gap:15px; align-items:flex-start;">
    <a href="#" class="vg-btn-outline-dark">Rangos de Precios</a>
    <a href="#" class="vg-card-link" style="align-self:flex-end;"><i class="fa fa-arrow-right"></i></a>
</div>
</div>
</div>
</section>
<section class="vg-organic">
<div class="vg-organic-inner">
<div class="vg-organic-img"><img decoding="async" src="https://neumovital.cl/wp-content/uploads/2025/07/20250626_132653-scaled.jpg" alt="Daniela Díaz"></div>
<div class="vg-organic-text">
<h4>La Fundadora</h4>
<h2>Daniela Díaz Hinojosa</h2>
<p style="font-size:20px; color:#555; line-height:1.7; margin-bottom:20px;">Kinesióloga Especialista en Rehabilitación Respiratoria (DENAKE) y creadora del <strong>Método Neumovital&reg;</strong>.</p>
<p style="font-size:18px; color:#555; line-height:1.7; margin-bottom:30px; font-style:italic; border-left:4px solid #46bfee; padding-left:20px;">"Mi promesa y compromiso es acompañar a pacientes y familias a recuperar su autonomía, guiados siempre bajo la filosofía del buen vivir y el buen morir."</p>
<ul style="list-style:none; padding:0; margin-bottom:40px;text-align:left;">
<li style="margin-bottom:15px; font-size:17px; display:flex; align-items:center; gap:15px; color:#333;"><i class="fa fa-graduation-cap" style="color:#46bfee; font-size:20px;"></i> Especialista en Neumología (PUC)</li>
<li style="margin-bottom:15px; font-size:17px; display:flex; align-items:center; gap:15px; color:#333;"><i class="fa fa-university" style="color:#46bfee; font-size:20px;"></i> Académica U. de Valparaíso</li>
<li style="margin-bottom:15px; font-size:17px; display:flex; align-items:center; gap:15px; color:#333;"><i class="fa fa-heartbeat" style="color:#46bfee; font-size:20px;"></i> Miembro SER Chile</li>
</ul>
<div class="vg-founder-actions"><a href="#" class="vg-btn">Conocer más de Daniela</a>
<div class="vg-social-icons"><a href="#"><i class="fa fa-linkedin"></i></a><a href="#"><i class="fa fa-instagram"></i></a></div>
</div>
</div>
</div>
</section>
<section class="vg-testimonials" style="padding:100px 5%; background-color:#fcfcfc !important; text-align:center;">
    <h2 style="font-size:45px; font-weight:900; color:#111111 !important; margin-bottom:50px;">Historias de Recuperación</h2>
    <div style="max-width:900px; margin:0 auto; background:#ffffff; padding:60px; border-radius:40px; box-shadow:0 20px 50px rgba(0,0,0,0.05); border:1px solid #f0f0f0;">
        <i class="fa fa-quote-left" style="font-size:45px; color:#46bfee; opacity:0.5; margin-bottom:25px; display:block;"></i>
        <p style="font-size:24px; color:#444; font-style:italic; line-height:1.6; margin-bottom:30px;">"Destaco su excelente profesionalismo, apoyo, compromiso con el paciente, siempre con una gran disposición y calidez humana..."</p>
        <h4 style="color:#8f55a0 !important; font-weight:800; font-size:18px; margin:0; text-transform:uppercase; letter-spacing:1px;">— Alicia Basso</h4>
        <p style="color:#888; font-size:14px; margin-top:5px;">Paciente Rehabilitación Pulmonar</p>
    </div>
</section>
<section class="vg-instagram">
<div class="vg-ig-inner">
<div class="vg-ig-text">
<h4><i class="fa fa-instagram"></i> @neumovital.cl</h4>
<h2>Consejos y Casos Clínicos</h2>
<p>Únete a nuestra comunidad de pacientes que ya están recuperando su calidad de vida. Tips de respiración, uso de inhaladores y casos reales.</p>
</div>
<div class="vg-ig-videos-grid">
<iframe src="https://www.instagram.com/reel/DWPZ7oWxyVv/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
<iframe src="https://www.instagram.com/reel/DYxxL4QRP56/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
<iframe src="https://www.instagram.com/reel/DTv3Qtijswv/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
<iframe src="https://www.instagram.com/p/DPexNKPCbOb/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
</div>
</div>
</section>
<section class="vg-doctors-banner" style="padding:80px 5%; background-color:#111111 !important; color:#ffffff !important; display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:50px;">
    <div style="max-width:600px;">
        <h4 style="color:#46bfee !important; font-weight:800; letter-spacing:2px; text-transform:uppercase; margin-bottom:15px;"><i class="fa fa-user-md"></i> Programa de Derivación</h4>
        <h2 style="font-size:40px; font-weight:900; margin-bottom:20px; line-height:1.1;">Alianza Estratégica para Especialistas</h2>
        <p style="font-size:18px; color:#aaaaaa !important; line-height:1.6; margin-bottom:0;">Somos el centro solucionador aliado para Broncopulmonares, Geriatras e Internistas. Aseguramos continuidad en la atención y resultados confiables para tus pacientes.</p>
    </div>
    <div style="background:rgba(255,255,255,0.05); padding:40px; border-radius:20px; max-width:400px; border:1px solid rgba(255,255,255,0.1);">
        <h3 style="font-size:22px; font-weight:800; margin-bottom:15px; color:#ffffff !important;"><i class="fa fa-shield" style="color:#25D366; margin-right:10px;"></i> Cobertura Transparente</h3>
        <p style="font-size:16px; color:#cccccc !important; line-height:1.6; margin-bottom:0;">Atendemos de forma ágil por sistema <strong style="color:#fff;">ISAPRE</strong> y ofrecemos valores preferentes y altamente accesibles para pacientes <strong style="color:#fff;">FONASA</strong>.</p>
    </div>
</section>
<section class="vg-footer-cta">
<div class="vg-footer-content">
<h2>¿Listo para dar el <span>primer paso</span>?</h2>
<a href="https://wa.me/56912345678" target="_blank" class="vg-btn-whatsapp"><i class="fa fa-whatsapp"></i> Agenda tu hora</a>
<div class="vg-whatsapp-text">Te responderemos a la brevedad para coordinar tu evaluación.</div>
</div>
</section>
</div>'''

# ==========================================
# V2 CONTENT
# ==========================================
css_v2 = '''<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800;900&display=swap');
.vg-wrapper{font-family:'Outfit', sans-serif !important;overflow-x:hidden;background-color:#ffffff !important;position:relative;z-index:1;width:100vw;left:50%;right:50%;margin-left:-50vw;margin-right:-50vw;}
.vg-btn-primary{background-color:#8f55a0 !important;color:#ffffff !important;padding:18px 40px;border-radius:8px;font-size:16px;font-weight:700;text-transform:uppercase;letter-spacing:1px;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:15px;transition:all 0.4s ease;box-shadow:0 15px 30px rgba(143, 85, 160, 0.25) !important;}
.vg-btn-primary:hover{transform:translateY(-5px);box-shadow:0 25px 40px rgba(143, 85, 160, 0.4) !important;color:#ffffff !important;background-color:#7a468a !important;}
.vg-btn-outline{border:2px solid #111111 !important;color:#111111 !important;padding:16px 38px;border-radius:8px;font-size:16px;font-weight:700;text-transform:uppercase;letter-spacing:1px;text-decoration:none;display:inline-block;transition:all 0.3s ease;text-align:center;}
.vg-btn-outline:hover{background-color:#111111 !important;color:#ffffff !important;}
.vg-play-btn{align-self:flex-start;max-width:350px;width:max-content;background-color:#ffffff !important;border:1px solid #d0d0d0 !important;color:#8f55a0 !important;padding:10px 24px;border-radius:50px !important;font-size:12px;font-weight:800;cursor:pointer;transition:0.3s;display:inline-flex;align-items:center;justify-content:center;gap:8px;outline:none;margin-bottom:25px;text-transform:uppercase;letter-spacing:1px;font-family:'Outfit', sans-serif !important;box-shadow:0 5px 15px rgba(0,0,0,0.05) !important;}
.vg-play-btn:hover{background-color:#8f55a0 !important;color:#fff !important;border-color:#8f55a0 !important;transform:translateY(-2px);}
.vg-play-btn.playing{background-color:#ff4757 !important;color:#fff !important;border-color:#ff4757 !important;animation:pulseRed 1.5s infinite;}
@keyframes pulseRed{0%{box-shadow:0 0 0 0 rgba(255, 71, 87, 0.4);}70%{box-shadow:0 0 0 15px rgba(255, 71, 87, 0);}100%{box-shadow:0 0 0 0 rgba(255, 71, 87, 0);}}
@keyframes organicShape{0%{border-radius:40% 60% 70% 30% / 40% 50% 60% 50%;}34%{border-radius:70% 30% 50% 50% / 30% 30% 70% 70%;}67%{border-radius:100% 60% 60% 100% / 100% 100% 60% 60%;}100%{border-radius:40% 60% 70% 30% / 40% 50% 60% 50%;}}
@keyframes organicShapeReverse{0%{border-radius:70% 30% 50% 50% / 30% 30% 70% 70%;}50%{border-radius:40% 60% 70% 30% / 40% 50% 60% 50%;}100%{border-radius:70% 30% 50% 50% / 30% 30% 70% 70%;}}
.vg-split-hero{display:flex;min-height:95vh;background-color:#ffffff !important;flex-wrap:wrap;}
.vg-split-left{width:55%;display:flex;flex-direction:column;justify-content:center;padding:80px 8%;position:relative;z-index:2;background-color:#fcfcfc !important;}
.vg-split-right{width:45%;position:relative;z-index:1;overflow:hidden;min-height:500px;}
.vg-split-right::after{content:'';position:absolute;top:0;left:0;width:100%;height:100%;background:linear-gradient(to right, #fcfcfc 0%, rgba(252,252,252,0.9) 5%, rgba(252,252,252,0) 40%);z-index:2;pointer-events:none;}
.vg-split-right::before{content:'';position:absolute;top:0;left:0;width:100%;height:100%;background:repeating-linear-gradient(-45deg, rgba(255, 255, 255, 0.35), rgba(255, 255, 255, 0.35) 2px, transparent 2px, transparent 12px);z-index:3;pointer-events:none;}
.vg-split-slider{position:absolute;top:0;left:0;width:100%;height:100%;}
.vg-split-img{position:absolute;top:0;left:0;width:100%;height:100%;background-size:cover;background-position:center;opacity:0;animation:crossfade 18s infinite;}
.vg-split-img:nth-child(1){background-image:url('https://neumovital.cl/wp-content/uploads/2025/07/15A1197_pp-scaled.jpg');animation-delay:0s;}
.vg-split-img:nth-child(2){background-image:url('https://neumovital.cl/wp-content/uploads/2025/07/20250626_132653-scaled.jpg');animation-delay:6s;}
.vg-split-img:nth-child(3){background-image:url('https://neumovital.cl/wp-content/uploads/2025/07/20250626_133426-1-scaled.jpg');animation-delay:12s;}
@keyframes crossfade{0%{opacity:0;transform:scale(1);}10%{opacity:1;}33.33%{opacity:1;}43.33%{opacity:0;transform:scale(1.05);}100%{opacity:0;}}
.vg-hero-label{font-size:14px;font-weight:800;color:#46bfee !important;text-transform:uppercase;letter-spacing:3px;margin-bottom:20px;display:flex;align-items:center;gap:10px;}
.vg-hero-label::before{content:'';display:block;width:40px;height:3px;background-color:#46bfee !important;}
.vg-title-split{font-size:clamp(50px, 5vw, 85px);font-weight:900;color:#111111 !important;line-height:1.05;margin-bottom:30px;letter-spacing:-2px;}
.vg-title-split span{color:#8f55a0 !important;}
.vg-desc-split{font-size:20px;color:#555555 !important;line-height:1.7;margin-bottom:40px;max-width:90%;font-weight:400;}
.vg-hero-actions{display:flex;gap:35px;align-items:center;flex-wrap:wrap;margin-bottom:50px;margin-top:30px;}
.vg-hero-citation{display:flex;align-items:center;padding:25px 0;border-top:1px solid #eeeeee !important;border-bottom:1px solid #eeeeee !important;margin-bottom:35px;}
.vg-hero-citation img{width:60px;height:60px;border-radius:50%;object-fit:cover;margin-right:20px;}
.vg-citation-text p{font-size:18px;font-style:italic;color:#333333 !important;font-weight:500;margin-bottom:5px;}
.vg-citation-text span{font-size:13px;color:#8f55a0 !important;font-weight:800;text-transform:uppercase;letter-spacing:1px;}
.vg-trust-bar{display:flex;justify-content:space-between;align-items:center;padding:40px 8%;background-color:#ffffff !important;border-top:1px solid #f0f0f0 !important;border-bottom:1px solid #f0f0f0 !important;flex-wrap:wrap;gap:30px;}
.vg-trust-item{display:flex;align-items:center;gap:15px;font-size:17px;font-weight:700;color:#111111 !important;}
.vg-trust-item i{font-size:24px;color:#46bfee !important;}
.vg-trust-item img{height:28px;filter:brightness(0) saturate(100%) invert(67%) sepia(45%) saturate(718%) hue-rotate(167deg) brightness(98%) contrast(93%);}
.vg-zigzag-section{padding:120px 0;background-color:#ffffff !important;}
.vg-zig-row{display:flex;flex-wrap:wrap;align-items:center;margin-bottom:120px;}
.vg-zig-row:last-child{margin-bottom:0;}
.vg-zig-text{width:45%;padding:0 8%;}
.vg-zig-img{width:55%;padding-right:5%;position:relative;}
.vg-zig-row.reverse .vg-zig-text{order:2;padding:0 8% 0 5%;}
.vg-zig-row.reverse .vg-zig-img{order:1;padding-right:0;padding-left:5%;}
.vg-zig-img-inner{width:100%;height:600px;border-radius:40% 60% 70% 30% / 40% 50% 60% 50%;background-color:#f8fbfc !important;position:relative;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,0.08) !important;animation:organicShape 12s ease-in-out infinite;transform:translateZ(0);}
.vg-zig-row.reverse .vg-zig-img-inner{animation:organicShapeReverse 14s ease-in-out infinite;}
.vg-zig-img-inner img{width:100%;height:100%;object-fit:cover;transform:scale(1.05);}
.vg-zig-num{font-size:150px;font-weight:900;color:#f0f4f8 !important;line-height:0.8;margin-bottom:20px;letter-spacing:-5px;}
.vg-zig-title{font-size:45px;font-weight:800;color:#111111 !important;line-height:1.1;margin-bottom:30px;}
.vg-zig-desc{font-size:18px;color:#666666 !important;line-height:1.7;margin-bottom:40px;}
.vg-founder-editorial{padding:0;background-color:#8f55a0 !important;display:flex;align-items:stretch;flex-wrap:wrap;position:relative;overflow:hidden;}
.vg-fc-img-strong{width:45%;position:relative;min-height:600px;display:flex;justify-content:center;align-items:center;padding:60px 0;}
.vg-fc-img-strong-blob{width:85%;height:85%;min-height:500px;position:relative;overflow:hidden;border-radius:60% 40% 30% 70% / 60% 30% 70% 40%;animation:organicShape 15s ease-in-out infinite alternate;box-shadow:0 40px 80px rgba(0,0,0,0.3) !important;}
.vg-fc-img-strong-blob img{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;transform:scale(1.1);}
.vg-fc-text-strong{width:55%;padding:120px 8%;display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2;}
.vg-fc-text-strong::after{content:"\\f10e";font-family:"FontAwesome";position:absolute;right:5%;bottom:5%;font-size:250px;color:rgba(255,255,255,0.05);z-index:-1;line-height:1;}
.vg-fc-text-strong h4{color:#46bfee !important;font-size:16px;font-weight:800;letter-spacing:3px;text-transform:uppercase;margin-bottom:20px;}
.vg-fc-text-strong h2{font-size:clamp(35px, 4vw, 55px);font-weight:900;color:#ffffff !important;margin-bottom:30px;line-height:1.1;}
.vg-fc-text-strong p.quote{font-size:clamp(20px, 2.5vw, 28px);color:#ffffff !important;font-weight:300;font-style:italic;margin-bottom:35px;line-height:1.4;border-left:4px solid #46bfee !important;padding-left:25px;}
.vg-fc-text-strong p.desc{font-size:18px;color:rgba(255,255,255,0.85) !important;line-height:1.8;margin-bottom:50px;font-weight:400;max-width:90%;}
.vg-fc-social-strong{display:flex;gap:20px;}
.vg-fc-social-strong a{width:60px;height:60px;border-radius:50%;background-color:rgba(255,255,255,0.1) !important;display:flex;align-items:center;justify-content:center;color:#ffffff !important;font-size:22px;transition:0.4s;}
.vg-fc-social-strong a:hover{background-color:#46bfee !important;color:#ffffff !important;transform:translateY(-5px);}
.vg-instagram-staggered{padding:120px 5%;background-color:#ffffff !important;}
.vg-ig-header{text-align:center;margin-bottom:80px;max-width:800px;margin-left:auto;margin-right:auto;}
.vg-ig-header h4{color:#e6683c !important;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:15px;font-size:14px;}
.vg-ig-header h2{font-size:50px;font-weight:900;color:#111111 !important;line-height:1.1;letter-spacing:-1px;}
.vg-ig-masonry{display:grid;grid-template-columns:repeat(4, 1fr);gap:30px;align-items:start;}
.vg-ig-item iframe{width:100%;height:500px;border-radius:20px;box-shadow:0 20px 50px rgba(0,0,0,0.08) !important;background:#ffffff;}
.vg-ig-item:nth-child(even){margin-top:80px;}
.vg-footer-cta-bold{background-color:#8f55a0 !important;padding:120px 5%;text-align:center;}
.vg-footer-cta-bold h2{font-size:clamp(40px, 5vw, 65px);font-weight:900;color:#ffffff !important;margin-bottom:40px;letter-spacing:-1px;line-height:1.1;}
.vg-footer-cta-bold h2 span{color:#e0f2fe !important;}
.vg-floating-cta{position:fixed;bottom:30px;left:30px;background-color:#8f55a0 !important;color:#fff !important;padding:16px 30px;border-radius:50px;font-weight:800;font-size:16px;box-shadow:0 10px 30px rgba(143, 85, 160, 0.4) !important;z-index:9999;display:flex;align-items:center;gap:12px;text-decoration:none;text-transform:uppercase;letter-spacing:1px;transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);opacity:0;visibility:hidden;transform:translateY(30px) scale(0.8);pointer-events:none;}
.vg-floating-cta.show-cta{opacity:1;visibility:visible;transform:translateY(0) scale(1);pointer-events:auto;animation:attentionWobble 3.5s infinite 1s;}
.vg-floating-cta:hover{transform:translateY(-5px) scale(1.05) !important;box-shadow:0 15px 40px rgba(143, 85, 160, 0.6) !important;color:#fff !important;background-color:#7a468a !important;animation:none !important;}
.vg-floating-cta i{font-size:20px;}
@keyframes attentionWobble{0%{transform:rotate(0deg) scale(1);box-shadow:0 0 0 0 rgba(143,85,160,0.7);}5%{transform:rotate(-15deg) scale(1.15);box-shadow:0 0 0 15px rgba(143,85,160,0);}10%{transform:rotate(15deg) scale(1.15);}15%{transform:rotate(-15deg) scale(1.15);}20%{transform:rotate(15deg) scale(1.15);}25%{transform:rotate(0deg) scale(1);box-shadow:0 0 0 0 rgba(143,85,160,0);}100%{transform:rotate(0deg) scale(1);}}
.vg-pill{background:rgba(255,255,255,0.05) !important;border:1px solid rgba(255,255,255,0.15) !important;padding:8px 18px;border-radius:12px;color:#ffffff !important;font-size:14px;font-weight:600;display:flex;align-items:center;gap:8px;}

/* --- V2 RESPONSIVE FIXES --- */
@media (max-width:1100px){
.vg-split-left{width:100%;padding:100px 5%;background-color:#ffffff !important; text-align:center;}
.vg-split-right{width:100%;min-height:400px;position:relative !important;}
.vg-split-right::after{background:linear-gradient(to bottom, #ffffff 0%, rgba(255,255,255,0.8) 15%, rgba(255,255,255,0) 40%);}
.vg-title-split{text-align:center;}
.vg-desc-split{text-align:center; margin-left:auto; margin-right:auto;}
.vg-hero-label{justify-content:center;}
.vg-hero-label::before{display:none;}
.vg-hero-actions{justify-content:center; width:100%;}
.vg-hero-citation{flex-direction:column; text-align:center; justify-content:center; gap:15px;}
.vg-hero-citation img{margin-right:0 !important; margin-left:0 !important;}
.vg-play-btn{margin-left:auto !important; margin-right:auto !important;}
.vg-zig-row{flex-direction:column;}
.vg-zig-text, .vg-zig-img{width:100%;padding:0 5% !important;margin-bottom:40px;text-align:center;}
.vg-zig-row.reverse .vg-zig-text{order:1;}
.vg-zig-row.reverse .vg-zig-img{order:2;}
.vg-fc-img-strong, .vg-fc-text-strong{width:100%;}
.vg-fc-img-strong{min-height:400px;padding:40px;}
.vg-fc-img-strong-blob{width:100%;height:100%;}
.vg-fc-text-strong{padding:80px 5%; text-align:center;}
.vg-fc-text-strong::after{display:none;}
.vg-fc-social-strong{justify-content:center;}
.vg-ig-masonry{grid-template-columns:repeat(2, 1fr);}
.vg-ig-item:nth-child(even){margin-top:0;}
.vg-ig-item:nth-child(2), .vg-ig-item:nth-child(4){margin-top:40px;}
.vg-doctors-banner { text-align:center; flex-direction:column; }
.vg-doctors-banner > div { width:100%; max-width:100% !important; }
}
@media (max-width:600px){
.vg-split-left{padding:80px 5% 50px !important;}
.vg-title-split{font-size:38px !important; margin-bottom:15px;}
.vg-desc-split{font-size:18px !important; margin-bottom:30px;}
.vg-hero-actions{flex-direction:column; gap:15px;}
.vg-hero-actions a{width:100%; text-align:center; margin:0;}
.vg-trust-item{width:100%;justify-content:center;}
.vg-floating-cta{bottom:20px;left:20px;padding:16px;border-radius:50%;}
.vg-floating-cta span{display:none;}
.vg-floating-cta i{font-size:24px;margin:0;}
.vg-ig-masonry{grid-template-columns:1fr;}
.vg-ig-item{margin-top:0 !important;margin-bottom:30px;}
.vg-zig-num{font-size:100px !important;}
.vg-zig-title{font-size:32px !important;}
.vg-zig-img-inner{height:400px !important;}
.vg-fc-text-strong h2{font-size:32px !important;}
.vg-footer-cta-bold h2{font-size:36px !important;}
.vg-trust-bar{padding:40px 5%;}
}
</style>
'''

html_v2 = '''<div class="vg-wrapper">
<section class="vg-split-hero">
<div class="vg-split-left">
<div class="vg-hero-label"><i class="fa fa-star"></i> Método Neumovital</div>
<button class="vg-play-btn" onclick="vgPlayText('text-hero-v2', this)"><i class="fa fa-play"></i> Escuchar Sección</button>
<div id="text-hero-v2">
<h1 class="vg-title-split">Tu respiración,<br />tu <span>libertad</span>.</h1>
<p class="vg-desc-split">Clínica especializada en Rehabilitación y Diagnóstico Pulmonar. Dejamos atrás las limitaciones físicas para que recuperes tu vida y autonomía con tecnología de punta.</p>
</div>
<div class="vg-hero-actions"><a href="#agendar" class="vg-btn-primary">Agendar Evaluación <i class="fa fa-arrow-right"></i></a><a href="#examenes" class="vg-btn-outline">Conocer Exámenes</a></div>
<div class="vg-hero-citation"><img decoding="async" src="https://neumovital.cl/wp-content/uploads/2025/06/IMG_6607_SnapseedCopy-scaled.jpeg" alt="Daniela Díaz Hinojosa">
<div class="vg-citation-text">
<p>&#8220;La medicina no se trata solo de pulmones, se trata de personas que vuelven a disfrutar su vida.&#8221;</p>
<span>Dra. Daniela Díaz H. Fundadora Neumovital&reg;</span></div>
</div>
</div>
<div class="vg-split-right">
<div class="vg-split-slider">
<div class="vg-split-img">&nbsp;</div>
<div class="vg-split-img">&nbsp;</div>
<div class="vg-split-img">&nbsp;</div>
</div>
</div>
</section>
<div class="vg-trust-bar">
<div class="vg-trust-item"><i class="fa fa-check-circle"></i> Tecnología de Frontera</div>
<div class="vg-trust-item"><i class="fa fa-check-circle"></i> Resultados Exactos</div>
<div class="vg-trust-item"><img decoding="async" src="https://upload.wikimedia.org/wikipedia/commons/e/ee/Fonasa_logo.svg" alt="Fonasa"></div>
<div class="vg-trust-item"><img decoding="async" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Isapre_Chile.png/1200px-Isapre_Chile.png" alt="Isapres" style="height:22px;"></div>
</div>
<section class="vg-zigzag-section" id="examenes">
<div style="text-align:center; margin-bottom:100px;">
    <h2 style="font-size:45px; font-weight:900; color:#111111 !important; margin-bottom:20px;">Nuestras Especialidades</h2>
    <div style="display:flex; justify-content:center; gap:10px; flex-wrap:wrap; max-width:800px; margin:0 auto;">
        <div class="vg-pill" style="background:#f0f4f8 !important; color:#333 !important; border:none !important;"><i class="fa fa-lungs" style="color:#46bfee !important;"></i> EPOC</div>
        <div class="vg-pill" style="background:#f0f4f8 !important; color:#333 !important; border:none !important;"><i class="fa fa-ribbon" style="color:#46bfee !important;"></i> Cáncer de Pulmón</div>
        <div class="vg-pill" style="background:#f0f4f8 !important; color:#333 !important; border:none !important;"><i class="fa fa-wave-square" style="color:#46bfee !important;"></i> Fibrosis Pulmonar</div>
        <div class="vg-pill" style="background:#f0f4f8 !important; color:#333 !important; border:none !important;"><i class="fa fa-bed" style="color:#46bfee !important;"></i> Apnea del Sueño</div>
        <div class="vg-pill" style="background:#f0f4f8 !important; color:#333 !important; border:none !important;"><i class="fa fa-virus" style="color:#46bfee !important;"></i> Secuelas Respiratorias</div>
    </div>
</div>
<div class="vg-zig-row">
<div class="vg-zig-text">
<div class="vg-zig-num">01</div>
<h2 class="vg-zig-title" style="color:#8f55a0 !important;">Rehabilitación Respiratoria Especializada</h2>
<p class="vg-zig-desc">El corazón de nuestro centro. Nuestro equipo te guía en un programa de entrenamiento muscular y aeróbico supervisado. El objetivo no es solo mejorar los números de tus exámenes, sino devolverte la capacidad de realizar tus actividades diarias sin fatiga extrema.</p>
<a href="#" class="vg-btn-outline">Rangos de Precios</a></div>
<div class="vg-zig-img">
<div class="vg-zig-img-inner"><img decoding="async" src="https://neumovital.cl/wp-content/uploads/2025/07/15A1197_pp-scaled.jpg" alt="Rehabilitación"></div>
</div>
</div>
<div class="vg-zig-row reverse">
<div class="vg-zig-text">
<div class="vg-zig-num">02</div>
<h2 class="vg-zig-title">Laboratorio de Función Pulmonar Avanzado</h2>
<p class="vg-zig-desc">Contamos con un moderno pletismógrafo y equipos de última generación que nos permiten realizar evaluaciones exactas en reposo: Espirometrías, Difusión de Monóxido (DLCO) y medición de Volúmenes Pulmonares. Un diagnóstico preciso es el primer paso vital.</p>
<a href="#" class="vg-btn-outline">Rangos de Precios</a></div>
<div class="vg-zig-img">
<div class="vg-zig-img-inner"><img decoding="async" src="https://neumovital.cl/wp-content/uploads/2025/07/20250626_132653-scaled.jpg" alt="Laboratorio Pulmonar"></div>
</div>
</div>
<div class="vg-zig-row">
<div class="vg-zig-text">
<div class="vg-zig-num">03</div>
<h2 class="vg-zig-title">Estudio y Monitoreo del Sueño</h2>
<p class="vg-zig-desc">La apnea del sueño y los trastornos respiratorios nocturnos pueden deteriorar tu calidad de vida sin que te des cuenta. Realizamos poligrafías respiratorias en la comodidad de tu hogar para detectar y tratar estos problemas de raíz.</p>
<a href="#" class="vg-btn-outline">Rangos de Precios</a></div>
<div class="vg-zig-img">
<div class="vg-zig-img-inner"><img decoding="async" src="https://neumovital.cl/wp-content/uploads/2025/07/IMG_6377-scaled.jpeg" alt="Estudio de Sueño"></div>
</div>
</div>
</section>
<section class="vg-founder-editorial">
<div class="vg-fc-img-strong">
<div class="vg-fc-img-strong-blob"><img decoding="async" src="https://neumovital.cl/wp-content/uploads/2025/06/IMG_6607_SnapseedCopy-scaled.jpeg" alt="Daniela Díaz"></div>
</div>
<div class="vg-fc-text-strong">
<h4>Kinesióloga Especialista en Rehabilitación Respiratoria (DENAKE)</h4>
<h2>Daniela Díaz Hinojosa</h2>
<p class="quote">&#8220;Mi compromiso es acompañar a pacientes y familias a recuperar su autonomía, guiados siempre bajo la filosofía del buen vivir y el buen morir.&#8221;</p>
<p class="desc">Creadora del <strong>Método Neumovital&reg;</strong>. Con formación en la Pontificia Universidad Católica y experiencia docente en la Universidad de Valparaíso, Daniela ha creado un espacio donde la evidencia científica más rigurosa se encuentra con la empatía. Como miembro de la SER Chile, garantiza estándares de clase mundial.</p>
<div class="vg-fc-social-strong"><a href="#"><i class="fa fa-linkedin"></i></a><a href="#"><i class="fa fa-instagram"></i></a></div>
</div>
</section>
<section class="vg-testimonials" style="padding:100px 5%; background-color:#fcfcfc !important; text-align:center;">
    <h2 style="font-size:45px; font-weight:900; color:#111111 !important; margin-bottom:50px;">Historias de Recuperación</h2>
    <div style="max-width:900px; margin:0 auto; background:#ffffff; padding:60px; border-radius:40px; box-shadow:0 20px 50px rgba(0,0,0,0.05); border:1px solid #f0f0f0;">
        <i class="fa fa-quote-left" style="font-size:45px; color:#46bfee; opacity:0.5; margin-bottom:25px; display:block;"></i>
        <p style="font-size:24px; color:#444; font-style:italic; line-height:1.6; margin-bottom:30px;">"Destaco su excelente profesionalismo, apoyo, compromiso con el paciente, siempre con una gran disposición y calidez humana..."</p>
        <h4 style="color:#8f55a0 !important; font-weight:800; font-size:18px; margin:0; text-transform:uppercase; letter-spacing:1px;">— Alicia Basso</h4>
        <p style="color:#888; font-size:14px; margin-top:5px;">Paciente Rehabilitación Pulmonar</p>
    </div>
</section>
<section class="vg-instagram-staggered">
<div class="vg-ig-header">
<h4>Comunidad @neumovital.cl</h4>
<h2>Aprende a respirar mejor junto a nuestros pacientes</h2>
</div>
<div class="vg-ig-masonry">
<div class="vg-ig-item"><iframe src="https://www.instagram.com/reel/DWPZ7oWxyVv/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe></div>
<div class="vg-ig-item"><iframe src="https://www.instagram.com/reel/DYxxL4QRP56/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe></div>
<div class="vg-ig-item"><iframe src="https://www.instagram.com/reel/DTv3Qtijswv/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe></div>
<div class="vg-ig-item"><iframe src="https://www.instagram.com/p/DPexNKPCbOb/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe></div>
</div>
</section>
<section class="vg-doctors-banner" style="padding:80px 5%; background-color:#111111 !important; color:#ffffff !important; display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:50px;">
    <div style="max-width:600px;">
        <h4 style="color:#46bfee !important; font-weight:800; letter-spacing:2px; text-transform:uppercase; margin-bottom:15px;"><i class="fa fa-user-md"></i> Programa de Derivación</h4>
        <h2 style="font-size:40px; font-weight:900; margin-bottom:20px; line-height:1.1;">Alianza Estratégica para Especialistas</h2>
        <p style="font-size:18px; color:#aaaaaa !important; line-height:1.6; margin-bottom:0;">Somos el centro solucionador aliado para Broncopulmonares, Geriatras e Internistas. Aseguramos continuidad en la atención y resultados confiables para tus pacientes.</p>
    </div>
    <div style="background:rgba(255,255,255,0.05); padding:40px; border-radius:20px; max-width:400px; border:1px solid rgba(255,255,255,0.1);">
        <h3 style="font-size:22px; font-weight:800; margin-bottom:15px; color:#ffffff !important;"><i class="fa fa-shield" style="color:#25D366; margin-right:10px;"></i> Cobertura Transparente</h3>
        <p style="font-size:16px; color:#cccccc !important; line-height:1.6; margin-bottom:0;">Atendemos de forma ágil por sistema <strong style="color:#fff;">ISAPRE</strong> y ofrecemos valores preferentes y altamente accesibles para pacientes <strong style="color:#fff;">FONASA</strong>.</p>
    </div>
</section>
<section class="vg-footer-cta-bold">
<h2>La falta de aire <span>no es</span> normal.</h2>
<a href="https://wa.me/56912345678" target="_blank" class="vg-btn-primary" style="background-color:#ffffff !important; color:#8f55a0 !important;"><i class="fa fa-whatsapp" style="font-size:24px;"></i> Contáctanos hoy mismo</a></section>
</div>'''


final_content_v1 = wrapper_start + '\n' + css_v1 + css_v1_mobile + '\n' + html_v1 + '\n' + floating_cta_html + '\n' + js + '\n' + wrapper_end
final_content_v2 = wrapper_start + '\n' + css_v2 + css_v2_mobile + '\n' + html_v2 + '\n' + floating_cta_html + '\n' + js + '\n' + wrapper_end

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(final_content_v1)
    
with open('propuestas/home/Propuesta-v2.txt', 'w') as f:
    f.write(final_content_v2)

print("Content Updated successfully.")
