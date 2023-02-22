import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**4 - 2*x + 1

# lets integrate btwn 0 and 2 so a = 0 and b = 2

N = 3

def simpson(a,b,N):
    sumodd = 0
    sumeven = 0
    h = (b-a)/N
    for k in range(1, N, 2):
        sumodd += f(a+k*h)
    for k in range(2,N,2):
        sumeven += f(a+k*h)
    Ifunc = (h/3)*(f(a) + f(b) + 4*sumodd + 2*sumeven)
    return Ifunc

print(simpson(0,2,10))