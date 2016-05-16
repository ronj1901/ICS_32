from tkinter import *


# perform a function after clicking the button

# what is binding: when a key is pressed ,that is an event
                # you can track this events , 

root = Tk()


##
##
##def printName(event): # event parameter is always required when bind function is used
##    ''' this function will be handled or called after button is clicked '''
##
##
##    name = input("what is your name  ? : ")
##    print("Hello {}, welcome to the clicking thing".format(name))
##    print()
##    
##
##



def leftclick(event):
    print("left")

def rightclick(event):
    print("right")

def leftkey(event):
    print("left key pressed")
    
def rightkey(event):
    print("right key pressed")
def scroll(event):
    print("scrolled")
    
##button1 = Button(root, text = " CLick here ") 
##button1.bind("<Button-1>", printName) #  perform the action when left mouse key is presed
##button1.pack()

root.geometry("500x500")

root.bind("<Button-1>", leftclick)
root.bind("<Button-2>", rightclick)
root.bind("<Button-3>", scroll)
root.bind("<Left>", leftkey)
root.bind("<Right>", rightkey)



root.mainloop()
 
