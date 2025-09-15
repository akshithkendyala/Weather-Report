import requests

api_key = "51757a6270996799bfda91996288713e"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json() #a JSON string is converted to python dictionary
        #Now "data" is a dictionary with keys => coord, weather, base, main, visibility, wind, clouds, dt, sys, timezone, id, name, cod
        #name => city name
        #weather => list of weather condition dictionaries(main description, icons)
        #main => dictionary with temperature, pressure, humidity, feels_like

        print(f"\n--- Weather report for {data['name']} ---")
        print(f"Condition   : {data['weather'][0]['description'].capitalize()}")
        print(f"Temperature : {data['main']['temp']}°C")
        print(f"Pressure : {data['main']['pressure'] } hPa")
        print(f"Humidity    : {data['main']['humidity']}%")
        print("-------------------------------------------\n")

    elif response.status_code == 404:
        print("Not Found: Wrong city name or city doesn't exist.")
    
    elif response.status_code == 401:
        print("Unauthorized: Missing or invalid API key.")
    
    elif response.status_code == 500:
        print("Internal Server Error: Something went wrong on the server.")
    
    else:
        print(f"Service temporarily down. Status code: {response.status_code}")


while True:
    city = input("Enter city name (or 'exit' to quit): ").strip()
    if city.lower() == "exit":
        print("Bye, Stay safe!\n")
        break
    get_weather(city)
