import requests

# function = 'params'
# access_id = '53ff6f065075535140441187'
# access_token = 'e0dd630ae5f950ff67dad0c1cb20ae56e89dcd0b'

# url = 'https://api.spark.io/v1/devices/' + access_id + '/' + function
# data = {'access_token': access_token, 'args': 'red_energy=0'}

# r = requests.post(url, data=data)

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
	forcast = json.data['data']['current_condition'][0]['weatherCode']
	return forcast

def get_windspeed(json_data):
	wind - json_data['data']['current_condition'][0]['windspeedMiles']
	return str(wind)


zip_code_input = get_zip_code()
weather_json = get_weather_json(zip_code_input)

temp = get_temperature(weather_json)

print(temp)

