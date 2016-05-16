__author__ = 'dgk'

#Shambhu Thapa 10677794 and Edward Ayran 75382995  ICS 31 Lab sec 2 Lab asst 6.


# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 d:  Search the collection for selected restaurants
     based on cuisine and average price
 e:  Search the collection for selected restaurants
     based on dish name
 c:  Change price of the dishes served
 p:  Print all the restaurants
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='c':
            n = float(input("Please enter the percentage change to apply to prices:  "))
            C = Collection_change_price(C, n)
        elif response=='d':
            n = input("Please enter the name of the cuisine:  ")
            p = input("please enter the Average price of the cuisine:  ")
            for r in Collection_search_by_cuisine(C, n, p):
                print(Restaurant_str(r))
        elif response=='e':
            n = input("Please enter the name of the dish: ")
            for r in Collection_search_by_dish(C, n):
                print(Restaurant_str(r))
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")


##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
Dish = namedtuple('Dish', 'name price calories')


def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:     " + Menu_str(self.menu) + "\n" +
        "Average price: $" + Average_price(self) + ". Average calories: "
        + Average_calories(self))

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter() )

#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

def Collection_search_by_cuisine(C: list, cuisine: str, price: str) -> list:
    """ Return list of Restaurants in input list whose cuisine matches input string
    """
    result = []
    for r in C:
        if r.cuisine == cuisine and Average_price(r) == price:
            result.append(r)
    return result

def Collection_search_by_dish(C: list, dish: str) -> list:
    """ Return list of Restaurants in input list whose dish is similar to
    input str
    """
    result = []
    for r in C:
        for m in r.menu:
            if dish in m.name:
                result.append(r)
    return result

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]

#### DISHES

def Menu_enter() -> list:
    dish_list = []
    adding_item = True
    while adding_item == True:
        response = input("Do you want to add a dish?" )
        if response.upper() == 'YES':
            dish_list.append(Dish_get_info())
        elif response.upper() == 'NO':
            for d in dish_list:
                Dish_str(d)
            adding_item = False
        else:
            print()
            adding_item = False
    return dish_list

def Dish_str(d: Dish) -> str:
    ''' Takes a Dish and returns it into a str '''
    return ("%s ($%.2f) : %d calories" %(d.name, d.price, d.calories))

def Menu_str(m: list) -> str:
    ''' Takes a menu list and returns it into a str '''
    menu_str_list = []
    for item in m:
        menu_str_list.append(Dish_str(item))
    return str(menu_str_list)

def Dish_get_info() -> Dish:
    """ Prompt user for fields of Dish; create and return.
    """
    return Dish(
        input("Please enter the name of the dish:  "),
        float(input("Please enter the price of that dish:  ")),
        float(input("Please enter the number of calories in the dish:  ")))

def dish_change_price(l:list, n: float) -> list:
    """ Changes the price of all dishes
    """
    c = []
    for rest in l:
        for dish in rest.menu:
            c.append(Dish(dish.name, dish.price + (dish.price * (n/100)), dish.calories))
    return c
def Collection_change_price(l:list, n: float) -> list:
    """ Changes the price of all dishes in a collection
    """
    c = []
    for rest in l:
        c.append(Restaurant(rest.name, rest.cuisine, rest.phone, dish_change_price(l, n)))
    return c
def Average_price(l:list) -> str:
    """ Takes the average price of the dishes in the menu
    """
    for rest in l.menu:
        return str(rest.price/len(l.menu))
def Average_calories(l:list) -> str:
    """ Takes the average calories of the dishes in the menu
    """
    for rest in l.menu:
        return str(rest.calories/len(l.menu))


        
restaurants()
