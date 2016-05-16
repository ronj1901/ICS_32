from tkinter import*

def Dropmenu(mylist,status):
    var=StringVar(root)
    var.set(status)
    mymenu=OptionMenu(root,var,*mylist)
    mymenu.pack(side=LEFT)
    mymenu.config(font=('calibri',(10)),bg='black',width=12)
    mymenu['menu'].config(font=('calibri',(10)),bg='blue')

root=Tk()

Dropmenu(['a','b','c'],'Select')

root.mainloop()
