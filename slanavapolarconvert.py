import numpy as np

r=input("how far away is the point of interest")
theta=input("what is the angle")

x=r*np.cos(np.float(theta))
y=r*np.sin(np.float(theta))

print('x=',x,"and y=",y)
