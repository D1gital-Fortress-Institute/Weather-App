from tkinter import *
import requests
import json
from datetime import datetime



# Function to show weather
def show_weather():

    weather_api_key = "e0217999c31130be17da630cb27671f0"

    city_name = city_value.get()


    weather_api_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + weather_api_key

    # Get the response from fetched url
    response = requests.get(weather_api_url)


    # Change the response from json to python readable
    weather_info = response.json()


    # Clear the text field for every new output
    tfield.delete("1.0", "end") 

    # In the API documentation, if the cod is 200, it means that the weather's data was successfully fetched

    if weather_info['cod'] == 200:
        kelvin = 273 #Value of temperature

        # Storing the fetched values of weather of a city

        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        #Assigning values to our weather variable, to display as output

        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp} \nFeels like in (celsius): {feels_like_temp}\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description} "
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(INSERT, weather)


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()



if __name__=='__main__':

    # Main Window Screen
    window = Tk()
    window.geometry("400x400")
    window.resizable(0, 0)

    window.title("Weather App")

    city_value = StringVar()

    city_head = Label(window, text = 'Enter City Name: ', font = 'Arial 12 bold').pack(pady=10)

    city_input = Entry(window, textvariable=city_value, width=24, font='Arial 14 bold').pack()

    Button(window, command = show_weather, text = "Check Weather", font="Arial 10", bg='blue', fg="white", activebackground='green', padx=5, pady=5).pack(pady=20)

    weather_now = Label(window, text="The Weather is: ", font = 'arial 12 bold').pack(pady=10)

    tfield = Text(window, width=46, height=10)
    tfield.pack()

    window.mainloop()

