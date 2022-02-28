class Tango_Controller:
    RESOLUTION = 4000
    MID_POSITION = 6000
    SERVO_STEP = 5
    SERVO_STEP_MAX = MID_POSITION + ((RESOLUTION/2))
    SERVO_STEP_MIN = MID_POSITION - ((RESOLUTION/2))
    MODE = "S" # S for Single Target, M for Multiple Target
    DEFAULT_VALUES = {"Waist": MID_POSITION, "Neck_Pan": MID_POSITION, "Neck_Tilt": MID_POSITION, "Right_Wheel": 0, "Left_Wheel": 0}
    serialQueue = []
    class Servo_Motor:
        def __init__(self, id, type, channel, speed = 0, target = 0):
            self.id = id
            self.channel = channel
            self.type = type
            self.speed = speed
            self.target = target
            return
        
        def set_channel(self, channel):
            self.channel = channel
            return
        
        def get_channel(self):
            return self.channel
        
        def get_type(self):
            return self.type
        
        def set_speed(self, speed):
            self.speed = speed
            return
        
        def get_speed(self):
            return self.speed
        
        def set_target(self, target):
            self.target = target
            
        def get_target(self):
            return self.target
        
        def encode_target(self):
            return [chr(self.target&0x7F), chr((self.target>>7)&0x7F)]
                    
        def encode_speed(self):
            return [chr((Tango_Controller.MID_POSITION - self.speed)&0x7F), chr(((Tango_Controller.MID_POSITION - self.speed)>>7)&0x7F)]
        pass
    DEBUG = True
    def __init__(self, serialController, mode):
        self.serial = serialController
        self.mode = mode
        self.motors = {"Right_Wheel": self.Servo_Motor("Right_Wheel", "Motor", 1), "Left_Wheel": self.Servo_Motor("Left_Wheel", "Motor", 2)}
        self.servos = {"Waist": self.Servo_Motor("Waist", "Servo", 0), "Neck_Pan": self.Servo_Motor("Neck_Pan", "Servo", 3), "Neck_Tilt": self.Servo_Motor("Neck_Tilt", "Servo", 4)}
        
        self.init_motors()
        self.init_servos()
        return
    
    # Initializing
    def init_motors(self):
        print("Initializing Motors") if self.DEBUG else None
        motorList = self.motors.keys()
        for motor in motorList:
            self.motors[motor].set_speed(self.DEFAULT_VALUES[motor])
        return
    
    def init_servos(self):
        print("Initializing Servos") if self.DEBUG else None
        servoList = self.servos.keys()
        for servo in servoList:
            self.servos[servo].set_target(self.DEFAULT_VALUES[servo])
        return
    
    # Robot Serial Controls
    def add_serial_queue(self, command):
        print("Command Added ", command) if self.DEBUG else None
        self.serialQueue.append(command)
        return

    def send_command(self):
        print("Command Sent ", self.serialQueue) if self.DEBUG else None
        self.serial.write(self.serialQueue.encode())
        self.serialQueue = []
        return
    
    def control_motor(self, motorId, speed):
        print("Controlling Motor ", motorId) if self.DEBUG else None
        motor = self.motors[motorId]
        motor_speed = self.MID_POSITION - speed
        if (motor_speed > self.SERVO_STEP_MIN) & (motor_speed < self.SERVO_STEP_MAX):
            motor.set_speed(speed)
        else:
            return
        start_byte = chr(0x84)
        self.add_serial_queue(start_byte)
        self.add_serial_queue(motor.get_channel())
        self.add_serial_queue(motor.encode_speed()[0])
        self.add_serial_queue(motor.encode_speed()[1])
        self.send_command()
        return

    def adjust_motor(self, motorId, speed):
        self.control_motor(motorId, self.motors[motorId].get_speed() + speed)
        return

    def control_servo(self, servoId, position):
        print("Controlling Servo ", servoId) if self.DEBUG else None
        servo = self.motors[servoId]
        target = position
        if (target > self.SERVO_STEP_MIN) & (target < self.SERVO_STEP_MAX):
            servo.set_target(target)
        else:
            return
        start_byte = chr(0x84)
        self.add_serial_queue(start_byte)
        self.add_serial_queue(servo.get_channel())
        self.add_serial_queue(servo.encode_target()[0])
        self.add_serial_queue(servo.encode_target()[1])
        self.send_command()
        return

    def adjust_motor(self, servoId, target):
        self.control_servo(servoId, self.servos[servoId].get_target() + target)
        return
    
    # Movement Set (Works in tandem with Robot Serial Controls)        
    def stop(self):
        print("Wheels Stopping") if self.DEBUG else None
        while (self.MID_POSITION != self.motors["Left_Wheel"].get_speed()) | (self.MID_POSITION != self.motors["Right_Wheel"].get_speed()):
            if self.motors["Left_Wheel"].get_speed() < 0:
                self.adjust_motor("Left_Wheel", self.SERVO_STEP)
            else:
                self.adjust_motor("Right_Wheel", -self.SERVO_STEP)
            if self.motors["Right_Wheel"].get_speed() < 0:
                self.adjust_motor("Right_Wheel", self.SERVO_STEP)
            else:
                self.adjust_motor("Right_Wheel", -self.SERVO_STEP)
        return
    
    def forward(self, speed):
        print("Wheels Moving Forward") if self.DEBUG else None
        if (speed > 0):
            self.control_motor("Right_Wheel", speed)
            self.control_motor("Left_Motor", speed)
        return
    
    def backward(self, speed):
        print("Wheels Moving Backward") if self.DEBUG else None
        if (speed > 0):
            self.control_motor("Right_Wheel", -speed)
            self.control_motor("Left_Motor", -speed)
        return
    
    def steer_right(self):
        print("Spinning Right") if self.DEBUG else None

        return
    
    def steer_left(self):
        print("Spinning Left") if self.DEBUG else None

        return
    
    pass
