####################################################################
#                                                                  #
# Skyler Corrigan                                                  #
# ECE351-52                                                        #
# Lab Number: 05                                                   #
# Due Date: 09/29/2022                                             #
# GitHub Codes: https://github.com/ElfinPeach/ECE351_Code.git      #
# GitHub Reports: https://github.com/ElfinPeach/ECE351_Report.git  #
#                                                                  #
####################################################################
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.signal as sig

#------------FUNCTIONS----------------------------------------#

def cosine(t): # The only variable sent to the function is t
    y = np.zeros(t.shape) # initialze y(t) as an array of zeros
    for i in range(len(t)): # run the loop once for each index of t
        y[i] = np.cos(t[i])
    return y

#Make a step function using an array t, stepTime, and stepHeight
def stepFunc(t, startTime, stepHeight):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        if(t[i] >= startTime):
            y[i] = stepHeight
    return y

#Make a ramp function using an array t, startTime, and slope
def rampFunc(t, startTime, slope):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        if(t[i] >= startTime):
            y[i] = t[i]-startTime
    y = y * slope
    return y

#Make e^at function using array t, startTime, and a (alpha)
def eExpo(t,amplatude,alpha):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        y[i]=amplatude * math.exp(alpha * (t[i]))
    
    return y

#Convolution function
def convolve(f1, f2):
    
    #Both functions need to be the same size or else the universe will explode!
    Nf1 = len(f1)
    Nf2 = len(f2)
    
    f1Extend = np.append(f1,np.zeros((1,Nf2-1)))
    f2Extend = np.append(f2,np.zeros((1,Nf1-1)))
    
    y = np.zeros(f1Extend.shape)
    
    for i in range(Nf1 + Nf2 - 2):
        y[i] = 0
        
        for j in range(Nf1):
            if (i-j+1 >0):
                try:
                    y[i] += f1Extend[j] * f2Extend[i-j+1]
                
                except:
                    print(i,j)
    return y

def funcPlot(t, R, L, C):
    
    X = (1/(R*C))
    tempR = -0.5 * ((1/(R*C))**2) #real part of g
    tempI = 0.5 * X * (math.sqrt((X**2)) - (4/(L*C))) #imaginary part of g
    
    gMag = math.sqrt( (tempR**2) + (tempI**2)) 
    
    tempTanX = 0.5 * (math.sqrt((X**2)) - (4/(L*C))) #numerator of angle g
    tempTanY = -0.5 * ((1/(R*C))**2) #denominator for angle g
    
    gDeg = math.atan(tempTanX / tempTanY) #g angle
    
    w = 0.5 * np.sqrt(X**2 - 4*(1/np.sqrt(L*C))**2 + 0*1j)
    a= (-0.5) * X
    
    y = (4e4)*(gMag/np.abs(w)) * np.exp(a * t) * np.sin(np.abs(w) * t + gDeg) * stepFunc(t, 0, 1)
    
    return y


#--------------END FUNCTIONS-----------------------------#

#---------------DEFINITIONS------------------------------#

steps = 1e-6

#t for part 1
start = 0
stop = 1.2e-3
#Define a range of t. Start at 0 and go to 20 (+a step)
t = np.arange(start, stop + steps, steps)


#For circuit-------------RLC DEF----------
R = 1e3 #Ohms
L = 27e-3 #Henries
C = 100e-9 #Ferrets :)

y = funcPlot(t, R, L, C)

#-------------END DEFINITIONS----------------------------#

#--------------Part One----------------------------------#
num = [0, L, 0] #Creates a matrix for the numerator
den = [C*R*L, L, R] #Creates a matrix for the denominator

tout1 , ySig = sig.impulse ((num , den), T = t)


#Make plots
plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(t,y)
plt.grid()
plt.ylabel('Hand Calc Output')
plt.title('Plots of hand calculated and computer calculate Function')

plt.subplot(2,1,2)
plt.plot(t,ySig)
plt.grid()
plt.ylabel('sig.impulse Output')

#-----------------------Part Two--------------------------#
tout2 , yStep = sig.step ((num , den), T = t)

plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(t,ySig)
plt.grid()
plt.ylabel('ySig Output')
plt.title('Plots of sig.impulse and sig.step Function')

plt.subplot(2,1,2)
plt.plot(t,yStep)
plt.grid()
plt.ylabel('sig.step Output')

plt.show()

