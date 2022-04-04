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
    def __init__(self, file:String):
        # Open File
        with open(file, "r") as f:
            # Read line by line
            line = f.readline()

            # Check U, u2, u3, ... un,(not case sensitive) Ignore lines with invalid syntax and comments
            # Comments are marked with # at the beginning of the line
            if line[0] == "#": # Comments
                pass
            elif line[0] == "u": #
                





        
        # Then parse character by character to find defined characters
        # "" ~ [] _ $  Check the 2022DialogAssignment Document
        # Ignore ? , . ! (Special characters)




        return


    

    pass