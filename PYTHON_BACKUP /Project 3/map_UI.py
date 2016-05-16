import mymap
import generator

def user_interface():
    '''
    interact betweeen different modules
    and produce the output
    '''

    try:
        
        locations  = get_locations()
        print(locations)
        
        data = mymap.get_result(mymap.build_search_url(locations))
        print(mymap.build_elevation_url(data))
        
        instructions = user_command()
    
        print(instructions)
        
        handle_output(data, instructions)
    except:
        
        print("MAPQUEST ERROR")
    finally:
        print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
   
  
    

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
        if user_result == 'STEPS':
            user_result = 'Steps'
        elif user_result == 'TOTALDISTANCE':
            user_result = 'Distance'
        elif user_result == 'TOTALTIME':
           user_result = 'Time'
        elif user_result == 'LATLONG':
           user_result = 'Latlong'
        elif user_result == 'ELEVATION':
           user_result = 'Elevation'
                    
        
        result.append(user_result)
           
    return result

def handle_output(data :'json', instruction:list):

    generator.get_output(data, instruction)
    #for item in instruction:
##        if item == 'Steps':
##            generate.Steps.control(data)



if __name__ == "__main__":
    '''
    handle the main interface of the map
    '''
    
    user_interface()

    
    
    
                          
