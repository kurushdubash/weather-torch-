import requests

# function = 'params'
# access_id = '53ff6f065075535140441187'
# access_token = 'e0dd630ae5f950ff67dad0c1cb20ae56e89dcd0b'

# url = 'https://api.spark.io/v1/devices/' + access_id + '/' + function
# data = {'access_token': access_token, 'args': 'red_energy=0'}

# r = requests.post(url, data=data)

weather_url = 'http://api.wunderground.com/api/cedc5b283ddfd80b/conditions/q/'

def get_zip_code():
	print('Please enter your zip code:')
	zip_code = input()

	while len(zip_code) < 5 or len(zip_code) > 5:
		print('Invalid Zip Code')
		print('Please enter your zip code:')
		zip_code = input()
	return zip_code

def get_location_info(zip_code):
	url = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + str(zip_code) + '&sensor=true'
	location_data = requests.get(url)
	location_json = location_data.json()
	return location_json['results'][0]['formatted_address']


def get_temperature_data(zip_code, url):
	url = url + str(zip_code) + '.json'
	data = requests.get(url)
	weather_json = data.json()
	return weather_json

zip_code_input = get_zip_code()
location = get_location_info(zip_code_input)
weather_data = get_temperature_data(zip_code_input, weather_url)

print(location)
print(weather_data)
