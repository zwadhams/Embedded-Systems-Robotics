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
leftMotor.setVelocity(.1)
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

def rotateRight(degree):
    print("Right")
    if degree < 45 :
        while (degree != 0):
            rightMotor.setVelocity(-1)
            leftMotor.setVelocity(1)
        print("West")
    elif degree > 315 :
        while (degree != 270):
            rightMotor.setVelocity(-1)
            leftMotor.setVelocity(1)
        print("West")
    elif degree < 315.0 and degree > 225.0:
        while (degree != 180):
            rightMotor.setVelocity(-1)
            leftMotor.setVelocity(1)
        print("North")
    elif degree < 225.0 or degree > 135 :
        while (degree != 90):
            rightMotor.setVelocity(-1)
            leftMotor.setVelocity(1)
        print("East")
    elif degree < 135 and degree > 45 :
        while (degree != 0):
            rightMotor.setVelocity(-1)
            leftMotor.setVelocity(1)
        print("South")
    else:
        print("unknown")
    while (degree != 0.00000101961154714703327):
        rightMotor.setVelocity(-1)
        leftMotor.setVelocity(1)

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
        degree = (((math.atan2(answer[0], answer[1])) - 1.5708) / math.pi * 180.0)+270
        print(degree)
        if degree < 45 :
            rotateRight(degree)
            print("W")
        elif degree > 315 :
            print("W")
        elif degree < 315.0 and degree > 225.0:
            rotateRight(degree)
            print("N")
        elif degree < 225.0 or degree > 135 :
            print("E")
        elif degree < 135 and degree > 45 :
            print("S")
        else:
            print("unknown")
        
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


        


