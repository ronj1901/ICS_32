#  Shambhu Thapa 10677794 and Michelle Vasquez 79554576  ICS 31 Lab sec 2.  Lab asst 8.

from collections  import namedtuple
Dish = namedtuple('Dish', 'name price calories')
def read_menu_with_count(s:str)->list:

    infile = open(s , "r")
    data  = infile.readlines()
    dishlist = []

    for line in data[1:]:
        
        dish = line.split('\t')
       
        i = "$"
        o = " "
        table= str.maketrans(i,o)        
        a = Dish(dish[0], float(dish[1].translate(table)), int(dish[2]))
        dishlist.append(a) 
            
    return dishlist
        
        
        
print(read_menu_with_count("menu1.txt"))

print("\n========================C2==============================================\n\n")
    
def read_menu(s:str)->list:

    infile = open(s , "r")
    data  = infile.readlines()
    dishlist = []

    for line in data:
        
        dish = line.split('\t')
       
        i = "$"
        o = " "
        table= str.maketrans(i,o)        
        a = Dish(dish[0], float(dish[1].translate(table)), int(dish[2]))
        dishlist.append(a) 
            
    return dishlist

print(read_menu("menu3.txt"))


print("\n========================C3==============================================\n\n")


def write_menu(d:list, s:str):


    outfile = open(s, 'w')
    #data = outfile.write(d, s)
    for item in d:
        return d[item[0]]
        
        
        
    
    outfile.close()




print(write_menu([Dish(name='Cheese Enchiladas', price=3.5, calories=400), Dish(name='Wet Burrito', price=6.0, calories=700), Dish(name='Chile Relleno', price=4.0, calories=600), Dish(name='Taco Salad', price=4.0, calories=400), Dish(name='Beef Taco', price=1.5, calories=250), Dish(name='Menudo', price=5.0, calories=750)], 'dish.txt'))

    
