# drop down menu

from tkinter import *

root =  Tk()

def random():
    print("this is a statement")


def NewFile():
    print("New File")

mainMenu = Menu(root)

mainMenu1 = Menu(root)

mainMenu2 = Menu(root)

mainMenu3 = Menu(root)

# create one of sub menu
        # submenu 1
        # submenu 2



root.configure(menu = mainMenu)
root.configure(menu = mainMenu1)
root.configure(menu = mainMenu2)
root.configure(menu = mainMenu3)

subMenu = Menu(mainMenu) # this time we dont write root in braces.

subMenu1 = Menu(mainMenu1)
subMenu2 = Menu(mainMenu2)
subMenu3 = Menu(mainMenu3)

mainMenu.add_cascade(label = "File", menu = subMenu)

subMenu.add_command(label = "Random Func", command  = random )
subMenu.add_command(label = "New File", command  =  NewFile)


mainMenu1.add_cascade(label = "Edit", menu = subMenu1)

mainMenu2.add_cascade(label = "Format", menu = subMenu2)
mainMenu3.add_cascade(label = "Run", menu = subMenu3)



subMenu1.add_command(label = "Random Func", command  = random )
subMenu1.add_command(label = "New File", command  =  random)


root.mainloop()
