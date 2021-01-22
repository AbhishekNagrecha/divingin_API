#Here i have imported the essential modules
import requests # to make a http request
import os       # to get access to your os
from datetime import datetime

my_api = os.environ['weather_api'] # to access the api stored in our environment variables
location = input("Please enter the city name: ")

full_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+my_api
api_link = requests.get(full_api_link)
api_info = api_link.json()
# print(api_data)

#Now here we create variables to store and display the information
# use the api response to get the details
temperature = ((api_info['main']['temp']) - 273.15) # coverts temperature to celsius
actual_temperature = ((api_info['main']['feels_like']) - 273.15)
description = api_info['weather'][0]['description']
humidity = api_info['main']['humidity']
wind_speed = api_info['wind']['speed']
sunrise_time = api_info['sys']['sunrise']
sunset_time = api_info['sys']['sunset']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
maximum_temperature = (api_info['main']['temp_max'] - 273.15)
minimum_temperature = (api_info['main']['temp_min'] - 273.15)

print ("------------------------------------------------------------------------------------------")
print ("Current Weather Statistics for the city of - {}  | {}".format(location.upper(), date_time))
print ("------------------------------------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temperature))
print ("However It Feels like: {:.2f} deg C".format(actual_temperature))
print ("Today's high will be: {:.2f} deg C".format(maximum_temperature))
print ("Today's low will be: {:.2f} deg C".format(minimum_temperature))
print ("Current weather desc:",description)
print ("Current Humidity is:",humidity, '%')
print ("Current wind speed is:",wind_speed ,'kmph')


