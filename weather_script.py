try:
    import requests
except ModuleNotFoundError:
    print("The 'requests' module is not installed. Please install it by running:")
    print("    pip install requests")
    exit(1)

def fetch_weather(api_key, city):
    """
    Fetch weather data for a given city from OpenWeatherMap API.

    Args:
        api_key (str): Your OpenWeatherMap API key.
        city (str): City name.

    Returns:
        dict: Weather data as returned by the API, or None if error.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather_info(weather_data):
    """
    Display temperature, humidity, and weather conditions from weather data.

    Args:
        weather_data (dict): Weather data as returned by fetch_weather.
    """
    if not weather_data:
        print("No weather data to display.")
        return

    try:
        temp_k = weather_data['main']['temp']
        temp_c = temp_k - 273.15
        humidity = weather_data['main']['humidity']
        condition = weather_data['weather'][0]['description']
        print(f"Temperature: {temp_c:.2f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {condition.capitalize()}")
    except (KeyError, IndexError, TypeError):
        print("Error: Unexpected weather data format.")

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        data = fetch_weather(api_key, city)
        display_weather_info(data)
