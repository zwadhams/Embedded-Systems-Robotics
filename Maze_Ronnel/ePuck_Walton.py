# Created by Ronnel Walton (02/12/2022)
# Project 1 Maze

# Libraries
from cProfile import run
from operator import ne
from controller import Robot
import pathlib, os, sys
import math


# Class to group each maze instance (Only one was initialized for project 1)
class mazeMap:
    def __init__(self):
        self.maze_graph = self.Graph()
        return
    # Class for each Node/Split for Maze exploration
    class Node:
        def __init__(self, key):
            self.id = key
            self.coordinates = [0, 0]
            self.connected_to = {}
            self.distance = sys.maxsize
            self.visited = False
            self.previous = None
            
        # distance plus cardinal direction referenced from current node
        def add_adjacent(self, adjacent, distance, cardinal):   
            if (adjacent not in self.connected_to):
                self.connected_to[adjacent] = [distance, cardinal]
                
        # list out all the nodes connected from the current node
        def get_connections(self):
            return self.connected_to.keys()
        
        # get the id of the node
        def get_id(self):
            return self.id
        
        # set the distance of the node to other nodes for dijsktra algorithm
        def set_distance(self, dist):
            self.distance = dist
        
        # get the distance from the current node to the requested adjacent node 
        def get_distance(self, adjacent):
            return self.connected_to[adjacent][0]
        
        # set the previous node of the current node for dijsktra algorithm
        def set_previous(self, prev):
            self.previous = prev
        
        # set the node as explored for dijsktra algorithm
        def set_visited(self):
            self.visited = True
            
        # print node with its adjacent node, distances and cardinal direction referenced from current node
        def __str__(self):
            return str(self.id) + ' adjacent: ' + str([(x.id, self.connected_to[x.id][0], self.connected_to[x.id][1]) for x in self.connected_to])  

        pass
    
    # Class to keep track of all Nodes/Split in Maze exploration
    class Graph:
        
        def __init__(self):
            self.map_list = {}
            self.total_nodes = 0
            
        # Add a node/split to the map
        def add_node(self, key):
            self.total_nodes += 1
            new_node = mazeMap.Node(key)
            self.map_list[key] = new_node
            return new_node
        
        # Retrieve a node using the id
        def get_node(self, n):
            if n in self.map_list:
                return self.map_list[n]
            else:
                return None
            
        # Add information how to get between nodes/split
        def add_path(self, fromN, toN, distance=0, cardinal = "North", x = 0, y = 0):
            if fromN not in self.map_list:
                self.add_node(fromN)
            if toN not in self.map_list:
                self.add_node(toN)
            self.map_list[fromN].add_adjacent(toN, distance, cardinal)
            self.map_list[toN].coordinates[0] = x
            self.map_list[toN].coordinates[1] = y
            rev_angle =  self.bearing2angle(cardinal) + 180
            rev_cardinal = self.deg2bearing((rev_angle)%360)
            self.map_list[toN].add_adjacent(fromN, distance, rev_cardinal)

        # Retrieve nodes from the map list
        def get_adjacents(self):
            return self.map_list.keys()
        
        # Set the coordinates for each nodes
        def set_coordinate(self, id, x, y):
            self.map_list[id].coordinates = [x, y]
            
        # degree to bearing conversion
        def deg2bearing(self, deg):
            self.angleWidth = (360/16)
            cardinal = None
            if ((315 - self.angleWidth) < deg) & ((315 + self.angleWidth) > deg):
                cardinal = "North-West"
            elif ((270 - self.angleWidth) <= deg) & ((270 + self.angleWidth) >= deg):
                cardinal = "West"
            elif (((225 - self.angleWidth) < deg) & ((225 + self.angleWidth) > deg)):
                cardinal = "South-West"
            elif ((180 - self.angleWidth) <= deg) & ((180 + self.angleWidth) >= deg):
                cardinal = "South"
            elif ((135 - self.angleWidth) < deg) & ((135 + self.angleWidth) > deg):
                cardinal = "South-East"
            elif ((90 - self.angleWidth) <= deg) & ((90 + self.angleWidth) >= deg):
                cardinal = "East"
            elif ((45 - self.angleWidth) < deg) & ((45 + self.angleWidth) > deg):
                cardinal = "North-East"
            elif ((360 - self.angleWidth) <= deg) | ((0 + self.angleWidth) >= deg):
                cardinal = "North"
            return cardinal
        
        # bearing to degree conversion
        def bearing2angle(self, cardinal):
            bearing = ["North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"]            
            if (bearing.index(cardinal)*45) == 0:
                return 0
            return bearing.index(cardinal)*45
    
        # check if the node already exist
        def check_exist(self, x, y):
            coordinates_margin = 3
            for key in self.map_list.keys():
                targetN = self.map_list[key]
                cmp_x = targetN.coordinates[0]
                cmp_y = targetN.coordinates[1]
                upper_x = (x + coordinates_margin)
                lower_x = (x - coordinates_margin)
                upper_y = (y + coordinates_margin)
                lower_y = (y - coordinates_margin)
                if ((upper_x > cmp_x) & (lower_x < cmp_x) & (upper_y > cmp_y) & (lower_y < cmp_y)):
                    # print('Check ')
                    return key
            return None
        
        # iter function
        def __iter__(self):
            return iter(self.map_list.values())
        
        pass
    
    # shortest algorithm for finding from and to destination
    def shortest(self, target, path = None): # Set the target
        if path == None:
            path = [target]
        target_node = self.maze_graph.get_node(target)
        
        if target_node.previous:
            path.append(target_node.previous.get_id())
            self.shortest(target_node.previous.get_id(), path)
        
        return path[::-1]
    
    def dijsktra(self, initial): # Set the starting point
        start = self.maze_graph.get_node(initial)
        start.set_distance(0)
        
        unvisited_queue = [(self.maze_graph.get_node(n).distance, n) for n in self.maze_graph.map_list]
        unvisited_queue = sorted(unvisited_queue, key = lambda x: x[0])
        while len(unvisited_queue):
            exploring_nodes = unvisited_queue.pop(0)
            current = self.maze_graph.get_node(exploring_nodes[1])
            current.set_visited()
            
            for next in current.connected_to:
                if self.maze_graph.get_node(next).visited:
                    continue
                new_dist = current.distance + current.get_distance(next)
                if new_dist < self.maze_graph.get_node(next).distance:
                    self.maze_graph.get_node(next).set_distance(new_dist)
                    self.maze_graph.get_node(next).set_previous(current)
                else:
                    pass
                
            unvisited_queue = [(self.maze_graph.get_node(n).distance, n) for n in self.maze_graph.map_list if not self.maze_graph.get_node(n).visited]
            unvisited_queue = sorted(unvisited_queue, key = lambda x: x[0])
        pass

class epuck_webot:
    # Constants (Some are based of Assignment constraints)
    TIME_STEP = 64
    MAX_TURNSPEED = 3.2
    MAX_SPEED = 6.28
    DIFF_SPEED = 1.3
    MARGIN_DIST = 10
    
    # Initialize ePuck bot
    def __init__(self, motorPos, maxMotorSpeed, distThrehold):
        # compensate distance travelled based on the number of turns. constant found through how much wheel travels per 90 degree turns
        self.rTurn_Comp = 0
        self.lTurn_Comp = 0
        self.total_dist_travelled = 0
        
        self.dist_stamp = 0
        self.distThrehold = distThrehold
        self.epuck = self.robot()
        self._robot = self.epuck.robot
        self.maxSpeed = maxMotorSpeed
        self.current_cardinal = None
        self.angle = 1.57
        self.epuck.add_device("LMotor", "left wheel motor")
        self.epuck.add_device("RMotor", "right wheel motor")
        self.epuck.add_device("LEncoder", "left wheel sensor")
        self.epuck.add_device("REncoder", "right wheel sensor")
        self.epuck.add_device("Compass", "compass")
        self.epuck.add_device("Trophy Sensor", "floor_touch")
        self.leftMotor = self.epuck.get_device("LMotor")
        self.rightMotor = self.epuck.get_device("RMotor")
        self.leftEncoder = self.epuck.get_device("LEncoder")
        self.rightEncoder = self.epuck.get_device("REncoder")
        self.init_sensor()
        self.init_motor(motorPos)
        return
    
    # initialize distance sensors
    def init_sensor(self):
        sensorPos = ['front_right', 'front_mid_right', 'right', 'back_right', 'back_left', 'left', 'front_mid_left', 'front_left']
        sensorNames = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']
        for i in range(8):
            self.epuck.add_device(sensorPos[i], sensorNames[i])
        return
    
    # initialize motors
    def init_motor(self, motorPos):
        self.leftMotor.setPosition(motorPos)
        self.rightMotor.setPosition(motorPos)
        self.leftMotor.setVelocity(0)
        self.rightMotor.setVelocity(0)
        return
    
    # set motor speed
    def set_motor_speed(self, motor, speed):
        self.epuck.get_device(motor).setVelocity(speed)
    
    # set_distance travelled
    def set_distance_travelled(self):
        self.total_dist_travelled = self.rightEncoder.getValue() - self.rTurn_Comp
    # set reference point for travelled distance
    def distance_stamp(self):
        self.dist_stamp = self.rightEncoder.getValue() - self.rTurn_Comp
    # get distance travelled based on reference point
    def get_distance_travelled(self):
        self.set_distance_travelled()
        if (self.total_dist_travelled - self.dist_stamp) < 0:
            return 0
        return self.total_dist_travelled - self.dist_stamp
    
    # steer right
    def steer_right(self):
        self.leftMotor.setVelocity(self.MAX_TURNSPEED)
        self.rightMotor.setVelocity(self.MAX_TURNSPEED - self.DIFF_SPEED)
        self.angle = self.get_angle()
        return self.angle
    
    # steer left
    def steer_left(self):
        self.leftMotor.setVelocity(self.MAX_TURNSPEED - self.DIFF_SPEED)
        self.rightMotor.setVelocity(self.MAX_TURNSPEED)
        self.angle = self.get_angle()
        return self.angle
    
    # spin left
    def spin_left(self,ratio):
        if (ratio <= 1):
            self.leftMotor.setVelocity(-(ratio*self.MAX_TURNSPEED))
            self.rightMotor.setVelocity((ratio*self.MAX_TURNSPEED))
        else:
            self.leftMotor.setVelocity(-self.MAX_TURNSPEED)
            self.rightMotor.setVelocity(self.MAX_TURNSPEED)
        self.angle = self.get_angle()
        return self.angle

    # spin right
    def spin_right(self, ratio):
        if (ratio <= 1):
            self.leftMotor.setVelocity(ratio*self.MAX_TURNSPEED)
            self.rightMotor.setVelocity(-(ratio*self.MAX_TURNSPEED))
        else:
            self.leftMotor.setVelocity(self.MAX_TURNSPEED)
            self.rightMotor.setVelocity(-self.MAX_TURNSPEED)
        self.angle = self.get_angle()
        return self.angle

    # spin the robot to an angle the near turn (right or left)
    def shortest_angle(self, angle):
        cmp_0 = abs(self.angle - angle)
        cmp_360 = 360 - cmp_0
        if (cmp_0 <= cmp_360):
            return cmp_0
        else:
            return cmp_360

    # get closest turn from current to the target cardinal
    def get_closest_turn(self, cardinal):
        angle = self.bearing2angle(cardinal)
        fix_angle = self.bearing2angle(self.deg2bearing(self.get_angle()))
        if (angle == 0):
            angle = 360
        clockwise = angle - fix_angle
        cclockwise = angle - (fix_angle + 360)
        if abs(clockwise) <= abs(cclockwise):
            return clockwise
        else:
            return cclockwise

    # get closest turn from current to the target cardinal
    def spin_compass(self, cardinal):
        turn = self.get_closest_turn(cardinal)
        self.closest_turn_angle(turn)
        
    # spin the ePuck to the target angle
    def closest_turn_angle(self, angle):
        cur_R_dist = self.rightEncoder.getValue()
        cur_L_dist = self.leftEncoder.getValue()
        self.margin_angle = 0.6
        min_speed = 0.1
        min_ratio = 0.03
        adjust_ratio = 0.025
        self.get_angle()
        target_angle = 0
        if (angle > 0):
            target_angle = self.angle + angle
            if (target_angle > 360):
                target_angle -= 360
        else:
            target_angle = self.angle - abs(angle)
            if (target_angle < 0):
                target_angle = 360 - abs(target_angle)
        target_angle = self.bearing2angle(self.deg2bearing(target_angle))
        which_turn = "R"
        cur_ratio = 1
        if (angle < 0):
            which_turn = "L"
        if (which_turn == 'R'):
            self.spin_right(cur_ratio)
        else:
            self.spin_left(cur_ratio)
        cur_angle = self.shortest_angle(target_angle)
        cmp_angle = self.shortest_angle(target_angle)
        prev_angle = cur_angle
        # keep turning
        while (self.margin_angle <= cur_angle) & (self._robot.step(self.TIME_STEP) != -1):
            cur_angle = self.shortest_angle(target_angle)
            cur_speed = (self.MAX_SPEED*((cur_angle/cmp_angle)*(cur_angle/cmp_angle)))
            if (cur_speed < min_speed):
                cur_ratio = min_ratio
            else:
                cur_ratio = 1
            if (cur_angle < self.margin_angle):
                self.stop()
            if (prev_angle < cur_angle):
                if (which_turn == 'R'):
                    self.spin_left(adjust_ratio)
                else:
                    self.spin_right(adjust_ratio)
            # adjust when over turning
            else:
                if (which_turn == 'R'):
                    self.spin_right(cur_ratio)
                else:
                    self.spin_left(cur_ratio)
            prev_angle = cur_angle
        # compensate turns
        self.lTurn_Comp += (self.leftEncoder.getValue() - cur_L_dist)
        self.rTurn_Comp += (self.rightEncoder.getValue() - cur_R_dist)

    # move forward approximately to target distance
    def forward_to(self, dist):
        self.forward()
        stamp_stop = self.get_distance_travelled() + dist
        upper_stop = stamp_stop + 1
        lower_stop = stamp_stop
        while ~((self.get_distance_travelled() > lower_stop) & (self.get_distance_travelled() < upper_stop)) & (self._robot.step(self.TIME_STEP) != -1):
            self.forward()
            if (self.check_trophy()):
                break
        
    # move forward
    def forward(self):
        self.leftMotor.setVelocity(self.MAX_SPEED)
        self.rightMotor.setVelocity(self.MAX_SPEED)
        return
    
    # stop
    def stop(self):
        self.leftMotor.setVelocity(0)
        self.rightMotor.setVelocity(0)

    # backward
    def backward(self):
        self.leftMotor.setVelocity(-self.MAX_SPEED)
        self.rightMotor.setVelocity(-self.MAX_SPEED)
        return
    
    # retrieve distance sensor
    def get_sensor(self, sensor):
        return self.epuck.get_device(sensor)
    
    # check if the distance sensor detects something
    def check_sensor(self, sensor):
        return self.epuck.get_device(sensor).getValue() > self.distThrehold
    
    # retrieve current bearing
    def check_compass(self):
        self.get_angle()
        return self.deg2bearing(self.angle)
    
    # convert angle to bearing
    def deg2bearing(self, deg):
        self.angleWidth = (360/16)
        cardinal = None
        if ((315 - self.angleWidth) < deg) & ((315 + self.angleWidth) > deg):
            cardinal = "North-West"
        elif ((270 - self.angleWidth) <= deg) & ((270 + self.angleWidth) >= deg):
            cardinal = "West"
        elif (((225 - self.angleWidth) < deg) & ((225 + self.angleWidth) > deg)):
            cardinal = "South-West"
        elif ((180 - self.angleWidth) <= deg) & ((180 + self.angleWidth) >= deg):
            cardinal = "South"
        elif ((135 - self.angleWidth) < deg) & ((135 + self.angleWidth) > deg):
            cardinal = "South-East"
        elif ((90 - self.angleWidth) <= deg) & ((90 + self.angleWidth) >= deg):
            cardinal = "East"
        elif ((45 - self.angleWidth) < deg) & ((45 + self.angleWidth) > deg):
            cardinal = "North-East"
        elif ((360 - self.angleWidth) <= deg) | ((0 + self.angleWidth) >= deg):
            cardinal = "North"
        return cardinal
    
    # convert bearing to angle
    def bearing2angle(self, cardinal):
        bearing = ["North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"]            
        if (bearing.index(cardinal)*45) == 0:
            return 0
        return bearing.index(cardinal)*45
    
    # retrieve current angle
    def get_angle(self):
        ret_values = self.epuck.get_device('Compass').getValues()
        if not math.isnan(ret_values[0]):
            self.angle = (((math.atan2(ret_values[0], ret_values[1])) - 1.5708) / math.pi * 180.0)
            if (self.angle < 0):
                self.angle = abs(self.angle)
            else:
                self.angle = 360 - abs(self.angle)
        return self.angle
    
    # Check if the trophy is found
    def check_trophy(self):
        if self.epuck.get_device("Trophy Sensor").getValue() != 1:
            return 0
        return 1
    
    # check the total distance travelled
    def check_distance_travelled(self):
        return self.total_dist_travelled
    
    # class for general robot
    class robot:
        def __init__(self):
            self.robot = Robot()
            self.devices = {}
            return
        
        def add_device(self, id, device_name):
            self.devices[id] = self.robot.getDevice(device_name)
            if callable(getattr(self.devices[id], "enable", None)):
                self.devices[id].enable(epuck_webot.TIME_STEP)
            return
        
        def get_device(self, id):
            return self.devices[id]
        
        def get_devices(self):
            return self.devices.keys()
        pass
    pass

# read/check map files
script_loc = pathlib.Path(__file__).parent
map_data_loc = os.path.join(script_loc, 'map_data.txt')
run_state = 0
mapf = None

# Map Coordinates
maze = mazeMap()
maze_obj = maze.maze_graph

# global variables
init_wall = False
trophy_found = False
threshold = 300
cornerDist = 0
pass_unknown_node = 0
unknown_node = 0
pass_unknown_node = 0
corner_found = False
trophy_node = None

# Check the current run number
if (not os.path.exists(map_data_loc)):
    run_state = 1

else: # Set the header for map file
    mapf = open(map_data_loc, "r")
    fileHead = mapf.readline()
    if ('run 1 complete' in fileHead):
        run_state = 2
    elif ('run 2 complete' in fileHead):
        run_state = 3

# reading map file
if ((run_state == 2) | (run_state == 3)):
    vertex_head = mapf.readline()
    
    if ('Nodes' in vertex_head):
        file_line = mapf.readline()
        while (not 'Paths' in file_line):
            node_in = file_line.strip()
            maze_obj.add_node(node_in)
            # print(node_in)
            file_line = mapf.readline()
        if ('Paths' in file_line):
            file_line = mapf.readline()
            while (file_line):
                if ("trophy" in file_line):
                    trophy_in = file_line.strip().split(' ')
                    trophy_node = trophy_in[2]
                else:
                    edge_in = file_line.split(',')
                    maze_obj.add_path(edge_in[0], edge_in[1], float(edge_in[2]), str(edge_in[3]), float(edge_in[4]), float(edge_in[5]))
                file_line = mapf.readline()

# close map file
if (os.path.exists(map_data_loc)):
    mapf.close()




# create the Robot instance.
print("Starting")
epuck = epuck_webot(float('inf'), 6.2, threshold)

x = 0
y = 0

if (run_state == 1):
    maze_obj.add_node("N0")

prevNode = "N0"
x = 0
y = 0
    
    
shortest_cardinal = []
shortest_distance = []
    
# State current Run number
if (run_state == 1):
    #right wall algo
    print("Right Wall")
elif (run_state == 2):
    #left wall algo
    print("Left Wall")
    
elif (run_state == 3): # find the shortest path before moving
    print("Shortest Path")
    maze.dijsktra(initial = 'N0')
    sp = maze.shortest(target = trophy_node)
    for i in range(len(sp)):
        if (i+1) < len(sp):
            cur = maze_obj.get_node(sp[i]).connected_to[sp[i+1]]
            shortest_cardinal.append(cur[1])
            shortest_distance.append(cur[0])
    
epuck.DIFF_SPEED += 2.2
cur_heading = "North"
distanceTravelled = 0
trophy_found = epuck.check_trophy()

# run_state = 4

stepF = 0
clear_init = 0
# remove any previous sensor data
while ~clear_init & (epuck._robot.step(epuck.TIME_STEP) != -1):
    clear_init = 1
# Start maze exploration
while (epuck._robot.step(epuck.TIME_STEP) != -1):
    direction = ["North", "South", "East", "West"]
    cur_front_right_val = epuck.get_sensor('front_right').getValue() * 10
    cur_front_mid_right_val = epuck.get_sensor('front_mid_right').getValue() * 10
    cur_right_val = epuck.get_sensor('right').getValue() * 10
    cur_back_right_val = epuck.get_sensor('back_right').getValue() * 10
    cur_cardinal_val = epuck.check_compass()
    cur_compass_deg = epuck.get_angle()
    trophy_found = epuck.check_trophy()
    epuck.stop()
    # Trophy found? in run 1/run 2
    if ~((epuck.get_sensor("front_right").getValue() > 110) & (epuck.get_sensor("front_left").getValue() > 110)) & trophy_found:
        diffTravel = epuck.get_distance_travelled()
        newNode = "N{}".format(maze_obj.total_nodes)
        if (trophy_node == None):
            trophy_node = newNode
        if ("North" == cur_heading):
            y += diffTravel
        elif "South" == cur_heading:
            y -= diffTravel
        elif "East" == cur_heading:
            x += diffTravel
        elif "West" == cur_heading:
            x -= diffTravel
        maze_obj.add_path(prevNode, newNode, diffTravel, cur_heading, x, y)
        epuck.distance_stamp()
        print('Win')
        
        break
    
    # Run 1 right hand rule
    if (run_state == 1):
        if (epuck.get_sensor("front_right").getValue() > 150) & (epuck.get_sensor("front_left").getValue() > 150):
            epuck.closest_turn_angle(-90)
        elif (epuck.get_sensor("front_mid_right").getValue() < 110) & (epuck.get_sensor("right").getValue() < 110):
            epuck.forward()
            stop = epuck.get_distance_travelled() + 2.3
            while (stop > epuck.get_distance_travelled()) & (epuck._robot.step(epuck.TIME_STEP) != -1):
                epuck.forward()
            epuck.closest_turn_angle(90)
            while (epuck.get_sensor("right").getValue() < 110) & (epuck._robot.step(epuck.TIME_STEP) != -1):
                epuck.forward()
        else:
            epuck.forward()
            
    # Run 2 Left hand rule
    elif (run_state == 2):
        if (epuck.get_sensor("front_right").getValue() > 150) & (epuck.get_sensor("front_left").getValue() > 150):
            epuck.closest_turn_angle(90)
        elif (epuck.get_sensor("front_mid_left").getValue() < 110) & (epuck.get_sensor("left").getValue() < 110):
            epuck.forward()
            stop = epuck.get_distance_travelled() + 2.3
            while (stop > epuck.get_distance_travelled()) & (epuck._robot.step(epuck.TIME_STEP) != -1):
                epuck.forward()
            epuck.closest_turn_angle(-90)
            while (epuck.get_sensor("left").getValue() < 110) & (epuck._robot.step(epuck.TIME_STEP) != -1):
                epuck.forward()
        else:
            epuck.forward()
        
    # Shortest Path 
    elif (run_state == 3):
        for i in range(len(shortest_cardinal)):
            if (epuck.deg2bearing(epuck.get_angle()) != shortest_cardinal[i]):
                epuck.spin_compass(shortest_cardinal[i])
            print(shortest_cardinal[i], " ", shortest_distance[i])
            epuck.forward_to(shortest_distance[i])
            left = epuck.get_sensor("left").getValue()
            right = epuck.get_sensor("right").getValue()
            if ((i+1) < len(shortest_cardinal)):
                if (shortest_cardinal[i] != shortest_cardinal[i+1]):
                    while((right > 66) & (left > 66)) & (epuck._robot.step(epuck.TIME_STEP) != -1):
                        left = epuck.get_sensor("left").getValue()
                        right = epuck.get_sensor("right").getValue()
                        epuck.forward()
            stop = epuck.get_distance_travelled() + 1.5
            while (stop > epuck.get_distance_travelled()) & (epuck._robot.step(epuck.TIME_STEP) != -1):
                epuck.forward()
            if (epuck.check_trophy() & ((len(shortest_cardinal)-1)==i)):
                print("Win")
                break
        break
    
    elif (run_state == 4):
        epuck.closest_turn_angle(90)
        print(epuck.leftEncoder.getValue(), " ", epuck.rightEncoder.getValue())
        epuck.closest_turn_angle(90)
        print(epuck.leftEncoder.getValue(), " ", epuck.rightEncoder.getValue())
        epuck.closest_turn_angle(90)
        print(epuck.leftEncoder.getValue(), " ", epuck.rightEncoder.getValue())
        epuck.closest_turn_angle(90)
        print(epuck.leftEncoder.getValue(), " ", epuck.rightEncoder.getValue())
        break
    
    # Gathering any map data
    # Nodes being explored
    compass_heading = epuck.check_compass()
    if (((run_state == 2) | (run_state == 1))&(compass_heading in direction) & (cur_heading != compass_heading) & (compass_heading != None)):
        diffTravel = epuck.get_distance_travelled()
        newNode = "N{}".format(maze_obj.total_nodes)
        if ("North" == cur_heading):
            y += diffTravel
        elif "South" == cur_heading:
            y -= diffTravel
        elif "East" == cur_heading:
            x += diffTravel
        elif "West" == cur_heading:
            x -= diffTravel
            
        
        if (diffTravel > 1):
            check_Node = maze_obj.check_exist(x, y)
            if (check_Node != None):
                maze_obj.add_path(prevNode, check_Node, diffTravel, cur_heading, x, y)
                prevNode = check_Node
            else:
                maze_obj.add_path(prevNode, newNode, diffTravel, cur_heading, x, y)
                prevNode = newNode

        epuck.distance_stamp()
        cur_heading = compass_heading
        
    # Any nodes unexplored during any other runs
    elif (((run_state == 2) | (run_state == 1)) & ((epuck.get_sensor("left").getValue() < 110) | (epuck.get_sensor("right").getValue() < 110)) & ~corner_found & (epuck.get_distance_travelled() > 3)):
        corner_found = True
        cornerDist = epuck.get_distance_travelled()
        
    if corner_found & ((epuck.get_sensor("left").getValue() > 110) & (epuck.get_sensor("right").getValue() > 110)):
        corner_end = epuck.get_distance_travelled()
        unknown_corner_dist = ((corner_end - cornerDist)/2) + cornerDist
        newNode = "N{}".format(maze_obj.total_nodes)
        if ("North" == cur_heading):
            y += unknown_corner_dist
        elif "South" == cur_heading:
            y -= unknown_corner_dist
        elif "East" == cur_heading:
            x += unknown_corner_dist
        elif "West" == cur_heading:
            x -= unknown_corner_dist
        check_Node = maze_obj.check_exist(x, y)
        if (check_Node != None):
            maze_obj.add_path(prevNode, check_Node, unknown_corner_dist, cur_heading, x, y)
            prevNode = check_Node
        else:
            maze_obj.add_path(prevNode, newNode, unknown_corner_dist, cur_heading, x, y)
            prevNode = newNode
        epuck.distance_stamp()
        cur_heading = compass_heading
        corner_found = False
        

        
    
# Enter here exit cleanup code.

if (os.path.exists(map_data_loc)):
    mapf.close()
    os.remove(map_data_loc)
        
if (not os.path.exists(map_data_loc)):
    mapf = open(map_data_loc, "w+")

# Writing Map data
mapf.write("run {} complete\n".format(run_state))
mapf.write("Nodes\n")
for write_node in maze_obj.map_list.keys():
    mapf.write(write_node+"\n")
mapf.write("Paths\n")
for write_node in maze_obj.map_list.keys():
    node_connection = maze_obj.get_node(write_node).get_connections()
    for write_edges in node_connection:
        write_distance = maze_obj.get_node(write_node).connected_to[write_edges]
        write_x = str(maze_obj.get_node(write_edges).coordinates[0] )
        write_y = str(maze_obj.get_node(write_edges).coordinates[1] )
        mapf.write("{},{},{},{},{},{}\n".format(str(write_node),str(write_edges),str(write_distance[0]), str(write_distance[1]),write_x,write_y))
mapf.write("trophy at {}\n".format(trophy_node))
mapf.close()
if ((run_state == 3) & os.path.exists(map_data_loc)):
    os.remove(map_data_loc)