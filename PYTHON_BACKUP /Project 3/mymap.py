import http.client
import urllib.request
import urllib.error
import urllib.parse
import json

import map_UI
# this module build url and loads json

MAPQUEST_API_KEY = "YGNQTFLjSeFX6mbmkVp2j4ll0Y3izVlQ"
BASE_URL  = "http://open.mapquestapi.com/directions/v2/route?"
ELEVATION_URL = "http://open.mapquestapi.com/elevation/v1/profile?"


def build_search_url(location_list: list)->str:
    '''
    Build the url for the mapquest, the json  data is produced
    based on the locations provided by the user 
    '''
    query_parameters = [
        ('key',MAPQUEST_API_KEY),('from',location_list[0])
    ]

    for address in location_list[1:]:
        query_parameters.append(('to',address))
    return BASE_URL + urllib.parse.urlencode(query_parameters)

def build_elevation_url(lat_lng:list)->str:
    '''
    Build the elevation url using the list of lat and lng
    and return elevation url 
    '''
##  query_parameters = [("key", MAPQUEST_API_KEY),("unit","f")]
    s = ""
    first = True
    for item in lat_lng:
        if first:
            s += str(item)
            first = False
        else:
            s += "," + str(item)


    query_parameters = [('key',MAPQUEST_API_KEY),('unit','f'),('latLngCollection',s)]
    
  #  query_parameters=[('key',MAPQUEST_API_KEY),('unit','f'),('latLngCollection',','.join(str(item) for item in lat_lng))]
        

    return  ELEVATION_URL + urllib.parse.urlencode(query_parameters)


def get_result(url :str)->'json':
    '''
    from the url, this function takes it as an input and
    produce the json data
    '''

    response = None

    try:
        response = urllib.request.urlopen(url)
        return json.loads(response.read().decode(encoding = 'utf-8'))

    finally:
        if response != None:
            response.close()
            



    



 
