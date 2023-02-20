from scipy import constants as constants
import numpy as np
from gaussxw import gaussxw,gaussxwab

#new gaussian integral stuff

#Define number of points and limits
N=50

epsilon=1.e-10
#start integral close to x=0 because integrand still dierges
a=epsilon
b=1.-epsilon

#make an integer range covering # of points


#define function
def f(x):
    import numpy as np
    f=(x**3)*np.exp(-x)/(1.-np.exp(-x))
#    print(x,f)
    return f   

#integrand with chang eof variables that is good to infinity
def g(z):
    import numpy as np
    x=z/(1.-z)
    g=(x**3)*np.exp(-x)/((1.-np.exp(-x))*(1.-z)**2)
#    print(x,f)
    return g

#trapiezoidal rule function
#Syntax limits, function, Number of points
def trape(a,b,f,N):
#stepsize
	h=(b-a)/N
#End points
	s=(f(a)+f(b))*h
#Accumulate and normal sum by simpson formula
	for i in range(1,N):
		s+=2.*f(a+i*h)*h

	s/=2.0
	return s

#Call trapezoidal function to get integral estimate
#trape(a,b,f,N)

#compare with riemann sum, using both terms in thermal integral
s=(trape(a,1,f,N)+trape(1/2,b,g,N))
stefan=s*(constants.Boltzmann**4.e0)/(4.*(np.pi*constants.speed_of_light)**2.e0*(constants.hbar**3.))
Nold=N
N*=2
s=(trape(a,1,f,N)+trape(1/2,b,g,N))
stefan_better=s*(constants.Boltzmann**4.e0)/(4.*(np.pi*constants.speed_of_light)**2.e0*(constants.hbar**3.))
error=(stefan_better-stefan)/stefan
print(stefan,error)

#New stuff for gaussian integrals
xvals,wp=gaussxwab(Nold,a,1)
s=0
for k in range(Nold):
    s += wp[k]*f(xvals[k])
xvals,wp=gaussxwab(Nold,1/2,b)
#s = 0.0
for k in range(Nold):
    s += wp[k]*g(xvals[k])
stefan_gauss=s*(constants.Boltzmann**4.e0)/(4.*(np.pi*constants.speed_of_light)**2.e0*(constants.hbar**3.))
print(stefan_gauss)









