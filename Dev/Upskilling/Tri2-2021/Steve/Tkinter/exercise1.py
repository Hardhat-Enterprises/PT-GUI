import tkinter
from tkinter import *
#start
#create a blank window
root = Tk()

#creating a label widget
#myLabel1 = Label(root, text="this is a label")
#myLabel2 = Label(root, text="Steve")
#shoving it onto the screen
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=1)
#end

e = Entry(root,width=50,borderwidth=5)
e.pack()

def myClick():
    myLabel = Label(root, text="look!" + e.get())
    myLabel.pack()

myButton = Button(root,text="Click Me!",command=myClick, fg="blue", bg="black")
myButton.pack()
#make it loops
root.mainloop()
