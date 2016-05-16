# a check button


from tkinter import *

root = Tk()

label1 = Label(root, text = "name: ")

label1.grid(row = 0 , column = 0, sticky = "E" )

label2 = Label(root, text = "Password: ")
label2.grid(row = 1 , column = 0, sticky = "E")

entryspace = Entry(root)   # create a text box

entryspace.grid(row = 0 , column = 1)  # for name 

entryspace2 = Entry(root)
entryspace2.grid(row = 1 , column = 1)   # for password 


cbutton =  Checkbutton(root, text = "Remember password")
cbutton.grid(columnspan = 2)

root.mainloop()
