#gridlayout 

from tkinter import *


root = Tk()

label1  =  Label(root,  text = "Label 1 ")

label2  =  Label(root,  text = "Label 2 ")

label3  =  Label(root,  text = "Label 3 ")

label1.grid(row  = 0 , column  = 0 )

label2.grid(row = 0, column = 1)

label3.grid(row = 1 , column = 0)

root.mainloop()
