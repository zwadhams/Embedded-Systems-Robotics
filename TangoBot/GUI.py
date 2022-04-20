import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from TextToSpeech import *

import speech_recognition as sr
import time, serial, sys
from TangoController import *
usb = serial.Serial('/dev/ttyACM0')
tangoController = Tango_Controller(usb)
from tkinter import *
from time import sleep

self = Tk()


def forward():
        if (tangoController.motors['Right_Wheel'].get_speed() == 0):
                tangoController.adjust_backward_forward(2)
        else:
                tangoController.adjust_backward_forward(1)

def backward():
        if (tangoController.motors['Right_Wheel'].get_speed() == 0):
                tangoController.adjust_backward_forward(-2)
        else:
                tangoController.adjust_backward_forward(-1)

def turnRight():
        tangoController.adjust_left_right(3)

def turnLeft():
        tangoController.adjust_left_right(-3)

def twistRight():
        tangoController.adjust_pan_waist(-1)

def twistLeft():
        tangoController.adjust_pan_waist(1)

def lookUp():
        tangoController.adjust_tilt_neck(1)

def lookDown():
        tangoController.adjust_tilt_neck(-1)

def lookRight():
        tangoController.adjust_pan_neck(-1)

def lookLeft():
        tangoController.adjust_pan_neck(1)


class MyApp(App):

    def build(self):
        Window.fullscreen = True
        self.window = GridLayout()
        self.icon = 'hello.jpg'
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x" : 0.5, "center_y" : 0.5}
        self.window.add_widget(Image(source='hello.jpg',
                                     size_hint = (3,3)))
        self.question = Label(text="What is your robot's name?",
                              font_size = 36,
                              color = '#00abFF')
        self.window.add_widget(self.question)
        self.answer = TextInput(multiline = False,
                                padding_y = (20 ,20),
                                padding_x = (10,10),
                                size_hint = (1, 0.9))
        self.window.add_widget(self.answer)
        self.button = Button(text="Talk")
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)
        
        return self.window

    def callback(self, instance):
        print(instance)
        self.question.text = "Hello " + self.answer.text + "!"
 

########These are the 7 actions our robot has to do########
    def motorsRun(speed, time, direction):
        pass

    def motorsTurn(direction, time):
        pass

    def headTilt():
        lookUp()
        lookDown()

    def headPan():
        lookRight()
        lookLeft()

    def waistTurn():
        twistRight()
        twistLeft()

    def speechInput():
        talkBack("Say something please")
        flag = True
        while(flag):
            r = sr.Recognizer()
            speech = sr.Microphone(device_index=0)
            with speech as source:
                audio = r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                recog = r.recognize_google(audio, language = 'en-US')
                if recog:
                    talkBack("Okay I heard you but I really dont care")
                    flag = False
                else:
                    talkBack("Yeah you didnt say anything, whatever")
                    flag = False
            except sr.UnknownValueError:
               talkBack("bbebrbbbrbbrbe, dead")

    def speechOutput(userInput):
        talkBack(userInput)
        

    speechOutput("nope")

def main():
    MyApp().run()
main()
