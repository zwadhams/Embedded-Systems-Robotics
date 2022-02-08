from controller import Robot, Motor

TIME_STEP = 64

robot = Robot()
print("Starting")

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.5)
rightMotor.setVelocity(0.0)
compas = robot.getDevice("compass")
compass.enable(TIME_STEP)

while robot.step(TIME_STEP) != -1;
    answer = compass.getValues()

    import math
    if not math.isnan(answer[0]):
        print(answer)

        angle = (math.atan2(answer[0], answer[1]))
        print(angle)
        if angle < .77 and angle > -0.82:
            print("West")
        elif angle < -0.82 and angle > -2.4:
            print("North")
        elif angle < -2.41 or angle > -2.4:
            print("East")
        else:
            print("South")
    else:
        print("Not")
