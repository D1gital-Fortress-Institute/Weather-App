import tkinter as tk
from tkinter import *
import requests
import json
from datetime import datetime

def create_label_frames():
    global entry_label_frame, search_label_frame, output_label_frame
    entry_label_frame = tk.LabelFrame(root, borderwidth=0).grid(row=0, column=0, pady=40)
    search_label_frame = tk.LabelFrame(root, borderwidth=0).grid(row=1, column=0, pady=10)
    output_label_frame = tk.LabelFrame(root, borderwidth=0).grid(row=2, column=0, pady=10)


def display_search_entry():
    global city_value

    city_value = tk.StringVar()
    name_label = tk.Label(entry_label_frame, text="Enter City Name", width=20, height=2, background='green', font=('Bookman Old Style', 10, 'bold')).grid(row=0, column=0, padx=105)
    entry_label = tk.Entry(entry_label_frame, textvariable=city_value, width=20, font=('Bookman Old Style', 20)).grid(row=1, column=0)

def display_search_button():
    search_button = tk.Button(search_label_frame, text='Search', width=10, height=1, background='orange', foreground='green', command=show_weather).grid(columnspan=4, pady=10)

def display_searched_text():
    global text_output
    text_output = tk.Text(output_label_frame, width=46, height=10)
    text_output.grid(row=4, column=0, pady=10)

def show_weather():

    weather_api_key: str = 'e0217999c31130be17da630cb27671f0'
    city_name = city_value.get()


    weather_url_path = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + weather_api_key

    response: object = requests.get(weather_url_path)

    weather_info = response.json()


    if weather_info['cod'] == 200:
        kelvin = 273

        temperature = int(weather_info['main']['temp'] - kelvin)
        feels_like = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure'] 
        humidity = weather_info['main']['humidity'] 
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']


        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temperature} \nFeels like in (celsius): {feels_like}\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description} "
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
    
    text_output.insert(0, weather)
    


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()



if __name__=='__main__':
    root = tk.Tk()
    root.title('Weather App')
    root.geometry('400x400')
    root.config(background='black')
    root.resizable(0, 0)


    # Call The Functions
    create_label_frames()
    display_search_entry()
    display_search_button()
    display_searched_text()

    root.mainloop()