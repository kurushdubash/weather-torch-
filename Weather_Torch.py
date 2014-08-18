import requests
import time

api = '2ffd40362f6c4bdd050c1ad48eaa7891cb1e4890'

def get_zip_code():
	# User input Zip Code for weather data
	print('Please enter your zip code:')
	zip_code = input()
	while len(zip_code) < 5 or len(zip_code) > 5:
		print('Invalid Zip Code')
		print('Please enter your zip code:')
		zip_code = input()
	return str(zip_code)

def get_weather_json(zip_code):
	# GETs the JSON from the worldweatheronline API
	weather_url = 'http://api.worldweatheronline.com/free/v1/weather.ashx?q=' + str(zip_code) + '&format=json&num_of_days=1&key=' + str(api)
	weather_data = requests.get(weather_url)
	weather_json = weather_data.json()
	return weather_json

def get_temperature(json_data):
	# Retrieves Temperature string from JSON
	temp = json_data['data']['current_condition'][0]['temp_F']
	return temp

def get_forcast(json_data):
	# Retrieves forcast code string from JSON
	forcast = json_data['data']['current_condition'][0]['weatherCode']
	return forcast

def get_windspeed(json_data):
	# Retrieves wind MPH string from JSON
 	wind = json_data['data']['current_condition'][0]['windspeedMiles']
 	return str(wind)

function = 'params'
access_id = '53ff6f065075535140441187'
access_token = 'e0dd630ae5f950ff67dad0c1cb20ae56e89dcd0b'

url = 'https://api.spark.io/v1/devices/' + access_id + '/' + function
data = {'access_token': access_token}
array_of_RGB_values = [[0,0,0]]

def check_weather():
	#API Pulls, Weather Data, and Weather codes
	weather_json = get_weather_json(zip_code_input)
	temp = get_temperature(weather_json)
	weather_code = get_forcast(weather_json)
	wind = get_windspeed(weather_json)
	print(temp, 'F')
	print(weather_code, "Weather Code")
	print(wind, "MPH wind")
	#Setting arguments for weather torch

	args = upside_down(int(weather_code))


	last_RGB_values = array_of_RGB_values.pop()
	red, green, blue = get_RGB(int(temp))
	change_colors(last_RGB_values[0], last_RGB_values[1], last_RGB_values[2], red, green, blue , args)
	sleep(10)

def upside_down(weather_code):
	# If JSON returns rainy/snowy forcast, this function returns True. 
	if weather_code > 142:
		return 'upside_down=1'
	return 'upside_down=0'

def sleep(refresh_rate):
	# Time between Weather API calls (time interval between Torch color updates)
	sleep_time = refresh_rate
	while sleep_time > 0:
		print(str(sleep_time), 'minutes remaining')
		time.sleep(60)
		sleep_time-=1

def get_RGB(temperature):
	# Gets the Torch Light colors based on the current Temperature
	red = 0
	green = 0
	blue = 0
	if temperature < 50:
		blue = 255
	elif temperature < 55:
		green = 128
		blue = 255
	elif temperature < 60:
		green = 255
		blue = 128
	elif temperature < 65:
		green = 255
		blue = 255
	elif temperature < 70:
		green = 255
		blue = 0
	elif temperature < 75:
		red = 128
		green = 255
	elif temperature < 80:
		red = 255
		green = 255
	elif temperature < 85:
		red = 255
		green = 128
	elif temperature < 90:
		red = 255
		green = 102
		blue = 102
	elif temperature < 95:
		red = 255
	elif temperature >= 95:
		red = 153
	return red, green, blue

def change_colors(old_red, old_green, old_blue, new_red, new_green, new_blue, args):
	# Torch color smooth transition between temperature settings
	print(old_red, old_green, old_blue)	
	print(new_red, new_green, new_blue)	
	
	while (old_red != new_red or old_blue != new_blue or old_green != new_green): 

		if old_red != new_red:
			if old_red < new_red:
				if old_red + 5 > new_red:
					old_red = new_red
				else:
					old_red += 5
			else:
				if old_red - 5 < new_red:
					old_red = new_red
				else:
					old_red -= 5

		if old_green != new_green:
			if old_green < new_green:
				if old_green + 5 > new_green:
					old_green = new_green
				else:
					old_green += 5
			else:
				if old_green - 5 < new_green:
					old_green = new_green
				else:
					old_green -= 5

		if old_blue != new_blue:
			if old_blue < new_blue:
				if old_blue + 5 > new_blue:
					old_blue = new_blue
				else:
					old_blue += 5
			else:
				if old_blue - 5 < new_blue:
					old_blue = new_blue
				else:
					old_blue -= 5

		data['args'] = args + ',red_energy=' + str(old_red) + ',green_energy=' + str(old_green)+ ',blue_energy=' + str(old_blue)
		print(data['args'])
		requests.post(url, data=data)
		if old_red == new_red and old_blue == new_blue and old_green == new_green:
			break;

	array_of_RGB_values.append([new_red, new_green, new_blue])


zip_code_input = get_zip_code()
while True:
	check_weather()











