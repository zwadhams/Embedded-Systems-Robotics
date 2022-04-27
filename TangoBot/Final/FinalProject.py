import time, serial, sys
from tkinter import *
from TangoController import *

def main():

    usb = serial.Serial('/dev/ttyACM0')
    tangoController = Tango_Controller(usb)

    return
