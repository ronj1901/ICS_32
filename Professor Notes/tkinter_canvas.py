
import tkinter


root = tkinter.Tk()
canvas = tkinter.Canvas(root,width = 500, height  = 500, background = "black")


canvas.create_line(100, 175, 250,275, fill = 'red')

canvas.pack()
print("ranodm:")

root.mainloop()
