#Creating an emopty GUI window  
import tkinter
window = tkinter.Tk()   
window.mainloop()   # making a tkinter GUI active  also called as event loop 

# widgets and options 

''' creating a button ''' 

button = tkinter.Button(master = window, text  = "Hello  ! ", font = ('helvetica', 20), command = hello_button_pressed)



def hello_button_pressed():
	''' do whatevr you want to do  ''' 
	name = input("what is your name")

	print("hello {} , you  just pressed a button".format(name))



 

