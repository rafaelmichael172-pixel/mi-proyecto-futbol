from flask import Flask, render_template

app = Flask(__name__)

# CONFIGURACIÓN DEL SITIO
SITE_CONFIG = {
    "nombre": "ApuestaTop",
    "dominio": "apuestatop.lat", 
    "contacto": "contacto@apuestatop.lat"
}

# --- AQUÍ PEGAS TUS DATOS REALES ---
# He puesto logos que SÍ cargan. Solo cambia los "links" y "bono_desc".

CASAS = [
    {
        "id": 1,
        "nombre": "Betano",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Betano_Logo.png",
        "etiqueta": "MEJOR EN LATAM",
        "etiqueta_color": "#ff4b4b", # Rojo Betano
        "etiqueta_texto_color": "#ffffff",
        "puntuacion": "4.9",
        "bono_titulo": "BONO EXCLUSIVO",
        "bono_desc": "S/500 + 20% Extra", # <--- EDITA ESTO
        "link": "https://www.betano.com", # <--- PEGA AQUÍ TU LINK DE AFILIADO
        "legal": "18+ | Aplican T&C | Nuevos usuarios",
        "autorizado": True
    },
    {
        "id": 2,
        "nombre": "Betsson",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Betsson_Logo.png",
        "etiqueta": "PAGOS RÁPIDOS",
        "etiqueta_color": "#ff9900", # Naranja Betsson
        "etiqueta_texto_color": "#000000",
        "puntuacion": "4.8",
        "bono_titulo": "APUESTA GRATUITA",
        "bono_desc": "S/40 Gratis o Cero Riesgo", # <--- EDITA ESTO
        "link": "https://www.betsson.com", # <--- PEGA AQUÍ TU LINK DE AFILIADO
        "legal": "Depósito mín. S/20 | Rollover x3",
        "autorizado": True
    },
    {
        "id": 3,
        "nombre": "Inkabet",
        "logo": "https://seeklogo.com/images/I/inkabet-logo-36B6F68414-seeklogo.com.png",
        "etiqueta": "100% PERUANA",
        "etiqueta_color": "#f8f9fa", # Blanco hueso
        "etiqueta_texto_color": "#333",
        "puntuacion": "4.7",
        "bono_titulo": "DUPLICA TU 1ER DEPÓSITO",
        "bono_desc": "Hasta S/800 de Bono", # <--- EDITA ESTO
        "link": "https://www.inkabet.pe", # <--- PEGA AQUÍ TU LINK DE AFILIADO
        "legal": "18+ | Juega Responsable",
        "autorizado": True
    },
    {
        "id": 4,
        "nombre": "Coolbet",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/1/13/Coolbet_logo.png",
        "etiqueta": "MEJORES CUOTAS",
        "etiqueta_color": "#000", 
        "etiqueta_texto_color": "#fff",
        "puntuacion": "4.9",
        "bono_titulo": "BONO BIENVENIDA",
        "bono_desc": "100% hasta S/400", # <--- EDITA ESTO
        "link": "https://www.coolbet.com", # <--- PEGA AQUÍ TU LINK DE AFILIADO
        "legal": "18+ | TyC Aplican",
        "autorizado": True
    }
]

# --- RUTAS DE LA PÁGINA ---

@app.route('/')
def home():
    return render_template('index.html', casas=CASAS, config=SITE_CONFIG)

# ¡ESTAS SON LAS RUTAS QUE FALTABAN PARA QUE FUNCIONEN LOS LINKS DEL FOOTER!
@app.route('/terminos-y-condiciones')
def terminos():
    return render_template('legal_terms.html', config=SITE_CONFIG)

@app.route('/politica-de-privacidad')
def privacidad():
    return render_template('legal_privacy.html', config=SITE_CONFIG)

@app.route('/juego-responsable')
def juego_responsable():
    return render_template('legal_responsible.html', config=SITE_CONFIG)

if __name__ == '__main__':
    app.run(debug=True)