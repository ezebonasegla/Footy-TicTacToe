import argparse
import json
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('url', help='La URL del sitio web')
parser.add_argument('equipo', help='El nombre del equipo para el archivo de salida')
args = parser.parse_args()
response = requests.get(args.url)
soup = BeautifulSoup(response.content, 'html.parser')

jugadores = []

tabla_jugadores = soup.find('table', {'class': 'standard_tabelle'})
filas = tabla_jugadores.find_all('tr')

for fila in filas[2:]:
    datos = fila.find_all('td')
    if len(datos) == 5:
        nombre = datos[0].text.strip()
        pais = datos[2].text.strip() if datos[2].find('img') is None else datos[3].text.strip()
        posicion = datos[3].text.strip() if datos[2].find('img') is None else datos[4].text.strip()
        fecha_nacimiento = datos[4].text.strip()
        if fecha_nacimiento and nombre and pais and posicion and int(fecha_nacimiento[-4:]) > 1939:
            jugador = {'nombre': nombre, 'pais': pais, 'posicion': posicion, 'fecha_nacimiento': fecha_nacimiento}
            jugadores.append(jugador)

with open(f"{args.equipo}.json", 'w', encoding='utf-8') as f:
    json.dump(jugadores, f, ensure_ascii=False, indent=4)

with open(f"{args.equipo}.json", 'r', encoding='iso-8859-1') as f:
    contenido = f.read()

contenido_modificado = contenido.encode('iso-8859-1').decode('utf-8')

with open(f"{args.equipo}.json", 'w', encoding='utf-8') as f:
    f.write(contenido_modificado)





