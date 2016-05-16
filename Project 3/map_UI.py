
# Shambhu Thapa 10677794
#Project 3:  Ride Across The River

import mymap
import generator

def user_interface():
    '''
    interact betweeen different modules
    and produce the output
    '''

    try:
        
        locations  = get_locations()
        
        data = mymap.get_result(mymap.build_search_url(locations))

    
        instructions = user_command()
        if len(locations) >= 2 and len(instructions) <=5 :
            
            handle_output(data, instructions)
            
        else:
            print("You must specify at least two locations and maximum 5 outputs. Please try again later\n")
    except:
        
        print("MAPQUEST ERROR")
    finally:
        print()
        print(" Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
   


def get_locations()->list:
    '''
    gets an input for locations from the user
    '''
    result = list()
    num_of_locations = int(input())

    for item in range(num_of_locations):
        location = input()
        result.append(location)

    return result


def user_command()->list:
    '''
    when the user wants to see the result they want to
    , this function ask the user the number of results
    that like to see
    '''

    num_of_results = int(input())
    result = list()

    for items in range(num_of_results):
        user_result = input()
        result.append(user_result)
           
    return result

def handle_output(data :'json', instruction:list):

    for item in instruction:
        if item == 'STEPS':
            generator.Steps(data).control()
        if item == 'TOTALDISTANCE':
            generator.Distance(data).control()
        
        if item == 'TOTALTIME':
            generator.Time(data).control()
        
        if item == 'LATLONG':
            generator.Latlong(data).control()
        
        if item == 'ELEVATION':
            generator.Elevation(data).control()
        

if __name__ == "__main__":
    '''
    handle the main interface of the map
    '''
    
    user_interface()

    
    
    
                          
