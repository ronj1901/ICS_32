"""
 this is  a  simple guessing game using python
 """
# this whole section deals with modules , library

import random

#print(random.randint(0,100)) # generates the random numbers from o to 100

### guessing game


# we are going to use if else and random
compGuess = random.randint(0, 50 )


while True:
    userGuess  = int(input("Guess a number between 0 and 50:\n"))
    if userGuess > compGuess:
        print("guess lower")
    elif userGuess  < compGuess:
        print("Guess Higher")
    else:
        print("Congratulations ! , you have guessed the correct numbers")
        break

    
        
        
