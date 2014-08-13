import requests

# GLOBAL VAIRABLES
zip = 90638

def get_weather_json(zip):
	url = 'http://api.wunderground.com/api/0d9457cce7717c37/conditions/q/' + str(zip) + '.json'
	weather_data = requests.get(url)
	weather_json = weather_data.json()
	return weather_json



def get_temperature(json_data):
	temp = json_data['current_observation']['feelslike_f']
	return temp

def get_forcast(json_data):
	forcast = json.data['current_observation']['weather']
	return forcast

def get_windspeed(json_data):
	wind - json_data['current_observation']['wind_mph']
	return str(wind)

weather_json = get_weather_json(zip)

temperature = get_temperature(weather.json)
wind = get_windspeed(json.data)

print (get_temperature(weather_json))

# Sometimes it says the Key does not exist! This cam be a problem














# function = 'params'
# access_id = '53ff6f065075535140441187'
# access_token = 'e0dd630ae5f950ff67dad0c1cb20ae56e89dcd0b'

# url = 'https://api.spark.io/v1/devices/' + access_id + '/' + function
# data = {'access_token': access_token, 'args': 'red_energy=255'}

# r = requests.post(url, data=data)
