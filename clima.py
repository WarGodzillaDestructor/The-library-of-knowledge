
import json 
import requests 

def reecibir_clima(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    params = {
    "q": ciudad,
    "appid": api_key,
    "units": "metric",
    "lang": "es"
}

    respuesta = requests.get(url, params=params)

    try:
        respuesta = requests.get(url, params=params)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            clima = datos['weather'][0]['description']
            temperatura = datos['main']['temp']
            humedad = datos['main']['humidity']
            sensacion_termica = datos['main']['feels_like']
            presion = datos['main']['pressure']
            temperatura_minima = datos['main']['temp_min']
            temperatura_maxima = datos['main']['temp_max']
            print(f"Clima en {ciudad}: {clima}")
            print(f"Temperatura: {temperatura}°C")
            print(f"Humedad: {humedad}%")
            print(f"Sensación térmica: {sensacion_termica}°C")
            print(f"Presión: {presion} hPa")
            print(f"Temperatura mínima: {temperatura_minima}°C")
            print(f"Temperatura máxima: {temperatura_maxima}°C")
        else:
            print(f"Error {respuesta.status_code}: ¿Escribiste bien la ciudad?")
    except Exception as e:
        print(f"Hubo un problema de conexión: {e}")
    
if __name__ == "__main__":
    ciudad = input("Ingresa el nombre de la ciudad: ").strip().title()
    api_key = input("Ingresa tu API Key de OpenWeatherMap: ").strip()
    reecibir_clima(ciudad, api_key)