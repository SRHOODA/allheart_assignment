# from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urlencode

with open('config.json') as f:
    params = json.load(f)['params']
# print(params['api_key'])

#we can use text search as well as nearby place search
place_endpoint = "https://maps.googleapis.com/maps/api/place/textsearch/json"

input_by_user = "resturants in delhi"

params = {
    "query": input_by_user,
    "key": params['api_key']   
    ##you have to add your own account api key(depends upon which api you gonna use google will charge you some amount)
}

nearby_place_endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

lat, lng = "37.39020952010728", "-122.0742763298927"
nearby_place_params = {
    "key": params['api_key'],
    "location": f'{lat}, {lng}',
    "radius": 50000,  #max radius in meters
    "keyword": "chinese food"
}

##similarly we also have a endpoint for detail_lookup
detail_lookup = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name%2Crating%2Cformatted_phone_number&key=YOUR_API_KEY"
##now we need tp define its params and then encode it and then make a request.

params_encoded = urlencode(params)
params_encoded_nearby = urlencode(nearby_place_params)

place_url = f'{place_endpoint}?{params_encoded}'
place_url_nearby = f'{nearby_place_endpoint}?{params_encoded_nearby}'

response = requests.get(f'{place_url}') 

print(response.json())

# print(response.text)

# ##i have tried several ways but BeautifulSoup is not returning any response, i am either getting None
# ##or empty [] list in response.

# ####so i am gonna use google place api to get the response as a json object

# #1. for that we need to sign in(only if have a google account otherwise need to create a new account) 
# #2. then need to create a project over google cloud platform and
# #3. then need to active the api services we want to use- places API
# #4. then get API key









