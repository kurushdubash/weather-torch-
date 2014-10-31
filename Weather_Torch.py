import requests
import time
from datetime import datetime

api = '2ffd40362f6c4bdd050c1ad48eaa7891cb1e4890'

# User input Zip Code for weather data
def get_zip_code():
	
	print('Please enter your zip code:')
	zip_code = input()
	while len(zip_code) < 5 or len(zip_code) > 5:
		print('Invalid Zip Code')
		print('Please enter your zip code:')
		zip_code = input()
	return str(zip_code)

# GETs the JSON from the worldweatheronline API
def get_weather_json(zip_code):
	
	weather_url = 'http://api.worldweatheronline.com/free/v1/weather.ashx?q=' + str(zip_code) + '&format=json&num_of_days=1&key=' + str(api)
	weather_data = requests.get(weather_url)
	weather_json = weather_data.json()
	return weather_json

# Retrieves Temperature string from JSON
def get_temperature(json_data):
	temp = json_data['data']['current_condition'][0]['temp_F']
	return temp

# Retrieves forcast code string from JSON
def get_forcast(json_data):
	forcast = json_data['data']['current_condition'][0]['weatherCode']
	return forcast

# Retrieves wind MPH string from JSON
def get_windspeed(json_data):
	wind = json_data['data']['current_condition'][0]['windspeedMiles']
	return str(wind)

# Gets the current time and posts it on the Torch every minute
def timenow():
	time_data = datetime.now().time().isoformat()
	url = 'https://api.spark.io/v1/devices/' + access_id + '/message'
	# print(type(time_data)) # str
	# print(time_data) # 00:42:55.923423423

	hour = int(time_data[0:2])
	minute = time_data[3:5]
	light = 'AM'

	if hour > 12:
		hour = hour - 12
		light = 'PM'
	elif hour == 00:
		hour = 12
	
	hour = str(hour)
	time = hour + ':' + minute + ' ' + light
	# print(time)
	data["message"] = time
	requests.post(url, data=data)
	
function = 'params'
access_id = '53ff6f065075535140441187'
access_token = 'a5c190e99b6803f74533e2876feb0c687e44cada'

url = 'https://api.spark.io/v1/devices/' + access_id + '/' + function
data = {'access_token': access_token}
array_of_RGB_values = [[0,0,0]]

#API Pulls, Weather Data, and Weather codes
def check_weather():
	
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
	sleep(10) #function call to do 10 iterations (=10 minutes currently)

# If JSON returns rainy/snowy forcast, this function returns True. 
def upside_down(weather_code):
	
	if weather_code > 142:
		return 'upside_down=1'
	return 'upside_down=0'

# Time between Weather API calls (time interval between Torch color updates)
def sleep(refresh_rate):
	
	sleep_time = refresh_rate
	while sleep_time > 0:
		print(str(sleep_time), 'minutes remaining')
		time.sleep(60) #60 seconds
		timenow()
		sleep_time-=1

# Gets the Torch Light colors based on the current Temperature
def get_RGB(temperature):
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
		blue = 255
	elif temperature < 65:
		green = 255
		blue = 128
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

# Torch color smooth transition between temperature settings
def change_colors(old_red, old_green, old_blue, new_red, new_green, new_blue, args):
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