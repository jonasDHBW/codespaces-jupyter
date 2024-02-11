
import requests



def get_weather(api_key, city):

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)

    data = response.json()



    if data['cod'] == 200:

        weather_info = {

            'city': data['name'],

            'description': data['weather'][0]['description'],

            'temperature': data['main']['temp'],

            'humidity': data['main']['humidity'],

            'wind_speed': data['wind']['speed'],

        }

        return weather_info

    else:

        return None



def main():

    api_key = 'YOUR_API_KEY'

    city = input("Enter city name: ")

    weather_info = get_weather(api_key, city)



    if weather_info:

        print(f"Weather in {weather_info['city']}:")

        print(f"Description: {weather_info['description']}")

        print(f"Temperature: {weather_info['temperature']}°C")

        print(f"Humidity: {weather_info['humidity']}%")

        print(f"Wind Speed: {weather_info['wind_speed']} m/s")

    else:

        print("Failed to fetch weather data.")



if __name__ == "__main__":

    main()



