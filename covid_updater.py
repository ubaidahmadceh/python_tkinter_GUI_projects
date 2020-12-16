import requests
from tkinter import *
import tkinter.messagebox
import json

root=Tk()

def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'
    
    x = 0
    while x < 1:
        tkinter.messagebox.showinfo('Covid-19 updater', text)
        x += 1

update()

root.mainloop()