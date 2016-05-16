
from tkinter import *
#getting data from the entries


root = Tk()

#pass
root.geometry("400x400")

label1 = Label(root, text = "Enter your expressions in the box")
label1.pack()
def evaluate(event):    # always put event as a paramter for binding functions
    data = e.get()   #  update with new value
    ans.configure(text = "Answer : " + str(eval(data))) 

e =  Entry(root)
e.bind("<Return>", evaluate)

e.pack()
ans = Label(root)
ans.pack() 

root.mainloop()
