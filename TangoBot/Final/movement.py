import math
import pathlib, os, sys
import random

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

    def set_visited(self): #maks this node as visited
        self.visited = True

    def set_previous(self): #marks the previous node 
        self.previous = prev

    def addEnemyType(self, enemyType): #0 is none, 1 is easy, 2 is hard
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
        print(node.get_id(), " start")
        node.set_startingNode()
    if node.get_id() == endLocation:
        print(node.get_id(), " exit")
        node.set_exitLocation() == True
    if node.get_id() == keyEnemyLocation: #working
        print(node.get_id(), " key enemy")
        node.set_holdsKey == True
        node.addEnemyType(2)
    if node.get_id() == hardEnemy2: #working
        print(node.get_id(), " hard enemy")
        node.addEnemyType(2)
    if node.get_id() in centerList: #working
        print(node.get_id(), "easy enemy")
        node.addEnemyType(1)
    if node.get_id() == healLocation: #working
        print(node.get_id(), "heal station")
        node.set_healStation()
    
