import time, serial, sys
from tkinter import *
from TangoController import *
import os
from playsound import playsound
import speech_recognition as sr
import pyttsx3
import random
import math
import pathlib, os, sys


class Node:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.visited = False
        self.previous = None
        self.cardinal = ""
        self.holdsKey = False
        self.enemyType = ""

    def __str__(self):
        tempList = self.connected_to.keys()
        tempStr = ""
        for key in tempList:
            tempStr += "Node " + str(key.id) + " " + self.connected_to[key] +", "
        return str(self.id) + ' is connected to: ' + tempStr


    def get_id(self): #return the number of the node
        return self.id

    def get_connections(self):
        return self.connected_to.keys()

    def set_visited(self): #maks this node as visited
        self.visited = True

    def set_previous(self): #marks the previous node 
        self.previous = prev

    def addEnemyType(self, enemyType): #0 is none, 1 is easy, 2 is hard
        if enemyType == 0:
            self.enemyType = "None"
        elif enemyTpe == 1:
            self.enemyType = "Easy"
        elif enemyType == 2:
            self.enemyType = "Hard"
    

def turnLeft():
    tangoController.adjust_left_right(3)
    time.sleep(0.55)
    tangoController.stop()
    
def turnRight():
    tangoController.adjust_left_right(-3)
    time.sleep(0.61)
    tangoController.stop()

def turn180():
    tangoController.adjust_left_right(3)
    time.sleep(1.082)
    tangoController.stop()

def forward():
    tangoController.adjust_backward_forward(3)
    time.sleep(0.4)
    tangoController.stop()

def backward():
    tangoController.adjust_backward_forward(-3)
    time.sleep(0.4)
    tangoController.stop()

def attack():
    tangoController.adjust_backward_forward(2)
    time.sleep(0.5)
    tangoController.stop()
    tangoController.control_servo("Shoulder", 7500)
    time.sleep(1)
    tangoController.control_servo("Shoulder", 4500)
    time.sleep(0.5)
    tangoController.adjust_backward_forward(-2)
    time.sleep(0.5)
    tangoController.stop()

def speak(text:str):
    # tts = gtts.gTTS(text)
    # tts.save("responseMessage.mp3")
    # playsound("responseMessage.mp3")
    # print(text)

    # #has to delet or it will error out
    # if os.path.exists("responseMessage.mp3"):
    #   os.remove("responseMessage.mp3")
    # else:
    #   print("The file does not exist")
    voice.say(text)
    voice.runAndWait()

def listen():

    inputSpeech = ""
    
    speak("Well?")
    flag = True
    r = sr.Recognizer()
    r.energy_threshold = 1568
    r.dynamic_energy_threshold = True
    speech = sr.Microphone()

    with speech as source:
        # audio = r.adjust_for_ambient_noise(source)
        while(flag):
            try:
                audio = r.listen(source, phrase_time_limit = 4)
                inputSpeech = r.recognize_google(audio, language = 'en-US')
                flag = False
            except sr.UnknownValueError:
                speak("What?")
    return inputSpeech

def changeDirection(current_direction:str, chooses):
    choosesStr = ""
    for choose in chooses:
        choosesStr += choose.lower() + ","
    cur_dir = current_direction.lower()
    invalid = True
    while (invalid):
        speak("Currently looking "+cur_dir)
        speak("I can go "+choosesStr)
        speak("Which direction should I go?")
        dir_input = listen().lower()
        # dir_input = "west"
        cardinal = ["north", "east", "south", "west"]
        if (dir_input in cardinal) and (dir_input in chooses):
            if (dir_input != cur_dir):
                to_dir_index = cardinal.index(dir_input)
                from_dir_index = cardinal.index(cur_dir)
                dif = to_dir_index - from_dir_index
                if (abs(dif) == 2):
                    turn180()
                    time.sleep(0.2)
                    forward()
                elif ((dif == -1) or (dif == 3)):
                    turnRight()
                    time.sleep(0.2)
                    forward()
                elif ((dif == 1) or (dif == -3)):
                    turnLeft()
                    time.sleep(0.2)
                    forward()
                cur_dir = dir_input
            else:
                forward()
            invalid = False
        else:
            speak("Cannot go that way, Try Again")
    return cur_dir

def main():
    return


usb = serial.Serial('/dev/ttyACM0')
tangoController = Tango_Controller(usb)
voice = pyttsx3.init()

main()
