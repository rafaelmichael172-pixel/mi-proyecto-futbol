from flask import Flask, render_template

app = Flask(__name__)

# DATOS DE LA WEB (Fáciles de editar)
SITE_CONFIG = {
    "nombre": "TopApuestas Perú",
    "dominio": "topapuestas.pe",  # Cambia esto cuando tengas dominio
    "contacto": "contacto@topapuestas.pe"
}

# DATOS DE LAS CASAS (Tus "Productos")
CASAS = [
    {
        "id": 1,
        "nombre": "Betano",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Betano_Logo.png",
        "etiqueta": "MEJOR EN PERÚ",
        "etiqueta_color": "#ff4b4b", # Rojo vibrante
        "etiqueta_texto_color": "#ffffff",
        "puntuacion": "4.9",
        "estrellas": 5,
        "bono_titulo": "BONO EXCLUSIVO",
        "bono_desc": "S/500 + 20% Extra",
        "link": "https://tu-link-afiliado.com/betano", # <--- TU LINK AQUÍ
        "legal": "18+ | Aplican T&C | Nuevos usuarios",
        "autorizado": True
    },
    {
        "id": 2,
        "nombre": "Betsson",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Betsson_Logo.png",
        "etiqueta": "PAGOS RÁPIDOS",
        "etiqueta_color": "#ff9900", # Naranja
        "etiqueta_texto_color": "#000000",
        "puntuacion": "4.8",
        "estrellas": 5,
        "bono_titulo": "APUESTA GRATUITA",
        "bono_desc": "S/40 Gratis o Cero Riesgo",
        "link": "https://tu-link-afiliado.com/betsson", # <--- TU LINK AQUÍ
        "legal": "Depósito mín. S/20 | Rollover x3",
        "autorizado": True
    },
    {
        "id": 3,
        "nombre": "Inkabet",
        "logo": "https://seeklogo.com/images/I/inkabet-logo-36B6F68414-seeklogo.com.png",
        "etiqueta": "100% PERUANA",
        "etiqueta_color": "#f8f9fa",
        "etiqueta_texto_color": "#333",
        "puntuacion": "4.7",
        "estrellas": 4,
        "bono_titulo": "DUPLICA TU 1ER DEPÓSITO",
        "bono_desc": "Hasta S/800 de Bono",
        "link": "https://tu-link-afiliado.com/inkabet", # <--- TU LINK AQUÍ
        "legal": "18+ | Juega Responsable",
        "autorizado": True
    }
]

@app.route('/')
def home():
    return render_template('index.html', casas=CASAS, config=SITE_CONFIG)

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