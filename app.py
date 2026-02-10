from flask import Flask, render_template

app = Flask(__name__)

# --- BASE DE DATOS REAL (PERÚ 2026) ---
CASAS = [
    {
        "id": "betano",
        "name": "Betano",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/2/22/Betano_Logo_2024.svg",
        "stars": "⭐⭐⭐⭐⭐",
        "rating_num": "5.0",
        "bonus_short": "S/500 GRATIS",
        "bonus_desc": "Bono de Bienvenida + S/75 Apuesta Gratis",
        "code": "BETAPE", # Tu código para SEO
        "pros": ["Pagos con Yape/Plin", "App Android/iOS", "Cuotas Mejoradas"],
        "rollover": "x7.5",
        "link": "https://www.betano.pe/myaccount/register/" # CAMBIA ESTO POR TU LINK DE AFILIADO
    },
    {
        "id": "bet365",
        "name": "Bet365",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Bet365_Logo.svg/1024px-Bet365_Logo.svg.png",
        "stars": "⭐⭐⭐⭐⭐",
        "rating_num": "4.9",
        "bonus_short": "S/500 BONO",
        "bonus_desc": "50% de créditos de apuesta extra",
        "code": "365LATAM",
        "pros": ["Líder Mundial", "Streaming HD", "Retiro Instantáneo"],
        "rollover": "x1",
        "link": "https://www.bet365.com/olp/open-account" # CAMBIA ESTO POR TU LINK DE AFILIADO
    },
    {
        "id": "inkabet",
        "name": "Inkabet",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/04/Inkabet_Logo.png",
        "stars": "⭐⭐⭐⭐☆",
        "rating_num": "4.7",
        "bonus_short": "S/10 GRATIS",
        "bonus_desc": "S/10 por registrarte sin depósito",
        "code": "INKAMAX",
        "pros": ["Casa 100% Peruana", "Bonos de Recarga", "Atención WhatsApp"],
        "rollover": "x10",
        "link": "https://www.inkabet.pe/registro" # CAMBIA ESTO POR TU LINK DE AFILIADO
    }
]

@app.route('/')
def index():
    return render_template('index.html', casas=CASAS)

if __name__ == '__main__':
    app.run(debug=True)