	• get_weather(city, api_key): This function constructs the URL for the API request using the city name and API key, makes the request using requests.get(), and returns the JSON response as a dictionary.
	• display_weather(weather_data): This function takes the weather data dictionary and prints the weather information in a readable format. It also handles the case where the city is not found.
	• main(): This is the main function that prompts the user for a city name, fetches the weather data, and displays it.