from math import tanh,cosh
from numpy import linspace
from pylab import plot,show

accuracy = 1e-16

def arctanh(u):
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        delta = (tanh(x)-u)*cosh(x)**2
        x -= delta
    return x

# upoints = linspace(-0.99,0.99,100)
# xpoints = []
# for u in upoints:
#     xpoints.append(arctanh(u))
# plot(upoints,xpoints)
# show()

a=0
b=100
x = 0.3
N = 300
h = (b-a)/N

while arctanh(x)>accuracy:
	df=(arctanh(x+h)-arctanh(x))/h
	x=x-arctanh(x)/df
print(x)