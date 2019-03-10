#Script reads the data from the microbit and plots graphs of time vs angle,
# time vs angular acceleration. The script then smooths the data for time vs
# angle and extracts the period by looking at the peaks from this function.

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as s


fin = open('/Users/Andy/Desktop/pendulum.txt')
        
        
list_lines = []
time = []
angle = []
AngAccel = []

#This loops over each line in the data file. It then separates each line into its 3
# corresponding values. It then appends the values to their respective time, angle,
# and angular acceleration lists.
for line in fin:      
    time.append(float(line.split(',')[1]))       
    angle.append(float(line.split(',')[0]))
    AngAccel.append(float(line.split(',')[2]))  
    
#Plots unfiltered, raw data of time vs angle and time vs acceleration      
plt.figure()
plt.plot(time, angle, 'k-')
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (Degrees)')
plt.title('Pendulum Angle vs Time')


plt.figure()
plt.plot(time, AngAccel, 'k-')

#Converts lists to arrays in order to analyze them using scipy. 
anglearray = np.array(angle)
timearray = np.array(time)
AngAccelarray = np.array(AngAccel)

#Filters the arrays using the scipy medfilt function in order to distinguish peaks.
filteredangle = s.medfilt(angle,13)
filteredaccel = s.medfilt(AngAccel,13)

plt.figure()
plt.plot(timearray, filteredangle, 'k-')
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (Degrees)')
plt.title('Pendulum Angle vs Time')

#Finds peaks, then finds average of the period by adding difference in peaks and
# dividing by the number of peaks. Prints period. 
peaks = s.find_peaks(filteredangle, prominence = 10)
peaksarray = peaks[0]
period = ((timearray[peaksarray[1]]-timearray[peaksarray[0]])+(timearray[peaksarray[2]]-timearray[peaksarray[1]]))/2
print('Average period of pendulum is ' + str(round(float(period),2)) + ' seconds')


    


