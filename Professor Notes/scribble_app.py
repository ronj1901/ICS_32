# scriblle app


# some practice code


import tkinter

root = tkinter.Tk()

canvas =  tkinter.Canvas(width = 500, height = 400, background = "white")
  #drawing on canvas


canvas.create_line(100,150, 250,  275,  fill = "black")

canvas.create_oval(125, 175, 250, 225, outline = "black", fill = "red")


root.mainloop()
