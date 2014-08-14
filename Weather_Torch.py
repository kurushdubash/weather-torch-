import requests
import time

api = '2ffd40362f6c4bdd050c1ad48eaa7891cb1e4890'

def get_zip_code():
	print('Please enter your zip code:')
	zip_code = input()
	while len(zip_code) < 5 or len(zip_code) > 5:
		print('Invalid Zip Code')
		print('Please enter your zip code:')
		zip_code = input()
	return str(zip_code)

def get_weather_json(zip_code):
	weather_url = 'http://api.worldweatheronline.com/free/v1/weather.ashx?q=' + str(zip_code) + '&format=json&num_of_days=1&key=' + str(api)
	weather_data = requests.get(weather_url)
	weather_json = weather_data.json()
	return weather_json

def get_temperature(json_data):
	temp = json_data['data']['current_condition'][0]['temp_F']
	return temp

def get_forcast(json_data):
	forcast = json_data['data']['current_condition'][0]['weatherCode']
	return forcast

# def get_windspeed(json_data):
# 	wind - json_data['data']['current_condition'][0]['windspeedMiles']
# 	return str(wind)

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
	print(temp, 'F')
	print(weather_code)

	#Setting arguments for weather torch

	is_upside_down = upside_down(int(weather_code))

	args = ''
	if is_upside_down:
		args+= 'upside_down=1'
	else: 
		args+= 'upside_down=0'

	last_RGB_values = array_of_RGB_values.pop()
	red, green, blue = get_RGB(int(temp))
	change_colors(last_RGB_values[0], last_RGB_values[1], last_RGB_values[2], red, green, blue , args)
	sleep(15)

def upside_down(weather_code):
	if weather_code > 142:
		return True
	return False

def sleep(refresh_rate):
	sleep_time = refresh_rate
	while sleep_time > 0:
		print(str(sleep_time), 'minutes remaining')
		time.sleep(60)
		sleep_time-=1

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

def change_colors(old_red, old_blue, old_green, new_red, new_green, new_blue, args):
	print(old_red, old_green, old_blue)	
	print(new_red, new_green, new_blue)	

	while (old_red != new_red or old_blue != new_blue or old_green != new_green): 

		if old_red != new_red:
			if old_red < new_red:
				if old_red + 20 > new_red:
					old_red = new_red
				else:
					old_red += 20
			else:
				if old_red - 20 < new_red:
					old_red = new_red
				else:
					old_red -= 20

		if old_green != new_green:
			if old_green < new_green:
				if old_green + 20 > new_green:
					old_green = new_green
				else:
					old_green += 20
			else:
				if old_green - 20 < new_green:
					old_green = new_green
				else:
					old_green -= 20

		if old_blue != new_blue:
			if old_blue < new_blue:
				if old_blue + 20 > new_blue:
					old_blue = new_blue
				else:
					old_blue += 20
			else:
				if old_blue - 20 < new_blue:
					old_blue = new_blue
				else:
					old_blue -= 20

		data['args'] = args + ',red_energy=' + str(old_red) + ',green_energy=' + str(old_green)+ ',blue_energy=' + str(old_blue)
		print(data['args'])
		requests.post(url, data=data)
		if old_red == new_red and old_blue == new_blue and old_green == new_green:
			break;

	array_of_RGB_values.append([new_red, new_green, new_blue])


zip_code_input = get_zip_code()
while True:
	check_weather()











