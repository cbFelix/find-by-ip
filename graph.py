import geocoder
import folium
import webbrowser
import os
from tkinter import *


def find():
    ip_address = ip_entry.get()
    g = geocoder.ip(ip_address)

    my_address = g.latlng
    location2.config(text=f'{my_address[0]}, {my_address[1]}')
    city2.config(text=f'{g.city}')

    map1 = folium.Map(location=my_address, zoom_start=10)

    folium.CircleMarker(my_address, radius=50, popup="Location", fill_color="red", color='red').add_to(map1)

    folium.Marker(my_address, popup=f'{ip_address}, {g.city}').add_to(map1)


def open_web_map():
    webbrowser.open("myMap.html")


root = Tk()
root.geometry('300x100')
root.title('Find By IP')

ip_entry = Entry(root, width=30)
ip_entry.grid(column=0, row=0)

find_btn = Button(root, text='Find', command=lambda: find(), width=8)
find_btn.grid(column=1, row=0)

location1 = Label(root, text='Location: ')
location1.grid(column=0, row=1)
location2 = Label(root, text='')
location2.grid(column=1, row=1)

city1 = Label(root, text='City: ')
city1.grid(column=0, row=2)
city2 = Label(root, text='')
city2.grid(column=1, row=2)

open_map_btn = Button(root, text='Open Map', command=lambda: open_web_map())
open_map_btn.grid(column=0, row=3)

author_label = Label(root, text='Author: @cbFelix')
author_label.grid(column=1, row=3)

root.mainloop()