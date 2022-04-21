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



class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        #Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

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
        self.turnRight.bind(on_press=self.pressTurnRight)
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
        
    def pressReset(self,instance):
        talkBack("reset")

    def pressBackwards(self,instance):
        talkBack("Backwards")
        
    def pressForewards(self,instance):
        talkBack("Forewards")

    def pressTurnRight(self,instance):
        talkBack("Turn Right")
        
    def pressTurnLeft(self,instance):
        talkBack("Turn Left")

    def pressTwistRight(self,instance):
        talkBack("Twist Right")
        
    def pressTwistLeft(self,instance):
        talkBack("Twist Left")

    def pressLookUp(self,instance):
        talkBack("Look Up")
        
    def pressLookDown(self,instance):
        talkBack("Look Down")

    def pressLookRight(self,instance):
        talkBack("Look Right")
        
    def pressLookLeft(self,instance):
        talkBack("Look Left")
        

class MyApp(App):
    

    def build(self):
        Window.fullscreen = True
        return MyGridLayout()
##        self.window = GridLayout()
##        self.icon = 'hello.jpg'
##        self.window.cols = 1
##        self.window.pos_hint = {"center_x" : 0.5, "center_y" : 0.5}
##        self.window.add_widget(Image(source='hello.jpg',
##                                     size_hint = (3,3)))
##        self.question = Label(text="What is your robot's name?",
##                              font_size = 36,
##                              color = '#00abFF')
##        self.window.add_widget(self.question)
##        self.answer = TextInput(multiline = False,
##                                padding_y = (20 ,20),
##                                padding_x = (10,10),
##                                size_hint = (1, 0.9))
##        self.window.add_widget(self.answer)

##        self.button1 = Button(color =(1, 0, .65, 1),
##                     background_normal = 'Buttons/normal/RUN.png',
##                     background_down ='Buttons/down/RUN.png',
##                     size_hint = (.3, .3),
##                     pos_hint = {"x":0.35, "y":0.3}
##                   )
##        self.button1.bind(on_press = self.callback)
##        self.window.add_widget(self.button1)
        
        return self.window

    def callback(self, instance):
        print(instance)
        self.question.text = "Hello " + self.answer.text + "!"
        talkBack(self.question.text)
 

########These are the 7 actions our robot has to do########
    def motorsRun(speed, time, direction):
        pass

    def motorsTurn(direction, time):
        pass

    def headTilt():
        pass

    def headPan():
        pass

    def waistTurn():
        pass

    def speechInput():
        pass

    

def main():
    MyApp().run()
main()
