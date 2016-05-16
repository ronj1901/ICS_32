# canvas.py

from tkinter import *

root = Tk()

canvas = Canvas(root, width =  300, height = 300, background  = "blue")
canvas.pack()
canvas.create_rectangle(20,20,150,270, fill = "white")
canvas.create_line(0,0,300,300, fill = "red")
canvas.create_polygon(0,0,5,5)
root.mainloop()
