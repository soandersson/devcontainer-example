#!/usr/local/bin/python
import requests

url = 'https://api.chucknorris.io/jokes/random'
params = {'param1': 'value1', 'param2': 'value2'}
headers = {'Authorization': 'Bearer <your_token>'}

#response = requests.get(url, params=params, headers=headers)

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print('Error:', response.status_code)