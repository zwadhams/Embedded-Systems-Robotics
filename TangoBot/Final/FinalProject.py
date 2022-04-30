import time, serial, sys
from tkinter import *
from TangoController import *
import os
from playsound import playsound
import speech_recognition as sr
import pyttsx3


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
    speech = sr.Microphone()

    with speech as source:
        audio = r.adjust_for_ambient_noise(source)
        while(flag):
            try:
                audio = r.listen(source, phrase_time_limit = 4)
                inputSpeech = r.recognize_google(audio, language = 'en-US')
                flag = False
            except sr.UnknownValueError:
                speak("What?")
    return inputSpeech

def main():


    # turnRight()
    # time.sleep(0.2)
    # turnLeft()
    # time.sleep(0.2)
    # turn180()
    # attack()
    # backward()
    # forward()
    # speak("Hello World")
    print(listen())
    return


usb = serial.Serial('/dev/ttyACM0')

tangoController = Tango_Controller(usb)

voice = pyttsx3.init()

main()
