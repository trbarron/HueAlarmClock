import pyowm
from phue import Bridge
import csv
import colorsys

#Connect to lights
b = Bridge('xxx.xxx.xxx.xxx') #Replace with your IP here
b.connect()
lights = b.lights

#Connect to weather service
owm = pyowm.OWM('ohyoudontgetmykey')  # You MUST provide a valid API key, replace with yours

#Get weather for seattle for the next day
fc = owm.daily_forecast('Seattle, WA', limit=1)
f = fc.get_forecast()
for weather in f:
    j = weather.get_weather_code()
j = 500

#Lookup weather code, set colors
f = open('C:\Filepathhere\weatherScenes.csv', 'rt') #point it towards CSV
reader = csv.DictReader(f)
for w in reader:
    if int(w['ID']) == j:
        break

#set lights to assigned color
for i in range(0,3):
    R = w["L"+str(i+1)+"R"]
    G = w["L"+str(i+1)+"G"]
    B = w["L"+str(i+1)+"B"]
    [hue, bri, sat] = colorsys.rgb_to_hls(float(R)/255,float(G)/255,float(B)/255)
    lights[i].hue = hue*65535
    lights[i].saturation = int(sat*255)
    lights[i].brightness = int(bri*255)
