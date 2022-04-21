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



class MyGridLayout(GridLayout):
    # Initialize infinite keywords

    #commandArray = [0, 0, 0, 0, 0, 0, 0, 0]
    
    def __init__(self, **kwargs):
        #Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        self.commandArray = [0, 0, 0, 0, 0, 0, 0, 0]
        self.index = 0
        #Set colums
        self.rows = 6
        self.columns = 3

        #add widgets
        self.lookLeft = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookLeft.png',
                    background_down ='Buttons/down/lookLeft.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookLeft.bind(on_press=self.pressLookLeft)
        self.add_widget(self.lookLeft)
        ####################################################
        self.lookRight = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookRight.png',
                    background_down ='Buttons/down/lookRight.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookRight.bind(on_press=self.pressLookRight)
        self.add_widget(self.lookRight)
        ####################################################
        self.lookDown = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookDown.png',
                    background_down ='Buttons/down/lookDown.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookDown.bind(on_press=self.pressLookDown)
        self.add_widget(self.lookDown)
        ####################################################
        self.lookUp = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookUp.png',
                    background_down ='Buttons/down/lookUp.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookUp.bind(on_press=self.pressLookUp)
        self.add_widget(self.lookUp)
        ####################################################
        self.twistLeft = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/twistLeft.png',
                    background_down ='Buttons/down/twistLeft.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.twistLeft.bind(on_press=self.pressTwistLeft)
        self.add_widget(self.twistLeft)
        ####################################################
        self.twistRight = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/twistRight.png',
                    background_down ='Buttons/down/twistRight.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.twistRight.bind(on_press=self.pressTwistRight)
        self.add_widget(self.twistRight)
        ####################################################
        self.turnLeft = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/turnLeft.png',
                    background_down ='Buttons/down/turnLeft.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.turnLeft.bind(on_press=self.pressTurnLeft)
        self.add_widget(self.turnLeft)
        ####################################################
        self.turnRight = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/turnRight.png',
                    background_down ='Buttons/down/turnRight.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.turnRight.bind(on_click=self.pressTurnRight)
        self.add_widget(self.turnRight)
        ####################################################
        self.Forewards = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/Forewards.png',
                    background_down ='Buttons/down/Forewards.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.Forewards.bind(on_press=self.pressForewards)
        self.add_widget(self.Forewards)
        ####################################################
        self.Backwards = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/Backwards.png',
                    background_down ='Buttons/down/Backwards.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.Backwards.bind(on_press=self.pressBackwards)
        self.add_widget(self.Backwards)
        ####################################################
        self.RUN = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/RUN.png',
                    background_down ='Buttons/down/RUN.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.RUN.bind(on_press=self.pressRUN)
        self.add_widget(self.RUN)
        ####################################################
        self.reset = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/reset.png',
                    background_down ='Buttons/down/reset.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.reset.bind(on_press=self.pressReset)
        self.add_widget(self.reset)
        ####################################################

    def pressRUN(self,instance):
        talkBack("RUN")
        for i in self.commandArray:
            if i == 1: #Backwards motors
                self.motorsRun()
                print("Backwards motors")
            elif i == 2: #Forewards motors
                self.motorsRun()
                print("forewards motors")
            elif i == 3: #Right motors
                self.motorsTurn()
                print("right motors")
            elif i == 4: #Left motors
                self.motorsTurn()
                print("left motors")
            elif i == 5: #waist turn right
                self.waistTurn()
                print("waist turn right")
            elif i == 6: #waist turn left
                self.waistTurn()
                print("waist turn left")
            elif i == 7: #head tilt up
                self.headTilt()
                print("head tilt up")
            elif i == 8: #head tilt down
                self.headTilt()
                print("head tilt down")
            elif i == 9: #head pan right
                self.headPan()
                print("head pan right")
            elif i == 10: #head pan left
                self.headPan()
                print("head pan left")
        
    def pressReset(self,instance):
        self.commandArray = [0, 0, 0, 0, 0, 0, 0, 0]
        print(self.commandArray)
        self.index = 0
        talkBack("reset")

    def pressBackwards(self,instance):
        command = 1
        self.commandArray[self.index] = command
        self.index = (self.index+1)%8
        talkBack("Backwards")
        print(self.commandArray)
        
    def pressForewards(self,instance):
        command = 2
        self.commandArray[self.index] = command
        self.index = (self.index+1)%8
        talkBack("Forewards")
        print(self.commandArray)

    def pressTurnRight(self,instance):
        command = 3
        self.commandArray[self.index] = command
        self.index = (self.index+1)%8
        talkBack("Turn Right")
        print(self.commandArray)
        
    def pressTurnLeft(self,instance):
        command = 4
        self.commandArray[self.index] = command
        self.index = (self.index+1)%8
        talkBack("Turn Left")
        print(self.commandArray)

    def pressTwistRight(self,instance):
        command = 5
        self.commandArray[self.index] = command
        self.index = (self.index+1)%8
        talkBack("Twist Right")
        print(self.commandArray)
        
    def pressTwistLeft(self,instance):
        command = 6
        self.commandArray[self.index] = command
        self.index = (self.index+1)%8
        talkBack("Twist Left")
        print(self.commandArray)

    def pressLookUp(self,instance):
        command = 7
        self.commandArray[self.index] = command
        self.index = (self.index+1)%8
        talkBack("Look Up")
        print(self.commandArray)
        
    def pressLookDown(self,instance):
        command = 8
        self.commandArray[self.index] = command
        self.index = (self.index+1)%8
        talkBack("Look Down")
        print(self.commandArray)

    def pressLookRight(self,instance):
        command = 9
        self.commandArray[self.index] = command
        self.index = (self.index+1)%8
        talkBack("Look Right")
        print(self.commandArray)
        
    def pressLookLeft(self,instance):
        command = 10
        self.commandArray[self.index] = command
        self.index = (self.index+1)%8
        talkBack("Look Left")
        print(self.commandArray)

    #####Actual moving stuff#######

    def motorsRun(self):#(speed, time, direction)
        pass

    def motorsTurn(self):#(direction, time)
        pass

    def headTilt(self):
        pass

    def headPan(self):
        pass

    def waistTurn(self):
        pass

    def speechInput(self):
        talkBack("Say something please")
        flag = True
        r = sr.Recognizer()
        speech = sr.Microphone()
        with speech as source:
            print("initialize")
            #audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit = 3)
            while(flag):
                try:
                    print("hit the try")
                    recog = r.recognize_google(audio, language = 'en-US')
                    if recog:
                        talkBack("Okay I heard you but I really dont care")
                        flag = False
                    else:
                        print("hit the else")
                        talkBack("Yeah you didnt say anything, whatever")
                        flag = False
                except sr.UnknownValueError:
                   talkBack("bbebrbbbrbbrbe, dead")
        

class MyApp(App):
    

    def build(self):
        #Window.fullscreen = True
        Window.clearcolor = (1,0,0,1)
        return MyGridLayout()
        

    def callback(self, instance):
        print(instance)
        self.question.text = "Hello " + self.answer.text + "!"
        talkBack(self.question.text)
 

########These are the 7 actions our robot has to do########
    

    

def main():
    MyApp().run()
main()
