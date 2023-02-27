import numpy as np
import matplotlib.pyplot as pyplot

def f(x):
    return np.sin(x)

N = 1000

def sim(a,b,N):
    a = 0
    b = np.pi
    h = (a-b)/N
    tot = f(a)+f(b)
    for i in range(1,N):
        t = a+i*h
        if i%2==1:
            tot += 4*f(t)
        else:
            tot += 2*f(t)
    simpson = tot*(h/3)
    return simpson

print(sim(0,np.pi,50))
