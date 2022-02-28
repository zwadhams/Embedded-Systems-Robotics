import time, serial, sys
import tkinter as tk
import keyboard as ky

class Keyboard_Input:
    DEFAULT_VALID = {'<Up>', '<Left>', '<Down>', '<Right>', '<space>', '<z>', '<c>', '<w>', '<s>', '<a>', '<d>'}
    def __init__(self, win, control_list = DEFAULT_VALID):
        self.win = win
        self.control_list = control_list
        return
    pass

while True:
    while ky.is_pressed("w") or ky.is_pressed("W"):
        #rightMotor
        #leftMotor
        print("Forward")
    
    while ky.is_pressed("w") or ky.is_pressed("W"):
        #rightMotor
        #leftMotor
        print("Forward")
        
    while ky.is_pressed("r") or ky.is_pressed("R"):
        #rightMotor negative value
        #leftMotor positive value
        print("Right")
        
    #rightMotor 6000 or off
    #leftMotor 6000 or off
