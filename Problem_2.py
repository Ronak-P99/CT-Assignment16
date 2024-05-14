# Weather Forecast Application Script
class Weather:
    def __init__(self):
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
    }

    def fetch_weather_data(self, city):
    # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})

    def parse_weather_data(self, city):
    # Function to parse weather data
        if not self.weather_data:
            return "Weather data not available"
        temperature = self.weather_data[city]["temperature"]
        condition = self.weather_data[city]["condition"]
        humidity = self.weather_data[city]["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    def get_detailed_forecast(self, city):
        # Function to provide a detailed weather forecast for a city
        data = self.fetch_weather_data(city)
        return print(data)

    def display_weather(self, city):
    # Function to display the basic weather forecast for a city
        forecast = self.fetch_weather_data(city)
        if not forecast:
            print(f"Weather data not available for {city}")
        else:
            parsed_weather = self.parse_weather_data(city)
            print(parsed_weather)

def main():
    my_weather = Weather()
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            my_weather.get_detailed_forecast(city)
        else:
            my_weather.display_weather(city)
if __name__ == "__main__":
    main()