####################################################################
#                                                                  #
# Skyler Corrigan                                                  #
# ECE351-52                                                        #
# Lab Number: 08                                                   #
# Due Date: 10/20/2022                                             #
# GitHub Codes: https://github.com/ElfinPeach/ECE351_Code.git      #
# GitHub Reports: https://github.com/ElfinPeach/ECE351_Report.git  #
#                                                                  #
####################################################################
import numpy as np
import matplotlib.pyplot as plt

#---------PT 1-------------------------------------------#
def b_k(n):
    b = (2 / (n * np.pi)) * (1 - np.cos((n) * np.pi))
    return b


def W(period):
    return ((2*np.pi)/period)


def xFourier(t, period, n):
    x_t = 0 #initialization
    for i in np.arange(1, n+1): 
        x_t += (b_k(i))*(np.sin(i * W(period) * t))
    return x_t

#Since this is an odd function, a0 = an = 0

#step size
steps = 1e-1

# t for part 1
start = 0
stop = 20
# Define a range of t. Start at 0 and go to 20 (+a step) 
t = np.arange(start, stop + steps, steps)

#Make arrays to plot against t
x_1 = xFourier(t, 8, 1)
x_3 = xFourier(t, 8, 3)
x_15 = xFourier(t, 8, 15)
x_50 = xFourier(t, 8, 50)
x_150 = xFourier(t, 8, 150)
x_1500 = xFourier(t, 8, 1500)

#plot stuff
plt.figure(figsize=(10, 12))
#space out subplots
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9,
                    top=1.0, wspace=0.4, hspace=0.4)

#PLOT EVERYTHING!!!!
plt.subplot(6, 1, 1)
plt.plot(t, x_1)
plt.title("Estimation when N=1")
plt.ylabel("x(t) Output")
plt.grid()

plt.subplot(6, 1, 2)
plt.plot(t, x_3)
plt.title("Estimation when N=3")
plt.ylabel("x(t) Output")
plt.grid()

plt.subplot(6, 1, 3)
plt.plot(t, x_15)
plt.title("Estimation when N=15")
plt.ylabel("x(t) Output")
plt.grid()

plt.subplot(6, 1, 4)
plt.plot(t, x_50)
plt.title("Estimation when N=50")
plt.ylabel("x(t) Output")
plt.grid()

plt.subplot(6, 1, 5)
plt.plot(t, x_150)
plt.title("Estimation when N=150")
plt.ylabel("x(t) Output")
plt.grid()

plt.subplot(6, 1, 6)
plt.plot(t, x_1500)
plt.title("Estimation when N=1500")
plt.ylabel("x(t) Output")
plt.grid()

plt.show()

print("a0 and an values for a are zero. This is because the wave is odd and has no offset.")
print("")
print("b1 = ", b_k(1))
print("")
print("b2 = ", b_k(2))
print("")
print("b3 = ", b_k(3))