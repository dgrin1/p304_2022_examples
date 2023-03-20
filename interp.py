from scipy.interpolate import interp1d,lagrange
import numpy as np
#make coarsely sampled x array
x=np.linspace(0,18,num=20,endpoint=True)
#real function values
y=np.cos(-x**2/9)
#linear interpolation
f=interp1d(x,y)
#cubic spline interpolation
f2=interp1d(x,y,kind='cubic')

#Lagrange interpolation
poly = lagrange(x,y)
#from numpy.polynomial.polynomial import Polynomial
#Polynomial(poly.coef[::-1]).coef



#true function values on dense array
xnew=np.linspace(0,18,num=400001,endpoint=True)
ynew=np.cos(-xnew**2/9)
import matplotlib.pyplot as plt
#plt.ion()

#other plots
plt.plot(x,y,'k^',label='Samples')
plt.plot(xnew,ynew,'k--',label='True Theory')
plt.plot(xnew,f(xnew),':',label='Linear Interpolation')
plt.plot(xnew,f2(xnew),color='green',markersize=1,label='Cubic Splines')
plt.xlim([0,10])
plt.ylim([2.0*min(ynew),2.0*max(ynew)])
plt.plot(xnew,poly(xnew),color='red',markersize=1,label='Lagrange')

plt.legend(loc=3)
plt.show()
