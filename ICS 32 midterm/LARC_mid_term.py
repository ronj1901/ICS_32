# Write Code

#1
def ask_for_floats() -> (float, float):
    ''' ask the user to enter two float numbers and returns tuple of those numbers'''
    while  True:
		

        value = input("Please enters two numbers : ").split(',')
        if len(value) != 2:
            print("Please try again later") 
        else: 
            break


    return (value[0], value[-1])


print(ask_for_floats())



#2
import powers
def square():

    while True:
        n = input("Number: ")

        if n != 'exit':
            try:
                squared = powers.square(n)
                print("{} squared = {}".format(n, squared))
            except:
                print("{} cannot be squared.".format(n))
        elif n == 'exit':
            break


square()

