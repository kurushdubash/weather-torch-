import requests
import time

api = '2ffd40362f6c4bdd050c1ad48eaa7891cb1e4890'
ferinheight = True

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

def check_weather():
	#API Pulls, Weather Data, and Weather codes
	weather_json = get_weather_json(zip_code_input)
	temp = get_temperature(weather_json)
	weather_code = get_forcast(weather_json)

	print(weather_code)
	#Setting arguments for weather torch

	red = 0
	green = 0
	blue = 0
	is_upside_down = upside_down(int(weather_code))

	args = ''
	if is_upside_down:
		args+= 'upside_down=1'
	else: 
		args+= 'upside_down=0'
		
	args = args + get_RGB()
	print(args)
	data = {'access_token': access_token, 'args': args}
	r = requests.post(url, data=data)

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

def get_RGB():
	return 'red_energy=255'

# def change_colors():
# 	while value > 0: 
# 	if value - 20 < 0:
# 		value = 0
# 	else:
# 		value-=20
# 	args ='upside_down=1,red_energy=' + str(value)
# 	data['args'] = args
# 	print (args)
# 	requests.post(url, data=data)

zip_code_input = get_zip_code()
check_weather()
while True:
	check_weather()











