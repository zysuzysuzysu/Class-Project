'''
Suzanne Marie Manongas
July 23, 2020

Program that interacts with a webservice to obtain data
Grabs information at openweathermap.org
'''

import json
from urllib.request import urlopen

class Weather:

	def __init__(self, city_name,latitude,longhitude,temperature,wind_speed,cloud_type,atm_pressure,humidity):
		self.city_name=city_name
		self.latitude=latitude
		self.longhitude=longhitude
		self.temperature=temperature
		self.wind_speed=wind_speed
		self.cloud_type=cloud_type
		self.atm_pressure=atm_pressure
		self.humidity=humidity

	def DisplayWeather(self):
		print()
		print(f"\t\t{self.city_name} Weather Information: ")
		geo_coordinates = f"\t\t\t(under geo-coordinates of {self.latitude}, {self.longhitude})"
		print(geo_coordinates)
		print(f"\n\t\tTemperature: {self.temperature}F")
		print(f"\t\tWind: {self.wind_speed} m/s")
		print(f"\t\tCloudiness: {self.cloud_type}")
		print(f"\t\tAtmospheric pressure: {self.atm_pressure}hpa")
		print(f"\t\tHumidity: {self.humidity}%")


def main():	
	while True:
		print("\nFIND YOUR WEATHER!!!")
		city_name=input("\n\tEnter your city name (Type Q to end the program): ")
		city_name=city_name.title()
		city_name=city_name.strip()

		if city_name == "Q":
			break

		else:
			api_token = '90156034a9cd88f0fd43039c52350eaf'
			api_url_base = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={api_token}'
			
			with urlopen(api_url_base) as response:
				source = response.read()
			data = json.loads(source)

			latitude = data['coord']['lat']
			longhitude = data['coord']['lon']
			temperature = data['main']['temp']
			wind_speed = data['wind']['speed']
			cloud_type = data['weather'][0]['description']
			atm_pressure = data['main']['pressure']
			humidity = data['main']['humidity']
			
			program= Weather(city_name,latitude,longhitude,temperature,wind_speed,cloud_type,atm_pressure,humidity)
			
			print(program.DisplayWeather())

main()
