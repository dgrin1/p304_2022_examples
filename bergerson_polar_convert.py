import numpy as np


r=input("How far away is the point of interest?")
theta=input("What is the angle?")

x=float(r)*np.cos(float(theta))
y=float(r)*np.sin(float(theta))

print(f"The x and y coordinates in the form (x,y) is ({x},{y}))