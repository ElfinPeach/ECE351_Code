####################################################################
#                                                                  #
# Skyler Corrigan                                                  #
# ECE351-52                                                        #
# Lab Number: 01                                                   #
# Due Date: 09/08/2022                                             #
# GitHub Codes: https://github.com/ElfinPeach/ECE351_Code.git      #
# GitHub Reports: https://github.com/ElfinPeach/ECE351_Report.git  #
#                                                                  #
####################################################################
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import math

#------------FUNCTIONS----------------------------------------#

#Make a step function using an array t, stepTime, and stepHeight
def Step(t, startTime, stepHeight):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        if(t[i] >= startTime):
            y[i] = stepHeight
    return y

#Make a ramp function using an array t, startTime, and slope
def Ramp(t, startTime, slope):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        if(t[i] >= startTime):
            y[i] = t[i]-startTime
    y = y * slope
    return y

#Make e^at function using array t, startTime, and alpha
def eExpo(t,startTime,amplitude,alpha):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        if(t[i] >= startTime):
            y[i]=amplitude * math.exp(alpha * (t[i]-startTime))
    
    return y

#Convolution function or something
def my_convolve(f1, f2):
    
    #Check both functions are the same size
    Nf1 = len(f1)
    Nf2 = len(f2)
    
    f1Extend = np.append(f1,np.zeros((1,Nf2-1)))
    f2Extend = np.append(f2,np.zeros((1,Nf1-1)))
    
    y = np.zeros(f1Extend.shape)
    
    for i in range(Nf1 + Nf2 - 2):
        
        if Nf1 != Nf2: #check both funcitons same length
            print("Error: Arrays not the same size")
            break
        
        y[i] = 0  #initialization
        
        for j in range(Nf1):
            if (i-j+1 >0):
                try:
                    y[i] += f1Extend[j] * f2Extend[i-j+1]
                
                except:
                    print(i,j)
    return y
#--------------END FUNCTIONS-----------------------------#

#--------------START DEFINITIONS-------------------------#
#Define step size
StepSize = 1e-2

#Define a range of t. Start at 0 and go to 20 w/ a StepSizeize of step
t = np.arange(0, 20+ StepSize, StepSize)

#-------------END DEFINITIONS----------------------------#

#Make stuff to plot!
func1 = Step(t,2,1) - Step(t, 9, 1)
func2 = eExpo(t,0,1,-1)
func3 = (Ramp(t,2,1) * (Step(t, 2, 1) - Step(t, 3, 1))) + ((Ramp(t, 3, -1) + 1) * (Step(t, 3, 1) - Step(t, 4, 1)) ) #x * y

#Own Convolution Function
f1Convolvef2_Mine = my_convolve(func1, func2)
f2Convolvef3_Mine = my_convolve(func2, func3)
f1Convolvef3_Mine = my_convolve(func1, func3)

#Built in Convolution Function
f1Convolvef2_Library = sig.convolve(func1, func2)
f2Convolvef3_Library = sig.convolve(func2, func3)
f1Convolvef3_Library = sig.convolve(func1, func3)

#Make a t range to pot the convolve functions!
#This should be the same as the size for all convolutions for this lab
tConv = np.arange(0, len(f1Convolvef2_Mine) * StepSize, StepSize)

#Three Figures Plot
plt.figure(figsize=(10,7))
plt.subplot(3,1,1)
plt.plot(t,func1)
plt.grid()
plt.ylabel('Output Step')
plt.title('Three Functions Together')

plt.subplot(3,1,2)
plt.plot(t,func2)
plt.grid()
plt.ylabel('Output Expenential')

plt.subplot(3,1,3)
plt.plot(t,func3)
plt.grid()
plt.ylabel('Output Ramps')

#Convilution plots
plt.figure(figsize=(10,7))
plt.subplot(3,2,1)
plt.plot(tConv, f1Convolvef2_Mine)
plt.grid()
plt.ylabel("Output F1 Conv. F2")
plt.title("My Convolvilution")

plt.subplot(3,2,2)
plt.plot(tConv, f1Convolvef2_Library)
plt.grid()
plt.ylabel("Output F1 Convolve F2")
plt.title("Library Convolvilution")

    #f2 convolve f3
plt.subplot(3,2,3)
plt.plot(tConv, f2Convolvef3_Mine)
plt.grid()
plt.ylabel("Output F2 Convolve F3")

plt.subplot(3,2,4)
plt.grid()
plt.plot(tConv, f2Convolvef3_Library)

    #f1 convolve f3
plt.subplot(3,2,5)
plt.plot(tConv, f1Convolvef3_Mine)
plt.grid()
plt.ylabel("Output F1 Convolve F3")

plt.subplot(3,2,6)
plt.grid()
plt.plot(tConv, f1Convolvef3_Library)

plt.show()