import requests  # To send http request, installed in terminal
import os
from datetime import datetime

location = input("Enter city name: ")  # User input

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + "94ceac1fac6664e20e8fe8a03cc34180"

api_link = requests.get(complete_api_link)  # because we have imported requests on the top
api_data = api_link.json()  # put it in  json format, and we have to put it in json otherwise it is not showing up in console, called a raw format
# print(api_data)  # this is just to print out the raw format. So we need to format this data so that user can read it
# read the API response so that you know what to call

if api_data['cod'] == '404':  # if the output is like this
    print("Invalid input. Please check the city name".format(location))
else:
    # create variables to store display data
    temp_city = ((api_data['main']['temp']) - 273.15)  # this is in kelvin so we need to put it in C
    weather_desc = api_data['weather'][0]['description']
    humid = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")  # %p is for AM PM

    print ("------------------------------------------------------------")
    print ("Weather Stats for - {}".format(location.upper(), date_time))
    print ("------------------------------------------------------------")

    print ("Current temperature is     : {:.2f} deg C".format(temp_city))
    print ("Current weather description: ",weather_desc)
    print ("Current humidity:          :",humid, '%')
    print ("Current wind speed         :", wind_spd, 'kmph')


