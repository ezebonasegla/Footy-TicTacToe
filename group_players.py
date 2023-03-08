import os
import json

players = []
clubs = {}

# Recorrer todos los archivos JSON
for filename in os.listdir():
    if not filename.endswith('.json') or filename == 'data.json':
        continue

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

        # Recorrer todos los jugadores en el archivo JSON
        for player in data:
            # Crear una clave única para cada jugador
            key = (
                player['nombre'],
                player['pais'],
                player['posicion'],
                player['fecha_nacimiento']
            )

            # Agregar el club actual a la lista de clubes del jugador
            clubs.setdefault(key, []).append(filename[:-5])

# Recorrer todos los jugadores y agregar la lista de clubes correspondiente
for key, club_list in clubs.items():
    player = {
        'nombre': key[0],
        'pais': key[1],
        'posicion': key[2],
        'fecha_nacimiento': key[3],
        'clubes': club_list
    }

    # Agregar el jugador a la lista de jugadores
    players.append(player)

# Guardar la lista de jugadores en un archivo JSON
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(players, file, ensure_ascii=False, indent=4)
