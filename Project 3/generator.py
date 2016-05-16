import mymap
import math

class Steps:
    def __init__(self, data):
        self.data = data
    def control(self):
        if self.data['info']['statuscode'] == 400:
            print("No route found")
        else:
            print("DIRECTIONS")
            for item in self.data['route']['legs']:
                for sub in item['maneuvers']:
                    print(sub['narrative'])

            print()
        

class Distance:
    def __init__(self, data):
        self.data = data
    def control(self):
        distance = 0
        for item in self.data["route"]["legs"]:
            for dis in item["maneuvers"]:
               distance += (dis["distance"])
        print("TOTAL DISTANCE: {} miles".format(str(round(distance))))
        print()

class Time:
    def __init__(self, data):
        self.data = data
    def control(self):
        print()
        time = 0 
        for item in self.data["route"]["legs"]:
            for tim in item["maneuvers"]:
                time += (tim["time"])
        print("TOTAL TIME: " + str(round(time/60)) + " minutes")
        print()

class Latlong:
    def __init__(self, data):
        self.data = data
        
    def control(self):
        print()
        print("LATLONGS")
        for item in self.data['route']['locations']:
            latitude=item['latLng']['lat']
            longitude=item['latLng']['lng']

            if latitude < 0:
                x = 'S'
            else:
                x = 'N'
            if longitude < 0:
                y = 'W'
            else:
                y = 'E'
            latitude = str(abs(round(latitude, 2))) + x
            longitude = str(abs(round(longitude, 2))) + y
            print(latitude, longitude)
        print()

def lat_lng(self, data)->list:
    '''
    creates a list of latitude and longitude
    and the result is passed to process elevation url
    '''

    new_list = []
    for latlng in data["route"]["locations"]:
        new_list.append(latlng['latLng']['lat'])
        new_list.append(latlng['latLng']['lng'])
    return new_list

class Elevation:
    def __init__(self, data):
        self.data = data
    def control(self):
        print('ELEVATIONS')
        result = lat_lng(self,self.data)
        for item in range(0,len(result),2):

            Data1 = mymap.build_elevation_url(result[item : item +2])
            Data2 = mymap.get_result(Data1)
            for element in Data2['elevationProfile']:
                print(round(element['height']))
                
        print()













