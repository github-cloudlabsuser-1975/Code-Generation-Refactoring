import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

OPENWEATHER_API_KEY = 'TU_API_KEY_AQUI'  # Reemplaza con tu clave de OpenWeatherMap

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'Falta el parámetro city'}), 400

    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric',
        'lang': 'es'
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return jsonify({'error': 'No se pudo obtener el clima'}), response.status_code

    data = response.json()
    weather = {
        'ciudad': data['name'],
        'temperatura': data['main']['temp'],
        'descripcion': data['weather'][0]['description'],
        'humedad': data['main']['humidity'],
        'viento': data['wind']['speed']
    }
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)