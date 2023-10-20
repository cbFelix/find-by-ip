import geocoder
import folium
import webbrowser
import argparse
import time

print('''
By using the software you agree to the rules written in the file "Rules-for-using-software.txt"!
''')

time.sleep(3)

parser = argparse.ArgumentParser(description='Find IP address location and open a web map.')

parser.add_argument('--web-map', action='store_true', help='Open web map in browser')
parser.add_argument('--target', required=True, help='Specify the target IP address')

args = parser.parse_args()


def find():
    ip_address = args.target
    g = geocoder.ip(ip_address)

    my_address = g.latlng
    print(f"{my_address[0]}, {my_address[1]}")
    for i in g:
        print(i)

    map1 = folium.Map(location=my_address, zoom_start=10)

    folium.CircleMarker(my_address, radius=50, popup=f'{ip_address}, {g.city}', fill_color="red", color='red').add_to(map1)

    folium.Marker(my_address, popup=f'{ip_address}, {g.city}').add_to(map1)

    map1.save('myMap.html')
    print('Web map saved as "myMap.html"')

    if args.web_map:
        webbrowser.open("myMap.html")


find()