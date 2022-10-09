####################################################################
#                                                                  #
# Skyler Corrigan                                                  #
# ECE351-52                                                        #
# Lab Number: 07                                                   #
# Due Date: 10/13/2022                                             #
# GitHub Codes: https://github.com/ElfinPeach/ECE351_Code.git      #
# GitHub Reports: https://github.com/ElfinPeach/ECE351_Report.git  #
#                                                                  #
####################################################################
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

        #Universal Stuff for Lab

    #Step size
steps = 1e-2

    #t for part 1
start = 0
stop = 10
    #Define a range of t. Start at 0 and go to 20 (+a step)
t = np.arange(start, stop + steps, steps)

#--------------PART 1, Open Loop Test------------------------------------#
    #Find the roots and the poles
    
    #A(s)=(s+4)/((s^2+4s+3))
A_num = [1, 4]
A_den = [1, 4, 3]

    #B(s)=s^2+26s+168
B_num = [1, 26, 168]
B_den = [1]

    #G(s)=(s+9)/((s^2+-6s-16)(s+4))=(s+4)/(s^3-2s^2-40s-64)
G_num = [1, 4]
G_den = [1, -2, -40, -64]

Azeros, Apoles, Again = sig.tf2zpk(A_num, A_den)
Bzeros, Bpoles, Bgain = sig.tf2zpk(B_num, B_den)
Gzeros, Gpoles, Ggain = sig.tf2zpk(G_num, G_den)

print("Zeros for A: ", Azeros)
print("")
print("Poles for A: ", Apoles)
print("")
print("Zeros for B: ", Bzeros)
print("")
print("Poles for B: ", Bpoles)
print("")
print("Zeros for G: ", Gzeros)
print("")
print("Poles for G: ", Gpoles)
print("")

H_open_num = [1, 9]
H_open_den = [1, -2, -37, -82, -48]

H_open_zeros, H_open_poles, H_open_gain = sig.tf2zpk(H_open_num, H_open_den)
print("Zeros of the Open Loop H(s)")
print(H_open_zeros)
print("")
print("Poles of the Open loop H(s)")
print(H_open_poles)
print("")

stepTOpen, stepHOpen = sig.step((H_open_num, H_open_den), T = t)

plt.figure(figsize=(10,7))
plt.plot(stepTOpen, stepHOpen)
plt.grid()
plt.xlabel("Time")
plt.ylabel("Output")
plt.title("Open Loop H(s) Step Response")

#-------------PART 2, Closed Loop Test---------------------------------------#

    #Finding the Numerator and Denomenator of transfer function
H_closed_num = sig.convolve([1,4],[1,9])

part_den = sig.convolve([1,1],[1,3])
H_closed_den = sig.convolve(part_den,[2,33,362,1448])

print("Closed loop numerator = ", H_closed_num)
print("Closed loop denemonator = ", H_closed_den)
print()

    #Numbers I got by hand:
#H_clo_num = [1, 13, 36]
#H_clo_den = [2, 41, 500, 2995, 6878, 4344]

H_closed_zeros, H_closed_poles, H_closed_gain = sig.tf2zpk(H_closed_num, H_closed_den)

print("Poles of the Closed loop H(s):")
print(H_closed_poles)
print("")

    #Define transfer function!
stepTClosed, stepHClosed = sig.step((H_closed_num, H_closed_den), T = t)

    #Make plots for pt1
plt.figure(figsize=(10,7))
plt.plot(stepTClosed, stepHClosed)
plt.grid()
plt.xlabel("Time")
plt.ylabel("Output")
plt.title("Closed Loop H(s) Step Response")

#--------SHOW PLOTS--------------------#
plt.show()