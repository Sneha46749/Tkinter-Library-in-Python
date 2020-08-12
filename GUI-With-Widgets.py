from tkinter import *

window = Tk()

b1 = Button(window, text = "Execute")
#b1.pack()  #To add button to the window
b1.grid(row = 0,column = 0)  #To specify the position of widgets in the window

e1 = Entry(window)
e1.grid(row = 0,column = 1)

t1 = Text(window, height = 1,width = 20)
t1.grid(row = 0,column = 2)

window.mainloop() #Necessary for the exit button of window 