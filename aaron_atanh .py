from math import tanh,cosh
from numpy import linspace
from pylab import plot,show

accuracy = 1e-12

def arctanh(u):
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        delta = (tanh(x)-u)*cosh(x)**2
        x -= delta
    return x

upoints = linspace(-0.99,0.99,100)
xpoints = []
for u in upoints:
    xpoints.append(arctanh(u))
plot(upoints,xpoints)
show()


initial_guess = 0.5 

def newtonRaph(function,initial_guess,h):
	print(initial_guess)
	fx = function(initial_guess)
	fxprime = (function(initial_guess+h)-function(initial_guess))/h
	updated_guess = initial_guess -fx/fxprime
	if abs(updated_guess-initial_guess)<10e-12:
		return updated_guess
	else:
		return newtonRaph(function,updated_guess,h)
	
zero = newtonRaph(arctanh, initial_guess, 0.01) 
print(zero)
