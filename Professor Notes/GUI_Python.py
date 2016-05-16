from tkinter import *

root = Tk()


#adding text to the screen
topFrame =Frame(root)

topFrame.pack()

botFrame = Frame(root)

botFrame.pack(side = BOTTOM)

button1 =  Button(topFrame, text = "Click me", fg = "Blue")
button1.pack(side = LEFT)

button2 =  Button(topFrame, text = "Hello ", fg = "Red")
button2.pack(side = LEFT)


button3 =  Button(botFrame, text = "Hi", fg = "Green")
button3.pack(side  = LEFT)

button4 =  Button(botFrame, text = "Whats up", fg = "Orange")
button4.pack(side = LEFT)

root.mainloop()




