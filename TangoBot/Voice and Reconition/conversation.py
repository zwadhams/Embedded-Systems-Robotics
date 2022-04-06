import _thread, threading
from tokenize import String
import speech_recognition as sr
import time
import pyttsx3

class Conversation:

    def __init__(self):
        self.currentPhrase = ""
        self.ready = False
        self.engine = pyttsx3.init()
        self.voice_num = 2
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[self.voice_num].id)
        self.speakTh = True
        self.listenTh = True
        return

    def speak_thread(self):
        # Speak the currentPhrase when ready is set to true
        while(self.speakTh):
            if self.ready:
                #speak
                self.engine.say(self.currentPhrase)
                self.engine.runAndWait()
                print(self.currentPhrase)
                self.currentPhrase = ""
                self.ready = False

    def listen_thread(self):
        # Listen to the user (Main Thread)
        while(self.listenTh):
            r = sr.Recognizer()
            speech = sr.Microphone(device_index=6)
            with speech as source:
                audio = r.listen(source, phrase_time_limit=3)
            try:
                recog = r.recognize_google(audio, language = 'en-US')
                # Test
                self.currentPhrase = recog
                self.ready = True
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    pass

class Dialog_Engine:
    
    def responseParse(l):
        if l[1] == ':':
            pass
            #we need some functionality to check the stuff
        #runs command if the 
        
    def definitionParse(l):
        # this definies a greeting variable and is given three values in square brackets
        pass
    
    def __init__(self, file:String):
        # Open File
        with open(file, "r") as f:
            # Read line by line
            line = f.readline()

            #for lines in f: might need some looping stuff to keep reading lines
            
            # Check U, u2, u3, ... un,(not case sensitive) Ignore lines with invalid syntax and comments
            # Comments are marked with # at the beginning of the line
            if line[0] == "#": # Comments
                pass
            elif line[0] == "u": 
                responseParse(line) #will eventually parse through the 
            elif line[0] == "~":
                definitionParse(line)
                #does something, not sure what that symbol means
                
            else:
                pass
               
        
        # Then parse character by character to find defined characters
        # "" ~ [] _ $  Check the 2022DialogAssignment Document
        # Ignore ? , . ! (Special characters)

        return
    
    pass

inst = Conversation()

_thread.start_new_thread(inst.speak_thread,())
inst.listen_thread()
