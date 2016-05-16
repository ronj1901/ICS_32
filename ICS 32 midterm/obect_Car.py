# Classes

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def displayInfo(self):
        print("Details of car\n")
        print("Make: " + self.make  +"\n"+ "Model: " +self.model + "\n"+ "year: " +str(self.year) )


car1 = Car("honda", "Accord", 2013)
car2 = Car("toyota", "Camry", 2013)

car3 = Car("Ford", "Mustang", 2016)

car4 = Car("Dodge", "Charger", 2011)

car5 = Car("Bmw", "M5", 2013)

car6 = Car("Chevy", "Camaro", 2015)

list_car = [car1,car2,car3,car4,car5,car6]
#car1.displayInfo()
for car in list_car:
    
    car.displayInfo()
    print("=======" * 10)

class Student:
    def __init__(self,name):
        self.name =name
        self.grades = []
        self.attenddance = 0

    def add_grades(self,grade):
        self.grades.append(grade)
    def attendDay(self):
        self.attenddance += 1
    def average(self):
        return sum(self.grades)/len(self.grades)

s1= Student("Harry np")
s1.add_grades(90)
s1.add_grades(86)
s1.add_grades(85)
s1.add_grades(78)
s1.add_grades(96)
print("the average of the student is "+ str(s1.average()))
for i in range(10):
    s1.attendDay()

print(s1.attenddance)

print("Class Person")


class Person:

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._age = 0

    def get_first_name(self):
        return self._first_name
    def get_last_name(self):
        return self._last_name

    def grow_up(self):
        self._age += 1


    def show_bio(self):
        print("{} {} is  {} years old.".format(self._first_name, self._last_name, self._age))

a = Person("shambhu", "Thapa")

print(a.show_bio())
for i in range(22):
    a.grow_up()
print(a.show_bio())

        
        
        

        

        
