####################################################################
#                                                                  #
# Skyler Corrigan                                                  #
# ECE351-52                                                        #
# Lab Number: 06                                                   #
# Due Date: 10/06/2022                                             #
# GitHub Codes: https://github.com/ElfinPeach/ECE351_Code.git      #
# GitHub Reports: https://github.com/ElfinPeach/ECE351_Report.git  #
#                                                                  #
####################################################################
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

#------------FUNCTIONS----------------------------------------#

#Make a step function using an array t, stepTime, and stepHeight
def stepFunc(t, startTime, stepHeight):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        if(t[i] >= startTime):
            y[i] = stepHeight
    return y

#----------------END FUNCTIONS-----------------------------#

#---------Part 1-------------------------------------------#
    #Define step size
steps = 1e-2

    #t for part 1
start = 0
stop = 2
    #Define a range of t. Start at 0 and go to 20 (+a step)
t = np.arange(start, stop + steps, steps)

    #Prelab stuff
h = ((np.exp(-6 * t)) + (-0.5 * np.exp(-4 * t))+ 0.5) * stepFunc(t, 0, 1)

    #Make the H(s) using the sig.step()
    
num = [1, 6, 12] #Creates a matrix for the numerator
den = [1, 10, 24] #Creates a matrix for the denominator

tout , yStep = sig.step((num , den), T = t)

den_residue = [1, 10, 24, 0]

    #Make and print the partial fraction decomp
roots, poles, _ = sig.residue(num, den_residue)

print("Part 1")
print("Roots =", roots)
print("Poles =", poles)


    #Make plots for pt1
plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(t,h, 'purple')
plt.grid()
plt.ylabel('Hand Solved Output')
plt.title('Plots of Hans Solved and Computer Solved Outputs')

plt.subplot(2,1,2)
plt.plot(t,yStep, 'red')
plt.grid()
plt.ylabel('sig.step Output')


#------------PART 2-------------------------

    #Define step size
steps = 1e-2

    #t for part 1
start = 0
stop = 4.5
    #Define a range of t2. Start at 0 and go to 20 (+a step)
t2 = np.arange(start, stop + steps, steps)

    #Make numerator and denomentaor for sig.residue()
num2 = [25250]
den2 = [1, 18, 218, 2036, 9085, 25250, 0]

R, P, K = sig.residue(num2, den2)

print("")
print("Part 2")
print("Roots =", R)
print("Poles =", P)

    #cosine vethod
yt = 0

    #Range iterates through each root
for i in range(len(R)):
    angleK = np.angle(R[i])
    magK = np.abs(R[i])
    W = np.imag(P[i])
    a = np.real(P[i])
        
    yt += magK * np.exp(a * t2) * np.cos(W * t2 + angleK) * stepFunc(t2, 0, 1)
    
print("K value =", magK)
print("K angle =", angleK)
    
#Make the lib generated step response
den2_step = [1, 18, 218, 2036, 9085, 25250]
tStep2, yStep2 = sig.step((num2,den2_step), T = t2)

    #Show Plots
plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(t2, yt,'purple')
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Cosine Method vs. Lib sig.step Method')


plt.subplot(2,1,2)
plt.plot(tStep2, yStep2, 'red')
plt.grid()
plt.xlabel('t')
plt.ylabel('sig.step y(t)')

#-------------SHOW ALL PLOTS-----------------
plt.show()