# Shambhu Thapa 10677794
# ICS 32
#Project # RIDINGN ACROSS THE RIVER

import http.client
import urllib.request
import urllib.error
import urllib.parse
import json

def user_interface()->None:
    ''' gets the user input '''
    url = "http://open.mapquestapi.com/directions/v2/route?"
    API_KEY = "YGNQTFLjSeFX6mbmkVp2j4ll0Y3izVlQ"
    
    location_list = []
    number_of_location = int(input())
    for i in range(0,number_of_location):
        location = str(input())
        location_list.append(location)

    from_ = location_list[0]
 #   to_ = None


    ## i need to make this query parameters dynanmic by using for llop and list
    query_parameters = [
        ('key',API_KEY),('from',from_)
    ]

    for i in location_list[1:]:
        query_parameters.append(('to',i))
    print(query_parameters)
    
    URL = url + urllib.parse.urlencode(query_parameters)


    try:
        response=urllib.request.urlopen(URL)
        data = json.loads(response.read().decode(encoding='utf-8'))
    finally:
        if response != None:
            response.close()

    print(URL)
    print("----" * 10)
    print("DIRECTIONS:")
    ### following for loop prints the step by step navigation
    for item in data["route"]["legs"]:
        for steps in item["maneuvers"]:
            print(steps["narrative"])
    ## following codes calculate the total distance
    print()
    distance = 0 
    for item in data["route"]["legs"]:
        for dis in item["maneuvers"]:
            distance += (dis["distance"])
        print("Total distance: {:.2f} miles".format(distance))
## following codes calcluates the total time of the trip
        
    print()
    time = 0 
    for item in data["route"]["legs"]:
        for tim in item["maneuvers"]:
            time += (tim["time"])
        print("TOTAL TIME: " + str(time))


    
##    output = int(input("Number of locations: "))
##    output_list = []
##    for i in range(output):
##        m = str(input("Output : "))
##        output_list.append(m)
##
##    for i in output_list:
##        if i.upper() == "STEPS":
##            print("DIRECTIONS\n")
##            for steps in data["route"]["locations"]:
##                print(str(steps["legs"]["origNarrative"]))
##                
##            
##        elif i.upper() == "TOTALDISTANCE":
##            print("TOTAL DISTANCE")
##
##        elif i.upper() == "TOTALTIME":
##            print("TOTAL TIME:")
##
##        elif i.upper() == "LATLONG":
##            print("LATLONG")
##            for location in data["route"]["locations"]:
##                print(str(location["latLng"]["lng"]) + " " + str(location["latLng"]["lat"]))
##        elif i.upper() == "ELEVATION":
##            print("ELEVATIONS")
##        else:
##            print("error")
##    #for i in nu
##    #location_1 = input()
##    #locaction_"""
if __name__ == '__main__':
    
    user_interface()
