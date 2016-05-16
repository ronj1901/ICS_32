# testing the json module and Mapquest API

import http.client
import urllib.request
import urllib.error
import urllib.parse
import json


API_KEY = "key=YGNQTFLjSeFX6mbmkVp2j4ll0Y3izVlQ"
base_url = "http://open.mapquestapi.com/directions/v2/route?"

from_to = "&from=" + urllib.parse.urlencode(from_)

url = base_ur + API_KEY + from_to

response = urllib.request.urlopen(url)
json_text = response.read().decode(encoding = 'utf-8')

data = json.loads(json_text)
for i in data:
    print(i)


