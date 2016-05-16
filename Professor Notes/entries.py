# entries .py 
from tkinter import *

root = Tk()

label1 = Label(root, text = "name: ")

label1.grid(row = 0 , column = 0 )

entryspace = Entry(root)   # create a text box 


entryspace.grid(row = 0 , column = 1)

root.mainloop()
