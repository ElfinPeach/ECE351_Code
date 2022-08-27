####################################################################
#                                                                  #
# Skyler Corrigan                                                  #
# ECE351-52                                                        #
# Lab Number: 01                                                   #
# Due Date: 09/01/2022                                             #
# GitHub Codes: https://github.com/ElfinPeach/ECE351_Code.git      #
# GitHub Reports: https://github.com/ElfinPeach/ECE351_Report.git  #
#                                                                  #
####################################################################

# Sample code for Lab 1
import numpy as np
import matplotlib.pyplot as plt

# Define variables
steps = 0.1 # step size
x = np.arange (-2,2+steps ,steps) # notice the final value is
# ‘2+steps ‘ to include ‘2‘
y1 = x + 2
y2 = x**2

# Code for plots
plt.figure(figsize =(12 ,8)) # start a new figure , with
# a custom figure size
plt.subplot (3,1,1) # subplot 1: subplot format(row , column , number)
plt.plot(x,y1) # choosing plot variables for x and y axes
plt.title('Sample Plots for Lab 1') # title for entire figure
# (all three subplots)
plt.ylabel('Subplot 1') # label for subplot 1
plt.grid(True) # show grid on plot

plt.subplot (3,1,2) # subplot 2
plt.plot(x,y2)
plt.ylabel('Subplot 2') # label for subplot 2
plt.grid(which='both') # use major and minor grids
# (minor grids not available
# since plot is small)

plt.subplot (3,1,3) # subplot 3
plt.plot(x,y1 ,'--r',label='y1')
plt.plot(x,y2 ,'o',label='y2') # plotting both functions on one plot
plt.axis ([-2.5, 2.5, -0.5, 4.5]) # define axis
plt.grid(True)
plt.legend(loc='lower right') # prints a legend on the plot
plt.xlabel('x') # x-axis label for all three subplots (entire figure)
plt.ylabel('Subplot 3') # label for subplot 3
plt.show() ### --- This MUST be included to view your plots! --- ###