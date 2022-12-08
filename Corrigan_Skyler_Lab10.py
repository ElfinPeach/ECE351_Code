####################################################################
#                                                                  #
# Skyler Corrigan                                                  #
# ECE351-52                                                        #
# Lab Number: 10                                                   #
# Due Date: 11/10/2022                                             #
# GitHub Codes: https://github.com/ElfinPeach/ECE351_Code.git      #
# GitHub Reports: https://github.com/ElfinPeach/ECE351_Report.git  #
#                                                                  #
####################################################################
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import control as con


#---------PART 1-----------------------------------#
    #Define step size
steps = 1

    #t for part 1
start = 1e3
stop = 1e6
    #Define a range of w, with a stepsize of step
w = np.arange(start, stop, steps)

#------------------------------TASK 1, Part 1---------------#
    # Data from RLC circuit
R=1e3
L=27e-3
C=100e-9


    # Magnitude function and phase function. Angle is in rad, gets converted to deg
magH = 10*np.log((w/(R*C)) / np.sqrt( (w/(R*C))**2 + (1/(L*C)-w**2)**2))
angH = ((np.pi/2) - np.arctan( (w/(R*C)) / (-1*(w**2) + (1/(L*C))) )) * (180/np.pi)


    # Angle correction
for i in range(len(angH)):
    if (angH[i] > 90):
        angH[i] = angH[i] - 180

plt.figure(figsize=(10,7))
plt.subplot(2,1,1) #Top Figure
plt.grid()
plt.semilogx(w, magH)
plt.title("hand-solved")
plt.subplot(2,1,2)
plt.grid()
plt.semilogx(w, angH)
plt.show()

#----------------------------TASK 1, PART 2------------#
numh = [1/(R*C),0]
denh = [1,1/(R*C),1/(L*C)]
sys = sig.TransferFunction(numh,denh)
ang,mag,phase = sig.bode(sys,w)

plt.figure(figsize=(10,7))
plt.subplot(2,1,1) 
plt.grid()
plt.semilogx(ang, mag)
plt.title("sig.bode Plot")
plt.subplot(2,1,2)
plt.grid()
plt.semilogx(ang, phase)
plt.show()


#------------------------Task 1, Part 3--------------------#
sys = con.TransferFunction(numh,denh)
_ = con.bode(sys, w, dB=True, Hz=True, deg=True, Plot=True)


#-----------------Task 2------------------------
t_steps = 1e-7
t = np.arange(0, 0.01+t_steps, t_steps)
x = (np.cos(2*np.pi*100*t)+ np.cos(2*np.pi*3024*t) + np.sin(2*np.pi* 50000*t))

numZ, denZ = sig.bilinear(numh, denh, 1/t_steps)
xFiltered = sig.lfilter(numZ, denZ, x)

plt.figure(figsize=(10,7))
plt.subplot(2,1,1) #Top Figure
plt.grid()
plt.plot(t,x)
plt.title("Unfiltered Signal")
plt.subplot(2,1,2)
plt.plot(t,xFiltered)
plt.title("Filtered Signal")
plt.grid()
plt.show()