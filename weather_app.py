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
def display_weather(weather_data):
    """
    Display the weather data in a readable format.

    Parameters:
    weather_data (dict): The weather data dictionary.
    """
    if weather_data.get("cod") != 200:
        print("City not found!")
        return

    city = weather_data["name"]
    temp = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")