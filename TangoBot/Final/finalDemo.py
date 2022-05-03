from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random
import pyttsx3
import time
#from FinalProject import *


class MyLayout(GridLayout):
    img = Image(source='images/maps/One.png',
                keep_ratio= False,
                allow_stretch = True
                )
    key = Button(color =(1, 0, .65, 1),
                 background_normal = 'images/items/nokey.png',
                 size_hint_y = None,
                 height=50,
                   )

    health = Button(color =(1, 0, .65, 1),
                    text= "Health 60/60",
                    size_hint_y = None,
                    height=50,
                    )

    map = 1
    enemyID = 2
    
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1

        self.bottom = GridLayout(size_hint_y = None,
                    height=50)
        self.bottom.cols = 2
        
        self.add_widget(self.img)
        self.location
        self.enemy
        self.add_widget(self.bottom)


        self.key.bind(on_press=self.enemy)
        self.bottom.add_widget(self.key)
        

        
        self.health.bind(on_press=self.healing)
        self.bottom.add_widget(self.health)
        

    def location(self, instance):        
        if self.map == 1:
            self.img.source = 'images/maps/One.png'
        elif self.map == 2:
            self.img.source = 'images/maps/two.png'
        elif self.map == 3:
            self.img.source = 'images/maps/three.png'
        elif self.map == 4:
            self.img.source = 'images/maps/six.png'
        elif self.map == 5:
            self.img.source = 'images/maps/seven.png'
        elif self.map == 6:
            self.img.source = 'images/maps/eight.png'
        elif self.map == 7:
            self.img.source = 'images/maps/eleven.png'
        elif self.map == 8:
            self.img.source = 'images/maps/twelve.png'
        elif self.map == 9:
            self.img.source = 'images/maps/thirteen.png'


    def enemy(self, instance):
        if self.enemyID == 1:
            self.img.source = 'images/enemy/slime.gif'
            voice.say("Splash")
            voice.runAndWait()
            voice.say("Run or Fight Slime")
            voice.runAndWait()
        elif self.enemyID == 2:
            self.img.source = 'images/enemy/boss.gif'
            voice.say("Screeeeeeetch")
            voice.runAndWait()
            voice.say("Run or Fight Skeleton Mutant")
            voice.runAndWait()
            

    def healing(self, instance):
        self.img.source = 'images/items/healing.gif'
        voice.say("Relax you are being healed")
        voice.runAndWait()
        self.health.text = "Health 60/60"

    def keyFound(self, instance):
        self.key.background_normal = 'images/items/key.png'
        voice.runAndWait()
        self.health.text = "Key Found"
        
        

    def damage(self, instance):
        self.health.text = "Health 50/60"
        voice.say("Relax you are being healed")
        voice.runAndWait()
        

class MyApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        Window.size = (800,480)
        Window.top = 10
        Window.left = 50
        return MyLayout()

if __name__ == '__main__':

        
##    ################################
##    #creates nodes
##    n1 = Node(1)
##    n2 = Node(2)
##    n3 = Node(3)
##    n6 = Node(6)
##    n7 = Node(7)
##    n8 = Node(8)
##    n11 = Node(11)
##    n12 = Node(12)
##    n13 = Node(13)
##
##    #creates node connections
##    n1.connected_to = {n2:"East"}
##    n2.connected_to = {n1:"West", n3:"East", n7:"South"}
##    n3.connected_to = {n2:"West", n8:"South"}
##    n6.connected_to = {n11:"South", n7:"East"}
##    n7.connected_to = {n2:"North", n6:"West", n12:"South"}
##    n8.connected_to = {n3:"North"}
##    n11.connected_to = {n6:"North"}
##    n12.connected_to = {n7:"North", n13:"East"}
##    n13.connected_to = {n12:"West"}
##    #################################
##    
##    monster = True
##    cornerList = [1, 3, 11, 13]
##    playerLocation = random.choice(cornerList) #gets starting location
##    cornerList.remove(playerLocation) #removes the starting location
##    endLocation = random.choice(cornerList) #this is the ending location
##    cornerList.remove(endLocation) 
##    healLocation = random.choice(cornerList) #location of heal station
##    cornerList.remove(healLocation)
##    keyEnemyLocation = random.choice(cornerList) #location of emeny with key
##    cornerList.remove(keyEnemyLocation)
##
##    centerList = [2, 3, 6, 7, 12]
##
##    hardEnemy2 = random.choice(centerList)
##    centerList.remove(hardEnemy2)
##    print(centerList)
##    #all others should be easy enemies
##
##    if (monster):
##        speak("Fight Time")
##        fight = random.choice([True, False, False, False])
##        if fight:
##            speak("En garde")
##            attack()
##        else:
##            speak("I dont wanna fight")
## 
##    
##    
##    
##    # current_direction = "north"
##    # testChooses = ["north", "south", "east"]
##    # current_direction = changeDirection(current_direction, testChooses)
##    # speak(current_direction)
##
##    # turnRight()
##    # time.sleep(0.2)
##    # turnLeft()
##    # time.sleep(0.2)
##    # turn180()
##    # attack()
##    # backward()
##    # forward()
##    # speak("Hello World")
##    # print(listen())

    voice = pyttsx3.init()
    MyApp().run()

