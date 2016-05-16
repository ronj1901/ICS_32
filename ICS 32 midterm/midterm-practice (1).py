### If you want to run the code, you should comment out the problems you haven't
###  done yet so you can't see the answers for them.
### Hints for each problem are at the bottom of this file
##
### 1. What's the output of the following code? 
##try:
##    try:
##        a = 5
##        b = 7
##        c = "five"
##        d = "seven"
##        print(a*c) 
##        print(c+d) 
##    except:
##        print(b*c) 
##    else:
##        print(c*d) 
##    finally:
##        print("first finally") 
##except:
##    print("second except") 
##else:
##    print("second else") 
##finally:
##    print("second finally") 
##
####ANSWERS
####fiveseven
##
## 2. Imagine you have 3 modules as seen below
##"first.py"
##import second
##print("1")
##if __name__ == '__main__':
##    print("first main")
##
##"second.py"
##import third
##print("2")
##if __name__ == '__main__':
##    import first
##    print("second main")
##
##"third.py"
##print("3")
##if __name__ == '__main__':
##    import second
##    print("third main")
##
## What is the output if
##  a) first.py is run,
##  b) second.py is run, and
##  c) third.py is run?
##
##
## 3. What's wrong with the following class? Just try to fix the class,
##  don't fix anything in the if name = main block
##class Person:
##    def __init__(self, name):
##        self.name = name
##        self.age = 0
##    def grow_up(self):
##        self.age += 1
##
##if __name__ == '__main__':
##    a = Person("Alex")
##    a.grow_up()


# 4. Write a function that takes a nested list of integers and returns the
#  minimum. Below is a function definition but you need to fill in the body.
# Remember that a nested list of integers means that every element in the list
#  is either an int or a nested list of ints.
##def find_min(l: list) -> int:
##    num_list = []
##    
##    for num in l:
##        if type(num) == list:
##            num_list.append(find_min(num))
##        else:
##            num_list.append(num)
##
##    return min(num_list)
    


# 5. What does the underscore before a function mean?
'''It means that it is a privaate code only for the programmer to use'''



# 6. What does the if __name__ == '__main__' statement mean?
'''If you want your program to run automatically without importing, use this.
or the code under this will ctreate whatever it has as a module'''




## Read all his code examples for review. If you understand everything he
##  wrote in his code examples, as well as what you did in projects,
##  you should be fine.
## Things to look over that I didn't go in depth about:
##  the sockets, protocol, and classes code examples.
## Make sure you're able to write your own classes!
## On Wednesday I'll be going over any questions you might have, so make sure
##  to bring them!








## Hints 
## 1. Remember what each word means. When do you do the except and else
##  blocks? When in doubt, always do finally!
##
## 2. If a module is loaded once through import, it doesn't load again, even if
##  the same import is called again. Python is smart enough to remember what
##  modules have been loaded already
##
## 3. Remember what we went over in class about classes. What always has to be
##  inside a class? There's 2 problems only, but they might be found in multiple
##  places
##
## 4. With recursion, always start small. How do you find the minimum of a simple
##  list of integers? After you get that, seperate it into the differnt possible
##  cases and deal with each seperately.













        

