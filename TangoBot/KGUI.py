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

    #commandArray = [0, 0, 0, 0, 0, 0, 0, 0]
    
    def __init__(self, **kwargs):
        #Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        self.commandArray = [0, 0, 0, 0, 0, 0, 0, 0]
        self.index = 0
        #Set colums
        self.rows = 1
        self.cols = 9

        self.left_grid = GridLayout()
        self.left_grid.rows = 7
        self.left_grid.cols = 2

        self.right_grid = GridLayout()
        self.right_grid.rows = 2
        self.right_grid.cols = 4
        

        #add widgets
        self.lookLeft = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookLeft.png',
                    background_down ='Buttons/down/lookLeft.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookLeft.bind(on_click=self.pressLookLeft)
        self.left_grid.add_widget(self.lookLeft)
        ####################################################
        self.lookRight = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookRight.png',
                    background_down ='Buttons/down/lookRight.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookRight.bind(on_click=self.pressLookRight)
        self.left_grid.add_widget(self.lookRight)
        ####################################################
        self.lookDown = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookDown.png',
                    background_down ='Buttons/down/lookDown.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookDown.bind(on_click=self.pressLookDown)
        self.left_grid.add_widget(self.lookDown)
        ####################################################
        self.lookUp = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookUp.png',
                    background_down ='Buttons/down/lookUp.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookUp.bind(on_click=self.pressLookUp)
        self.left_grid.add_widget(self.lookUp)
        ####################################################
        self.twistLeft = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/twistLeft.png',
                    background_down ='Buttons/down/twistLeft.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.twistLeft.bind(on_click=self.pressTwistLeft)
        self.left_grid.add_widget(self.twistLeft)
        ####################################################
        self.twistRight = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/twistRight.png',
                    background_down ='Buttons/down/twistRight.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.twistRight.bind(on_click=self.pressTwistRight)
        self.left_grid.add_widget(self.twistRight)
        ####################################################
        self.turnLeft = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/turnLeft.png',
                    background_down ='Buttons/down/turnLeft.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.turnLeft.bind(on_click=self.pressTurnLeft)
        self.left_grid.add_widget(self.turnLeft)
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
        self.left_grid.add_widget(self.turnRight)
        ####################################################
        self.Forewards = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/Forewards.png',
                    background_down ='Buttons/down/Forewards.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.Forewards.bind(on_click=self.pressForewards)
        self.left_grid.add_widget(self.Forewards)
        ####################################################
        self.Backwards = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/Backwards.png',
                    background_down ='Buttons/down/Backwards.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.Backwards.bind(on_click=self.pressBackwards)
        self.left_grid.add_widget(self.Backwards)
        ####################################################
        self.RUN = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/RUN.png',
                    background_down ='Buttons/down/RUN.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.RUN.bind(on_click=self.pressRUN)
        self.left_grid.add_widget(self.RUN)
        ####################################################
        self.reset = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/reset.png',
                    background_down ='Buttons/down/reset.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.reset.bind(on_click=self.pressReset)
        self.left_grid.add_widget(self.reset)
        ####################################################
        self.mic = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/mic.png',
                    background_down ='Buttons/down/mic.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.mic.bind(on_click=self.pressReset)
        self.left_grid.add_widget(self.mic)
        ####################################################
        self.add_widget(self.left_grid)

        #erase stuf and QUE
        word1 = "#"
        self.que1 = Button(color =(1, 0, .65, 1),
                            text= word1,
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.que1.bind(on_click=self.pressReset)
        self.right_grid.add_widget(self.que1)
        ####################################################
        word2 = "#"
        self.que2 = Button(color =(1, 0, .65, 1),
                            text= word2,
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.que2.bind(on_click=self.pressReset)
        self.right_grid.add_widget(self.que2)
        ####################################################
        word3 = "#"
        self.que3 = Button(color =(1, 0, .65, 1),
                            text= word3,
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.que3.bind(on_click=self.pressReset)
        self.right_grid.add_widget(self.que3)
        ####################################################
        word4 = "#"
        self.que4 = Button(color =(1, 0, .65, 1),
                            text= word4,
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.que4.bind(on_click=self.pressReset)
        self.right_grid.add_widget(self.que4)
        ####################################################
        word5 = "#"
        self.que5 = Button(color =(1, 0, .65, 1),
                            text= word5,
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.que5.bind(on_click=self.pressReset)
        self.right_grid.add_widget(self.que5)
        ####################################################
        word6 = "#"
        self.que6 = Button(color =(1, 0, .65, 1),
                            text= word6,
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.que6.bind(on_click=self.pressReset)
        self.right_grid.add_widget(self.que6)
        ####################################################
        word7 = "#"
        self.que7 = Button(color =(1, 0, .65, 1),
                            text= word7,
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.que7.bind(on_click=self.pressReset)
        self.right_grid.add_widget(self.que7)
        ####################################################
        word8 = "#"
        self.que8 = Button(color =(1, 0, .65, 1),
                            text= word8,
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.que8.bind(on_click=self.pressReset)
        self.right_grid.add_widget(self.que8)
        ####################################################
        self.add_widget(self.right_grid)


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
        pass
        

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
