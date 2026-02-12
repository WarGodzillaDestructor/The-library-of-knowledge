import requests 
from bs4 import BeautifulSoup 
import json 

def extraer_cotacizaciones(url):
    response = requests.get(url)
    html = response.text
    
    # Parsear HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Encontrar todas las cotizaciones
    quotes = []

    for quote_div in soup.find_all('div', class_='quote'):
        texto = quote_div.find('span', class_='text').text
        autor = quote_div.find('small', class_='author').text
        quotes.append({
            'texto': texto,
            'autor': autor
        })
    return quotes
    
def guardar_json(datos, archivo):
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)
url = "http://quotes.toscrape.com" 
print("Extrayendo cotazicaciones")

quotes = extraer_cotacizaciones(url)
print(f"Encontradas: {len(quotes)}")
    
    # Mostrar primeras 3
for quote in quotes[:3]:
        print(quote['texto'])
        print(f"  - {quote['autor']}") 
        guardar_json(quotes, 'cotizaciones.json')
        print("Guardadas en cotizaciones.json")