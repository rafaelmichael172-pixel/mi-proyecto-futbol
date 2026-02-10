from flask import Flask, render_template

app = Flask(__name__)

# --- BASE DE DATOS DE AFILIADOS (DATOS REALES PERÚ 2026) ---
# Aquí configuras todo. Los logos ya están listos con enlaces públicos.
CASAS = [
    {
        "id": "betano",
        "name": "Betano",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/2/22/Betano_Logo_2024.svg",
        "rating": 5.0,
        "stars": "⭐⭐⭐⭐⭐",
        "bonus_title": "Bono del 100% hasta S/500",
        "pros": ["App Móvil #1 en el Mundo", "Pagos inmediatos", "Supercuotas"],
        "rollover": "Rollover x7.5 | Min. Dep S/30",
        "affiliate_link": "#", # CAMBIA ESTO POR TU LINK DE AFILIADO
        "review_text": "Betano es actualmente el rey de Latinoamérica. Su app es insuperable y pagan en minutos."
    },
    {
        "id": "bet365",
        "name": "Bet365",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Bet365_Logo.svg/2560px-Bet365_Logo.svg.png",
        "rating": 4.9,
        "stars": "⭐⭐⭐⭐⭐",
        "bonus_title": "S/100 en Créditos de Apuesta",
        "pros": ["Mejor Streaming en Vivo", "Líder Mundial", "Crear Apuesta+"],
        "rollover": "Rollover x1 | Cuota 1.20",
        "affiliate_link": "#",
        "review_text": "La casa de apuestas más grande del mundo. Si te gusta apostar en vivo viendo el partido, esta es tu opción."
    },
    {
        "id": "inkabet",
        "name": "Inkabet",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/04/Inkabet_Logo.png", # Si falla, usa un placeholder
        "rating": 4.7,
        "stars": "⭐⭐⭐⭐☆",
        "bonus_title": "S/10 GRATIS + Duplica tu Saldo",
        "pros": ["Marca 100% Peruana", "Acepta Yape y Plin", "Atención local"],
        "rollover": "Rollover x10 | Bono x5",
        "affiliate_link": "#",
        "review_text": "La casa del pueblo. Inkabet entiende al peruano y acepta todos nuestros métodos de pago locales."
    },
    {
        "id": "1xbet",
        "name": "1xBet",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/1xBet_Logo_2022.svg/1200px-1xBet_Logo_2022.svg.png",
        "rating": 4.5,
        "stars": "⭐⭐⭐⭐☆",
        "bonus_title": "S/450 con tu Primer Depósito",
        "pros": ["Mayor catálogo de eventos", "Cuotas Altas", "Depósitos cripto"],
        "rollover": "Rollover x5 en Combinadas",
        "affiliate_link": "#",
        "review_text": "Gigante ruso con cuotas brutales, aunque su página puede ser un poco confusa para novatos."
    }
]

@app.route('/')
def index():
    return render_template('index.html', casas=CASAS)

@app.route('/resena/<id_casa>')
def resena(id_casa):
    # Busca la casa específica en nuestra "base de datos"
    casa_encontrada = next((c for c in CASAS if c["id"] == id_casa), None)
    if casa_encontrada:
        return render_template('resena.html', casa=casa_encontrada)
    return "Casa no encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)