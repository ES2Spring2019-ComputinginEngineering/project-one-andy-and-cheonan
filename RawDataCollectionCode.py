import microbit
import math
import random

g = -9.81
rod_length = 0.55


#Function finds the angle of the pendulum 
def yangle(accel_z, accel_y):
    angle_y = math.atan2(accel_y, accel_z)
    return (math.degrees(angle_y))

#Function finds the acceleration of the pendulum in the y direction (angular acceleration)
def angularacceleration(accel_y, rod_length):
    ang_accel = ((accel_y)/rod_length)*g/1000
    return ang_accel





count = 0

#This script will collect data from the microbit when the a button is pressed, and will stop collecting it when it is pressed a second time. 
#it will create a file with lines showing angle, time, and angular acceleration.

while count == 0:
    if microbit.button_a.is_pressed() == True:
        count = 1
        microbit.sleep(200)
        
with open('pendulum.txt', 'w') as fout:
    while count == 1:
        microbit.sleep(10)
        accel_x = microbit.accelerometer.get_x()
        accel_y = microbit.accelerometer.get_y()
        accel_z = microbit.accelerometer.get_z()
        Yangle = yangle(accel_z, accel_y)
        timepassed = microbit.running_time()/1000
        fout.write(str(Yangle)+','+str(timepassed)+','+str(angularacceleration(accel_y, rod_length)))
        fout.write("\n")
        if microbit.button_a.is_pressed() == True:
            break
