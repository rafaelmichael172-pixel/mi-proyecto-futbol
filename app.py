from flask import Flask, render_template_string

app = Flask(__name__)

# --- 1. DATOS DE LAS CASAS DE APUESTAS (REALES 2026) ---
CASAS = [
    {
        "nombre": "Betano",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Betano_Logo.png",
        "color": "#bf2a2a", # Rojo
        "etiqueta": "🏆 MEJOR DEL PERÚ",
        "puntuacion": "4.9",
        "bono_titulo": "BONO EXCLUSIVO",
        "bono_desc": "S/500 + 20% Extra",
        "link": "https://www.betano.com.pe",
        "legal": "18+ | Depósito mín S/30 | Rollover x5"
    },
    {
        "nombre": "Betsson",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Betsson_Logo.png",
        "color": "#ff7b00", # Naranja
        "etiqueta": "⚡ PAGOS RÁPIDOS",
        "puntuacion": "4.8",
        "bono_titulo": "APUESTA CERO RIESGO",
        "bono_desc": "S/50 Gratis",
        "link": "https://www.betsson.com/pe",
        "legal": "18+ | Nuevos usuarios | TyC Aplican"
    },
    {
        "nombre": "Inkabet",
        "logo": "https://seeklogo.com/images/I/inkabet-logo-36B6F68414-seeklogo.com.png",
        "color": "#333333", # Negro
        "etiqueta": "🇵🇪 100% PERUANA",
        "puntuacion": "4.7",
        "bono_titulo": "DUPLICA TU RECARGA",
        "bono_desc": "100% hasta S/800",
        "link": "https://www.inkabet.pe",
        "legal": "18+ | Rollover x7 | Min. cuota 1.50"
    },
    {
        "nombre": "Coolbet",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Coolbet_logo.svg/2560px-Coolbet_logo.svg.png",
        "color": "#000000", # Negro
        "etiqueta": "💎 MEJORES CUOTAS",
        "puntuacion": "4.8",
        "bono_titulo": "BONO BIENVENIDA",
        "bono_desc": "100% hasta S/400",
        "link": "https://www.coolbet.com/pe",
        "legal": "18+ | Sin Rollover complicado"
    }
]

# --- 2. EL DISEÑO WEB INTEGRADO (CSS + HTML DENTRO DE PYTHON) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ApuestaTop Perú 2026</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        /* ESTILOS CSS */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background-color: #0f0f0f; font-family: 'Montserrat', sans-serif; color: white; display: flex; flex-direction: column; min-height: 100vh; }
        
        /* HEADER */
        header { background: #000; padding: 15px; text-align: center; border-bottom: 2px solid #ff3b3b; box-shadow: 0 4px 15px rgba(255,59,59,0.2); }
        .logo { font-size: 24px; font-weight: 900; }
        .logo span { color: #ff3b3b; }
        .subtitle { font-size: 10px; color: #888; letter-spacing: 2px; text-transform: uppercase; margin-top: 5px; }
        
        /* CONTENEDOR */
        .container { width: 100%; max-width: 500px; margin: 0 auto; padding: 20px 15px; flex: 1; }
        
        /* TARJETA */
        .card { background: #1a1a1a; border-radius: 12px; margin-bottom: 20px; overflow: hidden; border: 1px solid #333; box-shadow: 0 5px 15px rgba(0,0,0,0.5); }
        .tag { font-size: 10px; font-weight: 800; text-align: center; padding: 5px; color: white; text-transform: uppercase; }
        
        .card-body { display: flex; padding: 15px; align-items: center; }
        
        /* LOGO IZQUIERDA */
        .col-left { width: 30%; text-align: center; display: flex; flex-direction: column; align-items: center; }
        .bookie-logo { width: 100%; max-width: 80px; height: auto; object-fit: contain; }
        .stars { color: #ffd700; font-size: 10px; margin-top: 8px; }
        .score { font-weight: bold; font-size: 14px; }
        
        /* INFO DERECHA */
        .col-right { width: 70%; padding-left: 15px; border-left: 1px solid #333; text-align: center; }
        .bonus-label { color: #aaa; font-size: 9px; font-weight: 700; text-transform: uppercase; }
        .bonus-val { font-size: 18px; font-weight: 900; color: #fff; margin: 4px 0; }
        
        /* BOTON */
        .btn-claim { display: block; background: linear-gradient(90deg, #d32f2f, #ff3b3b); color: white; text-decoration: none; padding: 10px; border-radius: 6px; font-weight: 800; font-size: 13px; margin-top: 8px; box-shadow: 0 4px 0 #8b0000; transition: transform 0.1s; }
        .btn-claim:active { transform: translateY(3px); box-shadow: none; }
        
        .legal-mini { font-size: 8px; color: #555; margin-top: 8px; }
        
        /* FOOTER */
        footer { background: #000; padding: 30px; text-align: center; border-top: 1px solid #333; font-size: 11px; margin-top: auto; }
        .footer-links a { color: #888; text-decoration: none; margin: 0 10px; }
        .footer-links a:hover { color: #fff; }
    </style>
</head>
<body>

    <header>
        <div class="logo">APUESTA<span>TOP</span></div>
        <div class="subtitle">Ranking Oficial Perú 2026</div>
    </header>

    <div class="container">
        {% for casa in casas %}
        <div class="card">
            <div class="tag" style="background-color: {{ casa.color }};">{{ casa.etiqueta }}</div>
            <div class="card-body">
                <div class="col-left">
                    <img src="{{ casa.logo }}" class="bookie-logo">
                    <div class="stars">⭐⭐⭐⭐⭐</div>
                    <div class="score">{{ casa.puntuacion }}/5.0</div>
                </div>
                <div class="col-right">
                    <div class="bonus-label">{{ casa.bono_titulo }}</div>
                    <div class="bonus-val">{{ casa.bono_desc }}</div>
                    <a href="{{ casa.link }}" target="_blank" class="btn-claim">RECLAMAR BONO ➤</a>
                    <div class="legal-mini">{{ casa.legal }}</div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>

    <footer>
        <div class="footer-links">
            <a href="/terminos">Términos</a>
            <a href="/privacidad">Privacidad</a>
        </div>
        <br>
        <p style="color:#444">© 2026 ApuestaTop. Solo +18.</p>
    </footer>

</body>
</html>
"""

# --- 3. RUTAS DE LA APLICACIÓN ---

@app.route('/')
def home():
    # Renderizamos el texto HTML de arriba mezclado con los datos de las casas
    return render_template_string(HTML_TEMPLATE, casas=CASAS)

@app.route('/terminos')
def terminos():
    return "<body style='background:#111; color:#fff; font-family:sans-serif; padding:20px;'><h1>Términos</h1><p>Sitio informativo. No captamos dinero.</p><a href='/' style='color:red'>Volver</a></body>"

@app.route('/privacidad')
def privacidad():
    return "<body style='background:#111; color:#fff; font-family:sans-serif; padding:20px;'><h1>Privacidad</h1><p>No guardamos datos.</p><a href='/' style='color:red'>Volver</a></body>"

if __name__ == '__main__':
    app.run(debug=True)