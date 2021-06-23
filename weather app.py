import requests
import csv
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
w_data=[["PLACE","TEMPERATURE","WEATHER","HUMIDITY","SPEED","DATE_TIME"],[location,temp_city,"deg C" ,weather_desc,hmdt,"%",wind_spd,date_time]]
csv.register_dialect("custom",delimiter='|')
with open('weather.txt','w') as e:
    writer=csv.writer(e,dialect="custom")
    writer.writerows(w_data)
e.close()

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

with open('weather.txt','r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
e.close()