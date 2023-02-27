# Author: Seamus Flannery
# Run this file from the command line, all functions are called in the executable.
# converts two x and y coordinate points to polar points and adds them
import numpy as np
import sys

r=input("How far away is the point of interest?")
theta=input("What is the angle?")

x=float(r)*np.cos(float(theta))
y=float(r)*np.sin(float(theta))
print("x=",x,"and y=",y)

r2=input("How far away is the second point of interest?")
theta2=input("What is the second angle?")

x2 = float(r2)*np.cos(float(theta2))
y2 = float(r2)*np.sin(float(theta2))
x=x+x2
y=y+y2

print("The combined vector is x=",x,"and y=",y)
