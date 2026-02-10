from flask import Flask, render_template

app = Flask(__name__)

# --- BASE DE DATOS MAESTRA (INFORMACIÓN REAL PERÚ 2026) ---
CASAS = [
    {
        "id": "betano",
        "name": "Betano",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/2/22/Betano_Logo_2024.svg",
        "rating": "5.0",
        "stars": "⭐⭐⭐⭐⭐",
        "bonus_short": "S/500 GRATIS",
        "bonus_full": "100% hasta S/500 + S/75 en Apuesta Gratis",
        "pros": ["App premiada 2025", "Pagos al toque con Yape", "Transmisión en vivo"],
        "rollover": "x7.5 en cuotas 1.80",
        "min_dep": "S/30",
        "link": "#", # AQUÍ PONDRÁS TU LINK DE AFILIADO
        "review": "Betano es el líder indiscutible en Perú. Su plataforma es la más rápida y ofrecen las mejores cuotas en la Liga 1."
    },
    {
        "id": "bet365",
        "name": "Bet365",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Bet365_Logo.svg/1024px-Bet365_Logo.svg.png",
        "rating": "4.9",
        "stars": "⭐⭐⭐⭐⭐",
        "bonus_short": "$30 USD EXTRA",
        "bonus_full": "Hasta $30 en créditos de apuesta",
        "pros": ["El mejor streaming del mundo", "Crear apuesta personalizada", "Retiro parcial"],
        "rollover": "x1 en cuota 1.20",
        "min_dep": "S/40",
        "link": "#",
        "review": "La casa más grande del mundo. Si buscas variedad de mercados y seguridad total, Bet365 es tu lugar."
    },
    {
        "id": "1xbet",
        "name": "1xBet",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/1xBet_Logo_2022.svg/1200px-1xBet_Logo_2022.svg.png",
        "rating": "4.7",
        "stars": "⭐⭐⭐⭐☆",
        "bonus_short": "S/450 BONO",
        "bonus_full": "Bono de bienvenida exclusivo de S/450",
        "pros": ["Miles de eventos diarios", "Acepta Criptomonedas", "Bonos de recarga"],
        "rollover": "x5 en apuestas combinadas",
        "min_dep": "S/4",
        "link": "#",
        "review": "Ideal para quienes buscan cuotas altísimas y métodos de pago alternativos como Bitcoin o USDT."
    }
]

@app.route('/')
def index():
    return render_template('index.html', casas=CASAS)

@app.route('/resena/<id_casa>')
def resena(id_casa):
    casa = next((c for c in CASAS if c["id"] == id_casa), None)
    if casa:
        return render_template('resena.html', casa=casa)
    return "Error: Casa no encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)