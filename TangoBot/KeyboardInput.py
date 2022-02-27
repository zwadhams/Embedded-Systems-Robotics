import time, serial, sys
import tkinter as tk

class Keyboard_Input:
    DEFAULT_VALID = {'<Up>', '<Left>', '<Down>', '<Right>', '<space>', '<z>', '<c>', '<w>', '<s>', '<a>', '<d>'}
    def __init__(self, win, control_list = DEFAULT_VALID):
        self.win = win
        self.control_list = control_list
        return
    pass