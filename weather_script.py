import requests

def get_weather(lat, lon, exclude="minutely,hourly", api_key="ee97033f0fba141f87d70af37d124965"):
    """
    Fetch weather data from OpenWeather API.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        exclude (str): Data to exclude from the response (default: "minutely,hourly").
        api_key (str): Your OpenWeather API key.

    Returns:
        dict: Weather data as a dictionary.
    """
    url = f"https://api.openweathermap.org/data/3.0/onecall"
    params = {
        "lat": lat,
        "lon": lon,
        "exclude": exclude,
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    latitude = 40.7128  # Replace with desired latitude
    longitude = -74.0060  # Replace with desired longitude

    weather_data = get_weather(latitude, longitude)
    if weather_data:
        print("Weather Data:")
        print(weather_data)
    else:
        print("Failed to retrieve weather data.")

        