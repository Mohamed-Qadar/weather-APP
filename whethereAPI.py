import os
import tkinter as tk
from tkinter import*
import requests
#from PIL import Image, Image
import time
from geopy.geocoders import nominatim
from tkinter import ttk,messagebox
from timezonefinder import  TimezoneFinder
from datetime import datetime
from tkinter import PhotoImage
import pytz


def getWeather(canvas):
    city = textField.get()
    #this is API address.
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=aa4a2100d2a44744ff2de50f8ea9c566"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    #local time, this is basic on GMT+03
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 32400))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 32400))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("900x500+300+200")
#canvas.geometry("600x500")
canvas.title("Weather App")
"""
#searchbox
#self.bg = tk.PhotoImage(file="black.png")
sear =photoImage(file ="black.png")
label1 =Label(image=sear)
label1.place(x=20,y=20)

textField = tk.Entry(canvas, justify='center', width = 20, font = ("poppins", 15, "bold"),bg ="404040",border=0,fg="white")
textField.place(x=50,y=40)
textField.focus()
textField.bind('<Return>', getWeather)

search_ico =photoImage(file ="search.png")
myimag_ico =Button(image=search_ico,borderwidth=0,cursor="hand2",bg="#404040")
myimag_ico.place(x=400,y=34)

#log
log_image =photoImage(file ="weather.png")
label2 =Label(image=log_image)
label2.place(x=150,y=100)
"""


canvas.geometry("600x500")
canvas.title("Weather App")
B = tk.Button(canvas, text ="Weather APP", fg="GREEN")
B.pack()
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")


textField = tk.Entry(canvas, justify='center', width = 20, font = t,fg="BLUE")
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()