import mymap
import math

# this module is an output generator, we make the simialr clases that does
# similar things . USING DUCK _TYPING METHOD
    

class Steps:
    def control(self,data):
        print("DIRECTIONS")
        for item in data['route']['legs']:
            for sub in item['maneuvers']:
                print(sub['narrative'])

        print()
        

class Distance:
    def control(self,data):
        distance = 0
        for item in data["route"]["legs"]:
            for dis in item["maneuvers"]:
               distance += (dis["distance"])
        print("TOTAL DISTANCE: {} miles".format(str(round(distance))))
        print()

class Time:
    def control(self,data):
        print()
        time = 0 
        for item in data["route"]["legs"]:
            for tim in item["maneuvers"]:
                time += (tim["time"])
        print("TOTAL TIME: " + str(round(time/60)) + " minutes")
        print()

class Latlong:
    def control(self, data):
        print("LATLONGS")
        for item in data['route']['locations']:
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
    '''

    new_list = []
    for latlng in data["route"]["locations"]:
        new_list.append(latlng['latLng']['lat'])
        new_list.append(latlng['latLng']['lng'])
    return new_list

class Elevation:
    def control(self,data):
        print('ELEVATION')
        result =lat_lng(self, data)
        print(result)
        for item in range(0,len(result),2):
            #Data = str(result[item]) + "," + str(result[item +1])
            Data1 = mymap.build_elevation_url(result[item : item +2])
            Data2 = mymap.get_result(Data1)
            #print("elevation data")
            #print(Data2)
            for element in Data2['elevationProfile']:
                print(round(element['height']))
                print()
            


def get_output(json:'json', output_list:list):
    for item in output_list:
        item = eval(item)
        item.control(item,json)
  
     
















