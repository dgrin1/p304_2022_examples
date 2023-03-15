import numpy as np
import matplotlib.pyplot as plt

def iteration(x0):
    if abs(f(x0))>0.0001:
        return iteration(x0-f(x0)/derivative(x0))
    else:
        print("This function reaches 0 at "+str(x0))

def f(x):
    return np.cos(x)-np.exp(x)

def derivative(x):
    return -np.sin(x)-np.exp(x)

#0s are at x=0 and x~-1.29 then recurring negative values, and the maximum between the two rightmost 0s is at ~-0.55, so try values on either side of peak to find 0s
iteration(-20)

xrange=np.linspace(-21,1,500)
frange=[]

for i in np.linspace(-21,1,500):
    frange.append(f(i))

plt.plot(xrange,frange)
plt.show()
