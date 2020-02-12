#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import AnalogSensor, UARTDevice
import time
# Write your program here
ev3 = EV3Brick()

ev3.speaker.set_volume(100)
ev3.speaker.say("Jeremy Can of Ski")

xnum=""
ynum=""
def padder(xnum,ynum):

    xnum = "% 5s" % xnum
    ynum = "% 5s" % ynum
    
    return "(" + xnum + "," + ynum + ")"


def mapper(y_ang):
 #mapping function stuff
    xMax = 90
    xMin = -90
    yMax = 90
    yMin = -63
    targetMax=100
    targetMin=-100

    #xSpan = xMax - xMin
    ySpan = yMax - yMin
    targetSpan= targetMax - targetMin

    #xScaled = targetMin + targetSpan*(float(x_ang - xMin)/ float(xSpan))
    yScaled = targetMin + targetSpan*((float(y_ang - yMin)/ float(ySpan)))
    return yScaled

def MotorAngles(x_motor,y_motor):
    x_ang= x_motor.angle()
    y_ang= y_motor.angle()
    #print("X Motor is ", x_ang," Y motor is ", y_ang)
    #Pad for digits to send the data for x and y position as strings

    x_ang= str(x_ang)
    y_ang= str(y_ang)
    anglestring = padder(x_ang, y_ang) 
    #print(len(anglestring))
    print(anglestring)
    return anglestring, x_ang,y_ang


sense = AnalogSensor(Port.S4, False)
sense.voltage()
uart = UARTDevice(Port.S4, 9600, timeout = 10000)
def UARTtest():
    uart.write("TEST")
    wait(100)
    data = uart.read_all()
    print(data)
    ev3.screen.print(data)

# Write your program here
def main():
    #UARTtest()

    x_motor = Motor(Port.C)
    y_motor = Motor(Port.D)
    speed = 0
    y_ang = 0
    x_ang = 0
    x_spd = 0
    y_spd = 0

    isTurnLeft= False
    isTurnRight= False
    light_value = 45
    x_motor.reset_angle(0)
    y_motor.reset_angle(0)
    counter = 0
    lightVal = ''
    while True:
        counter = counter + 1
        anglestring, x_ang, y_ang = MotorAngles(x_motor,y_motor)
        uart.write(anglestring)

        #get light value from other ev3
        wait(10)
       
        data = uart.read()
        
        data = data.decode('utf-8')

        #print("This is DATA:   ", data)
        #print(type(data))
        if (data is not '0') and (data is not '1'):
            data = '100'
        
        lightVal = int(data)
        print("Light Value is: ", lightVal)
        print(type(lightVal))
        #lightVal = 1
        if lightVal is 1:
            #print("IS BRAKING")
            #ev3.speaker.say("SHARK")
            start = time.time()
            if int(x_ang) > 0:
                x_motor.run(1000)
            if int(x_ang) < 0:
                x_motor.run(-1000)
            if int(y_ang) >0:
                y_motor.run(1000)
            if int(y_ang) < 0:
                y_motor.run(1000)
            wait(50)
            print( time.time() - start , " seconds")
            
            x_motor.stop()
            y_motor.stop()
            #x_motor.run_angle(100,10)
            #y_motor.run_angle(100,10)
            anglestring, x_ang, y_ang  = MotorAngles(x_motor,y_motor)
            uart.write(anglestring)
            

        
        
main()