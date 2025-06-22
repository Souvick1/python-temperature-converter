
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temp}°C")
    else:
        print("City not found or error fetching data.")

if __name__ == "__main__":
    api_key = "51.5085"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    get_weather(city, api_key)
