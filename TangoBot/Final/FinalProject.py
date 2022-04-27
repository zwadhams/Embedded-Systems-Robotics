import time, serial, sys
from tkinter import *
from TangoController import *

def main():

    usb = serial.Serial('/dev/ttyACM0')

    tangoController = Tango_Controller(usb)
    #tangoController.adjust_backward_forward(2)
    #time.sleep(0.5)
    #tangoController.stop()
    #tangoController.control_servo("Shoulder", 7500)
    #time.sleep(1)
    #tangoController.control_servo("Shoulder", 4500)
    #time.sleep(0.5)
    #tangoController.adjust_backward_forward(-2)
    #time.sleep(0.5)
    #tangoController.stop()
    
    tangoController.adjust_left_right(2)
    time.sleep(2.3)
    tangoController.stop()
    tangoController.adjust_left_right(-2)
    time.sleep(3)
    tangoController.stop()

    tangoController.adjust_left_right(2)
    time.sleep(4.6)
    tangoController.stop()

    return

main()
