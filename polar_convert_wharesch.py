import numpy as np

x=input("How far away is the point of interest in the x direction?")
y=input("How far away is the point of interest in the y direction?")

r=np.sqrt(float(x)**2 + float(y)**2)
theta=np.arctan(x/y)
print("r=",r,"and theta=",theta)
