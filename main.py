Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@Fishhkabob 
Fishhkabob
/
Ps4-to-Ev3
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Ps4-to-Ev3/main.py /
@wespd
wespd The base line code
…
Latest commit c01ec29 5 days ago
 History
 1 contributor
83 lines (64 sloc)  2.36 KB

#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch

import struct

# Declare motors 
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
steer_motor = Motor(Port.A)
forward = 0
left = 0
right = 0


# Auto center steering wheels.
steer_motor.run_until_stalled(250)
steer_motor.reset_angle(80)
steer_motor.run_target(300,0)


# A helper function for converting stick values (0 - 255)
# to more usable numbers (-100 - 100)
def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
 
    val: float or int
    src: tuple
    dst: tuple
 
    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    """
    return (float(val-src[0]) / (src[1]-src[0])) * (dst[1]-dst[0])+dst[0]


#ps4 mapping
infile_path = "/dev/input/event4"

# open file in binary mode
in_file = open(infile_path, "rb")

# Read from the file
# long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'    
EVENT_SIZE = struct.calcsize(FORMAT)
event = in_file.read(EVENT_SIZE)

while event:
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)
    
    if ev_type == 1: # A button was pressed or released.
        if code == 318 and value == 1:
            right = 85
            print(steer_motor.angle())
        if code == 317 and value == 1:
            right = -100
            print(steer_motor.angle())
        if code == 318 and code == 317 and value == 1:
            right = -100
            print(steer_motor.angle())
         if code == 318 and code == 317  and value == 0:
            right = 0
            print(steer_motor.angle())
            
    elif ev_type == 3: # Stick was moved
        if code == 0: 
            left = scale(value, (0,255), (40, -40))
        if code == 4: # Righ stick vertical
            forward = scale(value, (0,255), (100,-100))
        
    # Set motor voltages. 
    left_motor.dc(forward - left)
    right_motor.dc(forward + left)

    # Track the steering angle
    steer_motor.track_target(right)

    # Finally, read another event
    event = in_file.read(EVENT_SIZE)

in_file.close()
