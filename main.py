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

import ubinascii, ujson, urequests, utime

""" import ev3dev2
from ev3dev2.port import LegoPort """

""" class MySensor(Ev3devSensor):  #Define Class 
    _ev3dev_driver_name="ev3-analog-01"
    #do not forget to set port mode to EV3-Analog 
    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0) """


# Before running the code go to Device Browser and Sensors. Make sure you can see ev3-analog-01, otherwise you will get an error.

def SL_setup():
     urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
     headers = {"Accept":"application/json","x-ni-api-key":'HiJL-xViqSKa6rWkA7Nhwwa8F_d6D2UaK3SkOKUo7n'}
     return urlBase, headers
     
def Put_SL(Tag, Type, Value):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     propValue = {"value":{"type":Type,"value":Value}}
     
     try:
          print(urlValue,headers=headers,json=propValue)
          reply = urequests.put(urlValue,headers=headers,json=propValue).text
     except Exception as e:
          print(e)         
          reply = 'failed'
     return reply

def Get_SL(Tag):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     try:
          value = urequests.get(urlValue,headers=headers).text
          data = ujson.loads(value)
          print(data)
          result = data.get("value").get("value")
     except Exception as e:
          print(e)
          result = 'failed'
     return result
     
def Create_SL(Tag, Type):
     urlBase, headers = SL_setup()
     urlTag = urlBase + Tag
     propName={"type":Type,"path":Tag}
     try:
          urequests.put(urlTag,headers=headers,json=propName).text
     except Exception as e:
          print(e)

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


# Write your program here
def main():
    brick.sound.beep()
    
   


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
        x_ang= x_motor.angle()
        y_ang= y_motor.angle()
        print("X Motor is ", x_ang," Y motor is ", y_ang)
        

        # if x_ang > 70:
        #     isTurnRight = True
        # if x_ang < 70:
        #     isTurnLeft = True
        # #send angle values or protocol to the other ev3

        #get spd values mapped, send to systemlink
        yspd = mapper(y_ang)

        x_ang= str(x_ang)
        y_ang= str(y_ang)

        #Put_SL('angleX', "STRING", str(x_ang))
        #Put_SL('angleY','STRING',str(y_spd))

        #get light value from other ev3
        lightVal = Get_SL(lightVal)
        print("Light Value is", lightVal)

        """ while light_value < 100 :
            x_motor.stop(Stop.BRAKE)
            y_motor.stop(Stop.BRAKE) """

        if counter%1000 is 0:
            print("IS BRAKING")
            x_motor.stop(Stop.BRAKE)
            y_motor.stop(Stop.BRAKE)
            x_ang= x_motor.angle()
            y_ang= y_motor.angle()
            print("X Motor is ", x_ang," Y motor is ", y_ang)
            wait(1000)
            x_motor.stop()
            y_motor.stop()

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

