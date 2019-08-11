#import modules
import requests
import tkinter as tk
from tkinter import font

height = 700
width = 800

def get_weather(city):
	try:
		api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
		url = api_address+city
		weather_data = requests.get(url).json()
		name = weather_data['name']
		description = weather_data['weather'][0]['description']
		temp = weather_data['main']['temp']
		wind_speed = weather_data['wind']['speed']

		lower_label['text'] = "Name: "+name+"\n"+"Desc: "+description+"\n"+"Temp: "+str(temp)+"\n"+"Wind-speed: "+str(wind_speed)
	except:
		lower_label['text'] = "'"+city+"'"+"\n"+"Not found!"+"\n"+"Try again!!"

root = tk.Tk()

canvas = tk.Canvas(root,height=height,width=width)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg="#234873",bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry = tk.Entry(frame,font=20)
entry.place(relwidth=0.73,relheight=1)

button = tk.Button(frame, text="Get Weather",font=40,command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')

lower_label = tk.Label(lower_frame,font=('Rubik',35))
lower_label.place(relwidth=1,relheight=1)

root.mainloop()