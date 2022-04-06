import _thread, threading
from tokenize import String
import speech_recognition as sr
import time

class Conversation:

    def __init__(self):
        self.currentPhrase = ""
        self.ready = False
        return

    def speak_thread(self):
        # Speak the currentPhrase when ready is set to true

        if self.ready:
            #speak
            print(self.currentPhrase)
        return

    def listen_thread(self):
        # Listen to the user (Main Thread)
        while(True):
            r = sr.Recognizer()
            speech = sr.Microphone(device_index=6)
            with speech as source:
                audio = r.listen(source, phrase_time_limit=3)
            try:
                recog = r.recognize_google(audio, language = 'en-US')



            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


        return

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
