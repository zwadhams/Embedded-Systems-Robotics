from controller import Robot, Motor

TIME_STEP = 64

# create the Robot instance.
robot = Robot()
print("Starting")

# get the motor devices
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
# set the target position of the motors
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
rightMotor.setVelocity(.1)
leftMotor.setVelocity(-.1)
compass = robot.getDevice("compass")
compass.enable(TIME_STEP)
touchSensor = robot.getDevice("touch sensor") #enables touch sensor
touchSensor.enable(TIME_STEP)
leftE = robot.getDevice("left wheel sensor")
leftE.enable(TIME_STEP)

ps = []
psNames = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']

for i in range(8):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(TIME_STEP)

def rotateRight():
    print("Right")
    answer = compass.getValues()
    degree = ((math.atan2(ret_values[0], ret_values[1])) - 1.5708) / math.pi * 180.0
    print("Answer")
    print(answer)
    print("Angle")
    print(angle)
    if angle < .77 and angle > -.82:
        print("West")
        while (angle != 0.00000101961154714703327):
            rightMotor.setVelocity(-5)
            leftMotor.setVelocity(5)
    elif angle < -0.82 and angle > -2.4:
        print("North")
        while (angle != 0.00000101961154714703327):
            rightMotor.setVelocity(-5)
            leftMotor.setVelocity(5)
    elif angle < -2.41 or angle > 2.44 :
        print("East")
        while (angle != 0.00000101961154714703327):
            rightMotor.setVelocity(-5)
            leftMotor.setVelocity(5)
    else:
        print("South")
        while (angle != 0.00000101961154714703327):
            rightMotor.setVelocity(-5)
            leftMotor.setVelocity(5)

while robot.step(TIME_STEP) != -1:
    answer = compass.getValues()
    psValues = []
    testRun = 1;
    import math

    #Right following function
    #--------------------------#
    if (testRun == 1):
        pass
    
    if not math.isnan(answer[0]):
        #print(answer)
        #angle = (math.atan2(answer[0], answer[1]))
        degree = (((math.atan2(answer[0], answer[1])) - 1.5708) / math.pi * 180.0)+270
        #print(angle)
        print(degree)
        if degree < 45 :
            #rotateRight()
            print("West")
        elif degree > 315 :
            print("West")
        elif degree < 315.0 and degree > 225.0:
            print("North")
        elif degree < 225.0 or degree > 135 :
            print("East")
        elif degree < 135 and degree > 45 :
            print("South")
        else:
            print("unknown")
        
        #if angle < .77 and angle > -.82:
            #rotateRight()
        #    print("West")
        #elif angle < -0.82 and angle > -2.4:
        #    print("North")
        #elif angle < -2.41 or angle > 2.44 :
        #    print("East")
        #else:
        #    print("South")
        
    else:
        print("Not")

    #print(leftE.getValue())
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.


        


