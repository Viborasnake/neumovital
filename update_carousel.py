import re

with open('propuestas/home/Propuesta-v1.txt', 'r') as f:
    text = f.read()

# The CSS for the carousel
carousel_css = """
/* --- TESTIMONIALS CAROUSEL --- */
.vg-testim-carousel {
    max-width: 1200px;
    margin: 0 auto;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
    padding-bottom: 20px;
}
.vg-testim-carousel::-webkit-scrollbar {
    height: 8px;
}
.vg-testim-carousel::-webkit-scrollbar-track {
    background: #f0f0f0;
    border-radius: 10px;
}
.vg-testim-carousel::-webkit-scrollbar-thumb {
    background: #46bfee;
    border-radius: 10px;
}
.vg-testim-track {
    display: flex;
    gap: 30px;
    width: max-content;
    padding: 20px 10px;
}
.vg-testim-card {
    width: 380px;
    scroll-snap-align: center;
    background: #ffffff;
    padding: 40px 30px;
    border-radius: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    border: 1px solid #f0f0f0;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    transition: 0.3s;
    white-space: normal;
}
.vg-testim-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(143, 85, 160, 0.15);
    border-color: rgba(143, 85, 160, 0.3);
}
.vg-testim-card i.fa-quote-left {
    font-size: 35px;
    color: #46bfee;
    opacity: 0.5;
    margin-bottom: 20px;
}
.vg-testim-card p {
    font-size: 17px;
    color: #555;
    font-style: italic;
    line-height: 1.6;
    margin-bottom: 20px;
    flex-grow: 1;
}
.vg-testim-card h4 {
    color: #8f55a0 !important;
    font-weight: 800;
    font-size: 15px;
    margin-bottom: 5px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.vg-stars {
    color: #f1c40f;
    font-size: 13px;
    letter-spacing: 2px;
}
@media (max-width:600px) {
    .vg-testim-card { width: 300px; padding: 30px 20px; }
    .vg-testim-track { gap: 20px; }
}
</style>
"""

# Inject CSS by replacing </style> with our CSS + </style>
text = text.replace("</style>", carousel_css)

# The new HTML for the carousel
carousel_html = """<section class="vg-testimonials" style="padding:100px 5%; background-color:#f8fbfc !important; text-align:center; overflow:hidden;">
    <h2 style="font-size:45px; font-weight:900; color:#111111 !important; margin-bottom:20px;">Lo que dicen nuestros pacientes</h2>
    <p style="font-size:18px; color:#666; margin-bottom:50px;">Desliza para leer más testimonios <i class="fa fa-arrows-h" style="color:#46bfee; margin-left:10px;"></i></p>
    
    <div class="vg-testim-carousel">
        <div class="vg-testim-track">
            <div class="vg-testim-card">
                <i class="fa fa-quote-left"></i>
                <p>"Destaco su excelente profesionalismo, apoyo, compromiso con el paciente, siempre con una gran disposición y calidez humana..."</p>
                <div>
                    <h4>— Alicia Basso</h4>
                    <div class="vg-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                </div>
            </div>
            
            <div class="vg-testim-card">
                <i class="fa fa-quote-left"></i>
                <p>"Llegué sin poder caminar una cuadra por mi EPOC. Gracias a la rehabilitación, hoy puedo jugar con mis nietos sin ahogarme. Me devolvieron la vida."</p>
                <div>
                    <h4>— Carlos Martínez</h4>
                    <div class="vg-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                </div>
            </div>

            <div class="vg-testim-card">
                <i class="fa fa-quote-left"></i>
                <p>"La Dra. Díaz y su equipo me devolvieron la esperanza. Su laboratorio es de primer nivel y el trato es inigualable. No me sentí como un número más."</p>
                <div>
                    <h4>— María E. Silva</h4>
                    <div class="vg-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                </div>
            </div>

            <div class="vg-testim-card">
                <i class="fa fa-quote-left"></i>
                <p>"Después del COVID quedé con secuelas. En Neumovital encontré la guía exacta para recuperar mi capacidad pulmonar paso a paso y volver a mi trabajo."</p>
                <div>
                    <h4>— Rodrigo Fuentes</h4>
                    <div class="vg-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                </div>
            </div>

            <div class="vg-testim-card">
                <i class="fa fa-quote-left"></i>
                <p>"Me hicieron el estudio de apnea del sueño en mi propia casa. Súper cómodo y rápido. Por fin entiendo por qué amanecía tan cansada."</p>
                <div>
                    <h4>— Patricia Morales</h4>
                    <div class="vg-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                </div>
            </div>

            <div class="vg-testim-card">
                <i class="fa fa-quote-left"></i>
                <p>"Excelente clínica, no se siente como un hospital frío. Te tratan con un cariño inmenso y se nota que son expertos en lo que hacen."</p>
                <div>
                    <h4>— Jorge Villanueva</h4>
                    <div class="vg-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                </div>
            </div>
        </div>
    </div>
</section>"""

# Replace the old section block. 
# Using regex to match the old block accurately.
old_block_pattern = r'<section class="vg-testimonials".*?</section>'
text = re.sub(old_block_pattern, carousel_html, text, flags=re.DOTALL)

with open('propuestas/home/Propuesta-v1.txt', 'w') as f:
    f.write(text)

print("Carousel created successfully!")
