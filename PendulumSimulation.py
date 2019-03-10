import matplotlib.pyplot as plt
import numpy as np
import math as m
import scipy.signal as s
g = -9.81

def update_system(acc,ang,vel,time1,time2):
    dt = time2 - time1
    ang_Next = ang + (vel * dt)
    vel_Next = vel + (acc * dt)
    acc_Next = (g/l)*m.sin(ang_Next)
    return ang_Next, vel_Next, acc_Next

#def print_system(time,ang,vel,acc):
    #print("TIME:    ", time)
    #print("ANGLE:    ", ang)
    #print("ANGULAR VELOCITY:    ", vel)
    #print("ACCELERATION:    ", acc, '\n')
    #print((ang, vel, acc))

#initial conditions
l = 10                                            
ang = [m.pi/4]
vel = [0]
acc = [(g/l)*(m.sin(m.pi/2))]

time = np.linspace(0,20,20000)
#print_system(time[0],ang[0], vel[0], acc[0])


i = 1
while i < len(time):
    #update angle and velocity using previous values and time step
    ang_Next, vel_Next, acc_Next = update_system(acc[i-1], ang[i - 1], vel[i -1], time[i - 1], time[i])
    ang.append(ang_Next)
    vel.append(vel_Next)
    acc.append(acc_Next)
    #print_system(time[i], ang[i], vel[i], acc[i])
    i += 1



plt.figure(figsize = (4,6))
plt.subplot(3,1,1)
plt.plot(time, ang, 'r-') 

plt.xlabel('Time (seconds)')
plt.ylabel('Angle (rad)')
plt.title('Angle vs Time')
plt.xlim((0, 5)) # set x range to -1 to 8
plt.grid()


#plt.subplot(3,1,2)
#plt.plot(time, vel, 'b-') 
#plt.xlabel('Time (seconds)')
#plt.ylabel('Angular Velocity (rad/s)')
#plt.title('Angular Velocity vs Time')
#plt.xlim((0, 20)) # set x range to -1 to 8
#plt.grid()


plt.subplot(3,1,3)
plt.plot(time, acc, 'k-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (rad/s^2)')
plt.title('Angular Acceleration vs Time')
plt.xlim((-1, 8)) # set x range to -1 to 8
plt.show()

#Converts lists to arrays for analysis and plotting
angarray = np.array(ang)
accarray = np.array(acc)
timearray = np.array(time)

#Finds peaks of angle array
peaks = s.find_peaks(angarray)
maxes = peaks[0]
period = timearray[maxes[1]]-timearray[maxes[0]]
print("The period for the length " + str(l) + " meters" + " is " + str(period) + " seconds")

#################################

#Creates period vs length arrays using data from code above. Plots length vs period.
periods = [2.089, 2.953, 3.616, 4.175, 4.667, 5.112, 5.522, 5.903, 6.261, 6.599]
lengths = [1,2,3,4,5,6,7,8,9,10]
periodarray = np.array(periods)
lengtharray = np.array(lengths)

plt.subplot(3,1,3)
plt.plot(lengtharray, periodarray, 'k-') 
plt.xlabel('Length (meters)')
plt.ylabel('Period (seconds)')
plt.title('Length of Pendulum vs Oscillation Period')
plt.xlim((1, 10)) # set x range to -1 to 8
plt.show()
