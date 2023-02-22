from __future__ import division,print_function
#from scipy import constants as sc
from numpy import loadtxt,array,dot,sqrt,cos,sin,linspace,log
import numpy as np
from math import pi

import matplotlib.pyplot as plt
plt.ion()
data=loadtxt("stars.txt",float)
x=data[:,0]
y=data[:,1]
xbetter=[]
ybetter=[]

nstarsm1=np.size(x)

for i in range(0,nstarsm1):
	if y[i] <= 10:
		xbetter.append(x[i])
		ybetter.append(y[i])

subs=range(0,nstarsm1,5)
xsubs=x[subs]
ysubs=y[subs]

plt.scatter(xbetter,ybetter)
plt.scatter(xsubs,ysubs,c="r")
#sctter needs c=
plt.show()
plt.xlabel("Temperature in K")
plt.ylabel("Magnitude")
plt.xlim(0,13000)
plt.ylim(-5,20)
