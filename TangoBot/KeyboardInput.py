#import time, serial, sys
from tkinter import *

root = Tk()
root.title('Robot')
root.geometry("400x400")

def forward(e):
    myLabel = Label(root, text="Forward")
    myLabel.pack()

def backward(e):
    myLabel = Label(root, text="Backward")
    myLabel.pack()

def turnRight(e):
    myLabel = Label(root, text="Turning Right")
    myLabel.pack()

def turnLeft(e):
    myLabel = Label(root, text="Turning Left")
    myLabel.pack()

def twistRight(e):
    myLabel = Label(root, text="Twisting Right")
    myLabel.pack()

def twistLeft(e):
    myLabel = Label(root, text="Twisting Left")
    myLabel.pack()

def lookUp(e):
    myLabel = Label(root, text="Looking Up")
    myLabel.pack()

def lookDown(e):
    myLabel = Label(root, text="Looking Down")
    myLabel.pack()

def lookRight(e):
    myLabel = Label(root, text="Looking Right")
    myLabel.pack()

def lookLeft(e):
    myLabel = Label(root, text="Looking Left")
    myLabel.pack()

def speed(e):
    myLabel = Label(root, text="Speed 3")
    myLabel.pack()

def speedMed(e):
    myLabel = Label(root, text="Speed 2")
    myLabel.pack()

def speedLow(e):
    myLabel = Label(root, text="Speed 1")
    myLabel.pack()

root.bind('<w>', forward)
root.bind('<s>', backward)
root.bind('<d>', turnRight)
root.bind('<a>', turnLeft)
root.bind('<e>', twistRight)
root.bind('<q>', twistLeft)
root.bind('<Up>', lookUp)
root.bind('<Down>', lookDown)
root.bind('<Right>', lookRight)
root.bind('<Left>', lookLeft)
root.bind(3, speedHigh)
root.bind(2, speedMed)
root.bind(1, speedLow)


root.mainloop()


#------------------
#class Keyboard_Input:
#    DEFAULT_VALID = {'<Up>', '<Left>', '<Down>', '<Right>', '<space>', '<z>', '<c>', '<w>', '<s>', '<a>', '<d>'}
#    def __init__(self, win, control_list = DEFAULT_VALID):
#        self.win = win
#        self.control_list = control_list
#        return
#    pass
