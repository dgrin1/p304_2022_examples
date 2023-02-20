import numpy as np
import matplotlib.pyplot as plt


"""Simpon's Rule"""

def f(x):
    return x



def simp(a, b, N):
    h = (b-a)/N    # define h
    oddsum = 0   # sum of odd terms
    evensum = 0   # sum of even terms
    for k in range(1,(N),2):   # for loop for summation
        oddsum += f(a+k*h)
    for k in range(0,N+1,2):    # for loop for summation
        evensum += f(a+k*h)
    return (h/3)*(f(a)+4*oddsum+2*evensum)   # return the def of Simpson's rule

print(simp(0,4, 150))

