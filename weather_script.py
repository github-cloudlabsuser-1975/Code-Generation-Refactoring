import requests

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Fetches weather data for a given city using OpenWeatherMap API.

    Args:
        city_name (str): Name of the city.

    Returns:
        dict: Weather data if successful, None otherwise.
    """
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(data):
    """
    Displays weather information.

    Args:
        data (dict): Weather data.
    """
    if data:
        city = data.get("name")
        temp = data["main"].get("temp")
        weather = data["weather"][0].get("description")
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather.capitalize()}")
    else:
        print("No weather data available.")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)