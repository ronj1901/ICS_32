# classes
class ClassName:
    pass

# create an instance of a class / object

instance = ClassName()



class Students:
    # init initializes the object
    # we  need self because it reference its object
                                            # always take self as a parameter
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
            
        
student1 = Students("Bob", 12, "7th")

print(student1.name)
print(student1.age)
print(student1.grade)

shambhu = Students("Shambhu Thapa", 22, "B")
Mani = Students("Manish Patel", 25, "A")


print(Mani.grade)
print(Mani.name)
print(shambhu.age)
print(shambhu.grade)
                                            
class Cars:

    def __init__(self, year, make,model):
        self.year = year
        self.make  = make
        self.model  = model
    def display_info(self):
        return ("Make :" + str(self.make) + "\nModel: " + str(self.model) + "\nYear: " + str(self.year))


sam_car = Cars(2013, "Honda", "Accord Sport SE")
roman_car= Cars(2013, "Honda", "Civiv Lx")


print("----------Sam CAR DETAILS-----------")
print()
print(sam_car.display_info())
print("----------ROMAN CAR DETAILS-----------")
print()

print(roman_car.display_info())

##
##print("make: ", roman_car.make)
##print("model: ",roman_car.model)
##print("year: ", roman_car.year)
##
##
##
##
##print("make: ", sam_car.make)
##print("model: ",sam_car.model)
##print("year: ", sam_car.year)
##




