import requests

function = 'params'
access_id = '53ff6f065075535140441187'
access_token = 'e0dd630ae5f950ff67dad0c1cb20ae56e89dcd0b'

url = 'https://api.spark.io/v1/devices/' + access_id + '/' + function
data = {'access_token': access_token, 'args': 'red_energy=0'}

r = requests.post(url, data=data)

