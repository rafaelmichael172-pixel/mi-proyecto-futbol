import requests

# Tu llave recién obtenida
NUEVA_LLAVE = "F7fd1f2d10a43c5f2a0568e73fe2f0c9"

# URL para ver partidos en vivo
url = "https://v3.football.api-sports.io/fixtures?live=all"

headers = {
    'x-apisports-key': NUEVA_LLAVE
}

print("--- Intentando conectar con el servidor de fútbol... ---")

try:
    response = requests.get(url, headers=headers)
    datos = response.json()

    if response.status_code == 200:
        # Verificamos si la llave es válida según la respuesta del servidor
        if datos.get("errors"):
            print("Error detectado:", datos["errors"])
        else:
            partidos = datos.get('response', [])
            if not partidos:
                print("¡Conexión exitosa! Pero no hay partidos en vivo justo ahora.")
                print("Prueba mañana o en un rato cuando haya jornada.")
            else:
                print(f"¡LOGRADO! Se encontraron {len(partidos)} partidos en vivo.\n")
                for p in partidos[:10]:
                    local = p['teams']['home']['name']
                    visitante = p['teams']['away']['name']
                    liga = p['league']['name']
                    print(f"⚽ [{liga}] {local} vs {visitante}")
    else:
        print(f"Error de red. Código: {response.status_code}")

except Exception as e:
    print(f"Ocurrió un error: {e}")