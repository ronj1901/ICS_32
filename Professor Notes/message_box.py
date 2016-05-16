from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Did you know that the world just Blew up?")
answer = tkinter.messagebox.askquestion("Question 1", "Are you  human? ")

if answer == "yes":
    tkinter.messagebox.showinfo("Congrats", "Thank god ! it is good to know other human is out there")

if answer == "no":
    tkinter.messagebox.showinfo("Alienn, you are 100% confirmed alien")
root.mainloop()


