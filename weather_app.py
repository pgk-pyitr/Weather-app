import requests

def get_weather(city, api_key):
    """
    Fetch the weather data for a given city using OpenWeatherMap API.

    Parameters:
    city (str): The name of the city.
    api_key (str): Your OpenWeatherMap API key.

    Returns:
    dict: A dictionary containing weather data.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()