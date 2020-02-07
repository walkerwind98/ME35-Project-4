#!/usr/bin/env pybricks-micropython
#Project 4: Joystick with Feedback
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from pybricks.ev3devio import Ev3devSensor 
import utime
import ev3dev2
from ev3dev2.port import LegoPort

""" class MySensor(Ev3devSensor):  #Define Class 
    _ev3dev_driver_name="ev3-analog-01"
    #do not forget to set port mode to EV3-Analog 
    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0) """


# Before running the code go to Device Browser and Sensors. Make sure you can see ev3-analog-01, otherwise you will get an error.

# Write your program here
def main():
    brick.sound.beep()
    

    x_motor = Motor(Port.C)
    y_motor = Motor(Port.D)
    speed = 0
    y_ang = 0
    x_ang = 0
    isTurnLeft= False
    isTurnRight= False
    light_value = 45
    x_motor.reset_angle(0)
    y_motor.reset_angle(0)
    counter = 0

    while True:
        counter = counter + 1
        x_ang= x_motor.angle()
        y_ang= y_motor.angle()

        if x_ang > 70:
            isTurnRight = True
        if x_ang < 70:
            isTurnLeft = True
        #send angle values or protocol to the other ev3

        #get light value from other ev3

        """ while light_value < 100 :
            x_motor.stop(Stop.BRAKE)
            y_motor.stop(Stop.BRAKE) """

        if counter%100 is 0:
            x_motor.stop(Stop.BRAKE)
            y_motor.stop(Stop.BRAKE)
            wait(1000)

        isTurnLeft= False
        isTurnRight= False
        







        """ left_color = sensor_left.readvalue()
        right_color = sensor_right.readvalue()
        print('left sensor is ', left_color)
        print('right sensor is ', right_color)
        left_motor.run(speed)
        right_motor.run(speed)

        #while left_color > value:  #if left sensor sees the black line
            #left_motor.run(speed)
            #right_motor.run(speed + 200) #turn left

        #while right_color > value:  #if right sensor sees the black line
            #right_motor.run(speed)
            #left_motor.run(speed + 200)  #turn right """
        
main()

