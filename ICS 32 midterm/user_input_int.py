### write a function that ask the user to input two different integers and return tuples
##
##
##
####def user_interface()->(int,int):
####
####    while True:
####        try:
####            
####            number = input("Please enter two numbers: ")
####            f = number.split(',')
####            if len(f) != 2:
####                raise SyntaxError
####            return (int(f[0], int(f[1]))
####
####        except:
####            print("Try again")
##
##                
##                
def user_interface()->(int,int):
    while True:
        try:
            
            number = input("Please enter two numbers: ")
            f = number.split(',')
            if len(f) != 2:
                raise SyntaxError
                    
            return (int(f[0]), int(f[1]))

        except:
            print("try again")


print(user_interface())
def ask_for_floats() -> (float,float):

  while True:

    try: 

        f = input("Enter two floats:")

        f = f.split(',') 

        if len(f) != 2:

            raise SyntaxError 

        return (float(f[0]), float(f[1]))

    except:

      print("Try again.\n")


print(ask_for_floats())
