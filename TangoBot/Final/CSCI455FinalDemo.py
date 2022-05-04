from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import kivy.clock
import random
import pyttsx3
# from movement import *

import math
import pathlib, os, sys
import time, serial
from TangoController import *
from playsound import playsound
import speech_recognition as sr

import threading

class Node:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.visited = False
        self.previous = None
        self.cardinal = ""
        self.holdsKey = False
        self.enemyType = ""
        self.exitLocation = False
        self.healStation = False
        self.startingNode = False
        self.currentNode = False
        self.curLookCard = "North"

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

    def get_cardinals(self):
        return self.connected_to.values()

    def get_enemyType(self):
        return self.enemyType

    def get_holdsKey(self):
        return self.holdsKey

    def get_healStation(self):
        return self.healStation

    def get_exitLocation(self):
        return self.exitLocation

    def set_visited(self): #maks this node as visited
        self.visited = True

    def set_previous(self): #marks the previous node 
        self.previous = prev

    def set_enemyType(self, enemyType): #0 is none, 1 is easy, 2 is hard
        if enemyType == 0:
            self.enemyType = "None"
        elif enemyType == 1:
            self.enemyType = "Easy"
        elif enemyType == 2:
            self.enemyType = "Hard"

    def set_exitLocation(self):
        self.exitLocation = True

    def set_holdsKey(self):
        self.holdsKey = True

    def set_healStation(self):
        self.healStation = True

    def set_startingNode(self):
        self.startingNode = True

###################################
    #Use these two to set or unset the current node
    def set_currentNode(self):
        self.currentNode = True

    def remove_currentNode(self):
        self.currentNode = False

    def get_currentNode(self):
        return self.currentNode


class MyLayout(GridLayout):


    map = 0
    enemyID = ""
    healthy = 60


    
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
                    text= ("Health " + str(healthy) + "/60"),
                    size_hint_y = None,
                    height=50,
                    )


        
    
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
        

        
        #self.health.bind(on_press=self.healing)
        self.bottom.add_widget(self.health)


        self.location()
        

    def location(self):        
        if self.map == 1:
            self.img.source = 'images/maps/One.png'
        elif self.map == 2:
            self.img.source = 'images/maps/two.png'
        elif self.map == 3:
            self.img.source = 'images/maps/three.png'
        elif self.map == 6:
            self.img.source = 'images/maps/six.png'
        elif self.map == 7:
            self.img.source = 'images/maps/seven.png'
        elif self.map == 8:
            self.img.source = 'images/maps/eight.png'
        elif self.map == 11:
            self.img.source = 'images/maps/eleven.png'
        elif self.map == 12:
            self.img.source = 'images/maps/twelve.png'
        elif self.map == 13:
            self.img.source = 'images/maps/thirteen.png'


    def enemy(self, instance):
        if self.enemyID == "Easy":
            self.img.source = 'images/enemy/slime.gif'
        elif self.enemyID == "Hard":
            self.img.source = 'images/enemy/boss.gif'
            

    def healing(self, instance):
        self.img.source = 'images/items/healing.gif'
        self.healthy = 60
        self.health.text = "Health " + str(self.healthy) + "/60"

    def keyFound(self):
        self.key.background_normal = 'images/items/key.png'
        
        
        

    def damage(self):
        if self.enemyID == 1:
            self.healthy = self.healthy - 5
            if self.healthy > 1:
                self.health.text = "Health " + str(self.healthy) + "/60"
            elif self.healthy < 1:
                self.dead
        elif self.enemyID == 2:
            if self.healthy > 20:
                self.healthy = self.healthy - 20
                self.health.text = "Health " + str(self.healthy) + "/60"
            elif self.healthy <= 20:
                self.dead()
            

    def dead(self):
        self.health.text = "Dead"
        self.img.source = 'images/youdied.gif'
        


class GameGUI(MyLayout):

    class GameMove:
        # Global Utils
        usb = serial.Serial('/dev/ttyACM0')
        tangoController = Tango_Controller(usb)
        voice = pyttsx3.init()
        def turnLeft():
            GameGUI.GameMove.tangoController.adjust_left_right(3)
            time.sleep(0.55)
            GameGUI.GameMove.tangoController.stop()
            
        def turnRight():
            GameGUI.GameMove.tangoController.adjust_left_right(-3)
            time.sleep(0.61)
            GameGUI.GameMove.tangoController.stop()

        def turn180():
            GameGUI.GameMove.tangoController.adjust_left_right(3)
            time.sleep(1.082)
            GameGUI.GameMove.tangoController.stop()

        def forward():
            GameGUI.GameMove.tangoController.adjust_backward_forward(3)
            time.sleep(0.4)
            GameGUI.GameMove.tangoController.stop()

        def backward():
            GameGUI.GameMove.tangoController.adjust_backward_forward(-3)
            time.sleep(0.4)
            GameGUI.GameMove.tangoController.stop()

        def attack():
            GameGUI.GameMove.tangoController.adjust_backward_forward(2)
            time.sleep(0.5)
            GameGUI.GameMove.tangoController.stop()
            GameGUI.GameMove.tangoController.control_servo("Shoulder", 7500)
            time.sleep(1)
            GameGUI.GameMove.tangoController.control_servo("Shoulder", 4500)
            time.sleep(0.5)
            GameGUI.GameMove.tangoController.adjust_backward_forward(-2)
            time.sleep(0.5)
            GameGUI.GameMove.tangoController.stop()

        def speak(text:str):
            GameGUI.GameMove.voice.say(text)
            GameGUI.GameMove.voice.runAndWait()

        def listen():

            inputSpeech = ""
            
            GameGUI.GameMove.speak("Well?")
            flag = True
            r = sr.Recognizer()
            # r.energy_threshold = 1568
            # r.dynamic_energy_threshold = True
            speech = sr.Microphone()

            with speech as source:
                # audio = r.adjust_for_ambient_noise(source)
                while(flag):
                    try:
                        audio = r.listen(source, phrase_time_limit = 4)
                        inputSpeech = r.recognize_google(audio, language = 'en-US')
                        flag = False
                    except sr.UnknownValueError:
                        GameGUI.GameMove.speak("What?")
            return inputSpeech

        def changeDirection(current_direction:str, chooses):
            choosesStr = ""
            lowerChooses = []
            for choose in chooses:
                lowerChooses.append(choose.lower())
            for choose in chooses:
                choosesStr += choose.lower() + ","
            cur_dir = current_direction.lower()
            invalid = True
            while (invalid):
                GameGUI.GameMove.speak("Currently looking "+cur_dir)
                GameGUI.GameMove.speak("I can go "+choosesStr)
                print("I can go "+choosesStr)
                GameGUI.GameMove.speak("Which direction should I go?")
                dir_input = GameGUI.GameMove.listen().lower()
                # dir_input = "west"
                print(dir_input)
                cardinal = ["north", "east", "south", "west"]
                if (dir_input in cardinal) and (dir_input in lowerChooses):
                    if (dir_input != cur_dir):
                        to_dir_index = cardinal.index(dir_input)
                        from_dir_index = cardinal.index(cur_dir)
                        dif = to_dir_index - from_dir_index
                        if (abs(dif) == 2):
                            GameGUI.GameMove.turn180()
                            time.sleep(0.2)
                            GameGUI.GameMove.forward()
                        elif ((dif == -1) or (dif == 3)):
                            GameGUI.GameMove.turnRight()
                            time.sleep(0.2)
                            GameGUI.GameMove.forward()
                        elif ((dif == 1) or (dif == -3)):
                            GameGUI.GameMove.turnLeft()
                            time.sleep(0.2)
                            GameGUI.GameMove.forward()
                        cur_dir = dir_input
                    else:
                        GameGUI.GameMove.forward()
                    invalid = False
                else:
                    GameGUI.GameMove.speak("Cannot go that way, Try Again")
            return cur_dir

    class GameLogic:
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
        n1.connected_to = {n2:"East"}
        n2.connected_to = {n1:"West", n3:"East", n7:"South"}
        n3.connected_to = {n2:"West", n8:"South"}
        n6.connected_to = {n11:"South", n7:"East"}
        n7.connected_to = {n2:"North", n6:"West", n12:"South"}
        n8.connected_to = {n3:"North"}
        n11.connected_to = {n6:"North"}
        n12.connected_to = {n7:"North", n13:"East"}
        n13.connected_to = {n12:"West"}

        print(n1)
        print(n2)
        print(n3)
        print(n6)
        print(n7)
        print(n8)
        print(n11)
        print(n12)
        print(n13)
        print("------------")
        cornerList = [1, 8, 11, 13]
        playerStartLocation = random.choice(cornerList) #gets starting location
        cornerList.remove(playerStartLocation) #removes the starting location
        endLocation = random.choice(cornerList) #this is the ending location
        cornerList.remove(endLocation)
        healLocation = random.choice(cornerList) #location of heal station
        cornerList.remove(healLocation)
        keyEnemyLocation = random.choice(cornerList) #location of emeny with key
        cornerList.remove(keyEnemyLocation)

        centerList = [2, 3, 6, 7, 12]

        hardEnemy2 = random.choice(centerList)
        centerList.remove(hardEnemy2)
        #all others should be easy enemies

        nodeList = [n1, n2, n3, n6, n7, n8, n11, n12, n13]
        for node in nodeList:
            if node.get_id() == playerStartLocation:
                print(node.get_id(), "start and current node")
                node.set_startingNode()
                node.set_currentNode()
                node.set_enemyType(0)
            if node.get_id() == endLocation:
                print(node.get_id(), "exit")
                node.set_exitLocation()
                node.set_enemyType(0)
            if node.get_id() == keyEnemyLocation: #working
                print(node.get_id(), "key enemy")
                node.set_holdsKey()
                node.set_enemyType(2)
            if node.get_id() == hardEnemy2: #working
                print(node.get_id(), "hard enemy")
                node.set_enemyType(2)
            if node.get_id() in centerList: #working
                print(node.get_id(), "easy enemy")
                node.set_enemyType(1)
            if node.get_id() == healLocation: #working
                print(node.get_id(), "heal station")
                node.set_healStation()
                node.set_enemyType(0)

        print("------------")
        print("Beginning Game Sequence")
        #initializing player health and that they dont have the key
        playerHealth = 60
        hasKey = False
        playerNode = Node(None)
        for node in nodeList: #finds which node the player is currently on
            if node.get_currentNode() == True:
                playerNode = node
                #playerNode = n3
        gameLayout = MyLayout()
        gameLayout.map = playerNode.get_id()

        move = 0


        def mainGame():
            if GameGUI.GameLogic.move < 15: #number of turns before the player loses, was thinking 15 for 
                
                for node in GameGUI.GameLogic.nodeList: #finds which node the player is currently on
                    if node.get_currentNode() == True:
                        GameGUI.GameLogic.playerNode = node
                        #playerNode = n3

                GameGUI.gameLayout.map = GameGUI.GameLogic.playerNode.get_id()
                print("The player is currently on node", GameGUI.GameLogic.playerNode.get_id())
                GameGUI.GameMove.speak("The player is currently on node" + str(GameGUI.GameLogic.playerNode.get_id()))
                
                #-----------------------------------------------------------------------------#
                #enemy fighting logic - COMPLETE
                if GameGUI.GameLogic.playerNode.get_enemyType() == "Easy" or GameGUI.GameLogic.playerNode.get_enemyType() == "Hard":
                    print("Enemy encountered, would you like to fight or run")
                    GameGUI.GameMove.speak("Enemy encountered, would you like to fight or run")
                    breakout = False
                    userInput = GameGUI.GameMove.listen() #will be voice based
                    #user enters their choice
                    invalidInput = True
                    while (invalidInput): 
                        if userInput == "run": 
                            invalidInput = False
                            num = random.randint(1, 4)
                            if num == 1:
                                print("You didnt escape successfully, you must fight")
                                GameGUI.GameMove.speak("You didnt escape successfully, you must fight")
                                userInput = "fight"
                                invalidInput = True
                            else: #teleporting case
                                print("Escaped successfully")
                                GameGUI.GameMove.speak("Escaped successfully")
                                teleportTo = random.choice(GameGUI.GameLogic.nodeList)
                                print("Teleported to node", teleportTo.get_id())
                                GameGUI.GameMove.speak("Teleported to node " + str(teleportTo.get_id()))
                                teleportTo.set_currentNode()
                                GameGUI.GameLogic.playerNode = teleportTo
                                

                        elif userInput == "fight":
                            GameGUI.gameLayout.enemyID = GameGUI.GameLogic.playerNode.get_enemyType()
                            GameGUI.gameLayout.enemy()
                            if GameGUI.GameLogic.playerNode.get_enemyType() == "Easy": #easy enemy case
                                invalidInput = False
                                print("This should be a breeze (easy enemy)")
                                GameGUI.GameMove.speak("This should be a breeze (easy enemy)")
                                GameGUI.GameMove.attack()
                                hurt = random.randint(5, 15)
                                GameGUI.GameLogic.playerHealth -= hurt
                                GameGUI.gameLayout.healthy = GameGUI.GameLogic.playerHealth
                                GameGUI.gameLayout.damage()
                                if GameGUI.GameLogic.playerNode.get_holdsKey() == True:
                                    print("you got a key!")
                                    GameGUI.gameLayout.key = True
                                    GameGUI.gameLayout.keyFound()
                                    GameGUI.GameMove.speak("you got a key!")
                                    GameGUI.GameLogic.hasKey = True
                                if GameGUI.GameLogic.playerHealth > 0:
                                    print("You survived with", GameGUI.GameLogic.playerHealth, "health!")
                                    GameGUI.GameMove.speak("You survived with " + str(GameGUI.GameLogic.playerHealth) + " health!")
                                    GameGUI.GameLogic.playerNode.set_enemyType(0)
                                else:
                                    print("You died, game over :(")
                                    GameGUI.gameLayout.dead()
                                    GameGUI.GameMove.speak("You died, game over :(")
                                    exit()
                            if GameGUI.GameLogic.playerNode.get_enemyType() == "Hard": #hard enemy case
                                invalidInput = False
                                print("Uh oh, he looks scary (hard enemy)")
                                GameGUI.GameMove.speak("Uh oh, he looks scary (hard enemy)")
                                GameGUI.GameMove.attack()
                                hurt = random.randint(10, 30)
                                GameGUI.GameLogic.playerHealth -= hurt
                                GameGUI.gameLayout.healthy = GameGUI.GameLogic.playerHealth
                                GameGUI.gameLayout.damage()
                                if GameGUI.GameLogic.playerNode.get_holdsKey() == True:
                                    print("you got a key!")
                                    GameGUI.gameLayout.key = True
                                    GameGUI.gameLayout.keyFound()
                                    GameGUI.GameMove.speak("you got a key!")
                                    GameGUI.GameLogic.hasKey = True
                                if GameGUI.GameLogic.playerHealth > 0:
                                    print("You survived with", GameGUI.GameLogic.playerHealth, "health!")
                                    GameGUI.GameMove.speak("You survived with " + str(GameGUI.GameLogic.playerHealth) + " health!")
                                    GameGUI.GameLogic.playerNode.set_enemyType(0)
                                else:
                                    print("You died, game over :(")
                                    GameGUI.gameLayout.dead()
                                    GameGUI.GameMove.speak("You died, game over :(")
                                    exit()
                    
                        else:
                            invalidInput = True
                            print("Enemy encountered, would you like to fight or run")
                            userInput = GameGUI.GameMove.listen() #will be voice based
                #-----------------------------------------------------------------------------#
                #heal station logic - COMPLETE        

                if GameGUI.GameLogic.playerNode.get_healStation() == True:
                    print("Youve encountered a heal station! Healing you now.")
                    GameGUI.gameLayout.healing()
                    GameGUI.GameMove.speak("Youve encountered a heal station! Healing you now.")
                    GameGUI.GameLogic.playerHealth = 60
                    print("Current health:", GameGUI.GameLogic.playerHealth)
                    GameGUI.GameMove.speak("Current health: " + str(GameGUI.GameLogic.playerHealth))

                #-----------------------------------------------------------------------------#
                #endgame logic - COMPLETE
                    
                if GameGUI.GameLogic.playerNode.get_exitLocation() == True:
                    if GameGUI.GameLogic.hasKey == True:
                        print("Youve escaped! You win!")
                        GameGUI.GameMove.speak("Youve escaped! You win!")
                        exit()
                    else:
                        print("Youve found the exit but don't have the key! Go find it!")
                        GameGUI.GameMove.speak("Youve found the exit but don't have the key! Go find it!")
                    
                #-----------------------------------------------------------------------------#
                #movement logic - NEEDS WORK
                validDirections = list(GameGUI.GameLogic.playerNode.get_cardinals())
                validNodes = list(GameGUI.GameLogic.playerNode.get_connections())
                # print("I see a path to the: ")
                # for i in range(len(validDirections)):
                #     print(validDirections[i] + str(validNodes[i].get_id()))
                # print("Which direction would you like to go in?")
                GameGUI.gameLayout.map = GameGUI.GameLogic.playerNode.get_id()
                GameGUI.gameLayout.location()
                GameGUI.GameLogic.playerNode.remove_currentNode()

                userInput = GameGUI.GameMove.changeDirection(GameGUI.GameLogic.playerNode.curLookCard, validDirections).capitalize()
                
                # userInput = validDirections[0] # Test the first choice

                print(userInput) # print
                # print("Going to " + str(validNodes[validDirections.index(userInput)].get_id())) # use validNodes[validDirections.index(userInput)].get_id() to get the node id/node key
                GameGUI.GameLogic.playerNode = validNodes[validDirections.index(userInput)]
                GameGUI.gameLayout.map = GameGUI.GameLogic.playerNode.get_id()
                GameGUI.gameLayout.location()
                GameGUI.GameLogic.playerNode.set_currentNode()
                GameGUI.GameLogic.playerNode.curLookCard = userInput
                # print("Looking " + playerNode.curLookCard)
                #gets user input via voice
                #we need to move the node to in the direction the user says
                #this should be the last thing needed for the logic
                #we also need to add voice output to it as well
                GameGUI.GameLogic.move += 1
                GameGUI.GameLogic.mainGame()
            else:
                #robot should say something before it closes the program
                print("player has lost....took too many moves")
                GameGUI.GameMove.speak("player has lost....took too many moves")
                #exit()
    
    

class MyApp(App):


    gamegui = GameGUI()
    def build(self):
        #Window.fullscreen = True
        Window.clearcolor = (1,1,1,1)
        Window.size = (800,480)
        Window.top = 10
        Window.left = 50
        MyApp.gamegui.GameLogic.mainGame()
        return MyApp.gamegui

if __name__ == '__main__':
    gameapp = MyApp()
    gameapp.run()