#import time, serial, sys
from tkinter import *

root = Tk()
root.title('Robot')
root.geometry("400x400")

def clicker(e):
    myLabel = Label(root, text="Forward")
    myLabel.pack()


root.bind('<w>', clicker)


root.mainloop()


#------------------
#class Keyboard_Input:
#    DEFAULT_VALID = {'<Up>', '<Left>', '<Down>', '<Right>', '<space>', '<z>', '<c>', '<w>', '<s>', '<a>', '<d>'}
#    def __init__(self, win, control_list = DEFAULT_VALID):
#        self.win = win
#        self.control_list = control_list
#        return
#    pass
