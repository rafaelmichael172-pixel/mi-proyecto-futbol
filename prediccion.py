import requests

# Tu llave que ya sabemos que funciona
NUEVA_LLAVE = "F7fd1f2d10a43c5f2a0568e73fe2f0c9"
url = "https://v3.football.api-sports.io/fixtures?live=all"

headers = {'x-apisports-key': NUEVA_LLAVE}

print("--- ANALIZANDO PARTIDOS EN VIVO PARA PRONÓSTICOS ---")

response = requests.get(url, headers=headers)
datos = response.json()
partidos = datos.get('response', [])

for p in partidos:
    # 1. Obtenemos datos básicos
    local = p['teams']['home']['name']
    visitante = p['teams']['away']['name']
    
    # 2. Intentamos obtener las estadísticas de tiros y córners
    # Nota: No todas las ligas pequeñas dan estadísticas en vivo, por eso validamos
    stats = p.get('statistics', [])
    
    if stats:
        # Aquí es donde ocurre la magia del programador
        # Extraemos tiros a puerta y córners para el cálculo
        print(f"\n📊 Análisis: {local} vs {visitante}")
        
        # Filtramos los datos de la API (Tiros a puerta y Córners)
        # Este es el inicio de tu algoritmo de 'Goles Esperados'
        for s in stats:
            equipo = s['team']['name']
            tiros = next((item['value'] for item in s['statistics'] if item['type'] == 'Shots on Goal'), 0)
            corners = next((item['value'] for item in s['statistics'] if item['type'] == 'Corner Kicks'), 0)
            
            # Si un equipo tiene muchos tiros y corners, su probabilidad de gol sube
            if tiros and tiros > 4:
                print(f"   🔥 AVISO: {equipo} está presionando mucho ({tiros} tiros a puerta).")
            
            print(f"   - {equipo}: {tiros} Tiros a puerta | {corners} Córners")
    else:
        print(f"\n⚽ {local} vs {visitante} (Sin estadísticas detalladas en vivo aún)")
       




       