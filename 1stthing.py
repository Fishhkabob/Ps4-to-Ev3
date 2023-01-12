#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time



# Declare motors 
y = int()
y == 3
x = int()
x == 0
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
arm_motor = Motor(Port.A)
ultrasonicSensor = UltrasonicSensor(Port.S4)
forward = 0
left = 0
right = 0
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=152)


# Auto center steering wheels.
arm_motor.run_until_stalled(250)
arm_motor.reset_angle(45)
arm_motor.run_target(90,0)
boolean_result = True


#automation phase
in_file = open  
while True:
    if x == 0:
        print(arm_motor.angle())
        print(ultrasonicSensor.distance())
        arm_motor.run_until_stalled(250)
        wait(2000)
        arm_motor.run_until_stalled(-250)
        print(arm_motor.angle())
        print(ultrasonicSensor.distance())
        wait(2000)

    if arm_motor.angle() <= -90 and ultrasonicSensor.distance() >= 400:
        x == 1
        robot.drive(100, 0)
        
    if ultrasonicSensor.distance() < 400:
            robot.stop
            robot.turn(90)
            x == 0
    
    if y == 9:
        break

    

    




   #while x == 0:
   

#while isDoing() == True:
    #if ultrasonicSensor.distance() < 400:
            #robot.drive(-40, 90)


#in_file.close()