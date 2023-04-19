import numpy as np
from scipy.interpolate import interp1d,lagrange
import matplotlib.pyplot as plt

cdata = np.loadtxt('starling_scalcls.txt', float)

ls = cdata[:,0]
#print(cdata[0:199,0])


#make coarsely sampled x array
#x=np.linspace(0,18,num=20,endpoint=True)
x = np.linspace(0,2198,num=50,dtype=int)

#real function values
#y=np.cos(-x**2/9)
y = []
for i in x:
	y.append(cdata[i,1])

#linear interpolation
f=interp1d(x,y)
#cubic spline interpolation
f2=interp1d(x,y,kind='cubic')

#Lagrange interpolation
poly = lagrange(x,y)
#from numpy.polynomial.polynomial import Polynomial
#Polynomial(poly.coef[::-1]).coef


#true function values on dense array
#xnew=np.linspace(0,18,num=400001,endpoint=True)
xnew = np.linspace(0,2198,num=200,dtype=int)

#ynew=np.cos(-xnew**2/9)
ynew = []
for i in xnew:
	ynew.append(cdata[i,1])

#plt.ion()

def derv_est(x,xnext):
	dx = (f2(xnext)-f2(x))/(xnext-x)	
	return dx  

dxs = []
for i in range(200):
	if i+1<200:
		dxs.append(derv_est(xnew[i],xnew[i+1]))
	else:
		dxs.append(derv_est(xnew[i],xnew[i]))

plt.subplot(1,2,2)
plt.plot(xnew,dxs, label = "derivative")
plt.legend(loc=1)


#other plots
plt.subplot(1,2,1)
plt.plot(x,y,'k^',label='Samples')
plt.plot(xnew,ynew,'k--',label='True Theory')
plt.plot(xnew,f(xnew),':',label='Linear Interpolation')
plt.plot(xnew,f2(xnew),color='green',markersize=1,label='Cubic Splines')
#plt.xlim([0,10])
#plt.ylim([2.0*min(ynew),2.0*max(ynew)])
#plt.plot(xnew,poly(xnew),color='red',markersize=1,label='Lagrange')
#plt.xlim([0,max(xnew)])
plt.ylim([0,8000])

plt.legend(loc=1)
plt.show()
