from tkinter import *

window = Tk()

def km_to_miles():
    miles = float(e1_value.get()) * 1.6  #get method grabs a string
    t1.insert(END,miles)  #Text widget has a method insert() to insert the text

b1 = Button(window, text = "Execute",command = km_to_miles)
b1.grid(row = 0,column = 0)  

e1_value = StringVar()
e1 = Entry(window,textvariable = e1_value)
e1.grid(row = 0,column = 1)

t1 = Text(window, height = 1,width = 20)
t1.grid(row = 0,column = 2)

window.mainloop()