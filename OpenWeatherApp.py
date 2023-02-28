#Created by Michael Speer
#Created on 02/13/2022
#Created for CIS245-T301

#This is a simple Python program that interfaces with a user via the console window
#and pulls weather information from the openweathermap.org API
#Thanks for looking!

import requests

api_key = {your key here}

def display_weather(data):
    """displays weather passed to it from get_weather"""
    
    location = data['name']
    t_current = data['main']['temp']
    print(f"\nThe current temperature in {location} is {t_current} degrees fahrenheit\n")

    t_max = data['main']['temp_max']
    print(f"The forecasted maximum temperature for the day is {t_max} degrees fahrenheit\n")

    t_min = data['main']['temp_min']
    print(f"The forecasted minimum temperature for the day is {t_min} degrees fahrenheit\n")

    weather_description = data['weather'][0]['description']
    print(f"The weather is {weather_description}\n")

def get_weather(location):    
    """gets weather and displays error codes"""

    url = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&units=imperial&appid="+api_key
    r = requests.get(url)
    data = r.json()

    display_weather(data)

while True:
    user_input = input(f"What is the Zip Code or Name of the location you would like weather for? \nType 'q' to quit \n\n")
    if user_input.lower() == 'q':
        break

    else:        
        try:
            get_weather(user_input)
        except:
            print(f"\nSomething went wrong, try again.\nMake sure your inputs are valid and you are connected to the internet.\n")
