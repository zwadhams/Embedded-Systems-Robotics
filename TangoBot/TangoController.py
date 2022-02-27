import time, serial, sys

class Tango_Controller:
    class Servo_Motor:
        def __init__(self, id, type, speed = 0, target = 0):
            self.id = id
            self.address = None
            self.type = type
            self.speed = speed
            self.target = target
            return
        
        def set_address(self, address):
            self.address = address
            return
        
        def get_address(self):
            return self.address
        
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
        
        pass
    DEBUG = True
    def __init__(self, serialController, mode):
        self.serial = serialController
        self.mode = mode
        self.motors = [self.Servo_Motor("Right_Wheel", "Motor"), self.Servo_Motor("Left_Wheel", "Motor")]
        self.servos = [self.Servo_Motor("Waist", "Servo"),self.Servo_Motor("Neck_Pan", "Servo"), self.Servo_Motor("Neck_Tilt", "Servo")]
        
        return
    
    # Initializing
    def init_motors(self):
        print("Initializing Motors") if self.DEBUG else None
        
        return
    
    def init_servors(self):
        print("Initializing Servos") if self.DEBUG else None
        
        return
    
    # Robot Serial Controls
    def send_command(self, command):
        print("Command Sent ", command) if self.DEBUG else None
        
        return
    
    def control_motor(self, motorId):
        print("Controlling Motor ", motorId) if self.DEBUG else None
        
        return
    
    def control_servo(self, servoId):
        print("Controlling Servo ", servoId) if self.DEBUG else None
        
        return
    
    # Movement Set (Works in tandem with Robot Serial Controls)
    # TODO: Ramping Speed Controls
        
    def stop(self):
        print("Wheels Stopping") if self.DEBUG else None
        
        return
    
    def forward(self):
        print("Wheels Moving Forward") if self.DEBUG else None
        
        return
    
    def backward(self):
        print("Wheels Moving Backward") if self.DEBUG else None
        
        return
    
    def turn_wheel(self, direction):
        print("Wheels Turning ", direction) if self.DEBUG else None
        
        return
    
        
    def steer_wheel(self, direction):
        print("Wheels Steering ", direction) if self.DEBUG else None
        
        return


    
    pass