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
        self.foo = "Nothing Here"

    def __str__(self):
            return str(self.id) + ' adjacent: ' + str([(x.id, x.foo) for x in self.connected_to])

    def get_id(self): #return the number of the node
        return self.id

    def get_connections(self):
        return self.connected_to.keys()

    def set_visited(self): #maks this node as visited
        self.visited = True

    def set_previous(self): #marks the previous node 
        self.previous = prev


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
    monster = True
    cornerList = [1, 3, 11, 13]
    playerLocation = random.choice(cornerList) #gets starting location
    cornerList.remove(playerLocation) #removes the starting location
    endLocation = random.choice(cornerList) #this is the ending location


    if (monster):
        speak("Fight Time")
        fight = random.choice([True, False, False, False])
        if fight:
            speak("En garde")
            attack()
        else:
            speak("I dont wanna fight")
    
    
    ################################
    #creates nodes
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n11 = Node(11)
    n12 = Node(12)
    n13 = Node(13)

    #creates node connections
    n1.connected_to = {n2}
    n2.connected_to = {n1, n3, n7}
    n3.connected_to = {n2, n8}
    n6.connected_to = {n11, n7}
    n7.connected_to = {n2, n6, n12}
    n8.connected_to = {n3}
    n11.connected_to = {n6}
    n12.connected_to = {n7, n13}
    n13.connected_to = {n12}
    #################################
    
    # current_direction = "north"
    # testChooses = ["north", "south", "east"]
    # current_direction = changeDirection(current_direction, testChooses)
    # speak(current_direction)

    # turnRight()
    # time.sleep(0.2)
    # turnLeft()
    # time.sleep(0.2)
    # turn180()
    # attack()
    # backward()
    # forward()
    # speak("Hello World")
    # print(listen())
    return


usb = serial.Serial('/dev/ttyACM0')
tangoController = Tango_Controller(usb)
voice = pyttsx3.init()

main()
