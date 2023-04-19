
# based off Riley's code from the class showcase, wanted to show through comments that I understand the material
import numpy as np
from scipy.interpolate import interp1d,lagrange
import matplotlib.pyplot as plt

cdata = np.loadtxt('/Users/jtturner/Dropbox/My Mac (Jacqueline’s MacBook Pro (3))/Downloads/Computational_Physics/jjturner_hw/camb_77426547_scalcls.dat.txt',float) #get data, nees to change the path if I want other people to run it

ls = cdata[:,0] # prints the data
#print(cdata[0:199,0])


#make coarsely sampled x array
#x=np.linspace(0,18,num=20,endpoint=True)
x = np.linspace(0,1000,num=50,dtype=int) #makes the x-arrray

#real function values
#y=np.cos(-x**2/9)
y = []
for i in x:
	y.append(cdata[i,1]) # matches the data to the array

#linear interpolation
f=interp1d(x,y)
#cubic spline interpolation
f2=interp1d(x,y,kind='cubic')

#Lagrange interpolation
poly = lagrange(x,y) #not actually used
#from numpy.polynomial.polynomial import Polynomial
#Polynomial(poly.coef[::-1]).coef


#true function values on dense array
#xnew=np.linspace(0,18,num=400001,endpoint=True)
xnew = np.linspace(0,1000,num=50,dtype=int) # the number of points seems not to affect results but this makes arrays for the graphs

#ynew=np.cos(-xnew**2/9)
ynew = []
for i in xnew: #same process as before matches the data to the array
	ynew.append(cdata[i,1])

#plt.ion()

def derv_est(x,xnext): #makes the derivative by doing cubespline/actual between each point
	dx = (f2(xnext)-f2(x))/(xnext-x)
	return dx

dxs = []
for i in range(50): #this ensures the last point has an accurate derivative
	if i+1<50:
		dxs.append(derv_est(xnew[i],xnew[i+1]))
	else:
		dxs.append(derv_est(xnew[i],xnew[i]))
#actual plot work actual fits on the left and derivative on the right
plt.subplot(1,2,2)
plt.plot(xnew,dxs, label = "derivative")
plt.legend(loc=1)
plt.title("Derivative")


#other plots
plt.subplot(1,2,1)
plt.plot(x,y,'r^',label='Samples')
plt.plot(xnew,ynew,'r--',label='True Theory')
plt.plot(xnew,f(xnew),':',label='Linear Interpolation')
plt.plot(xnew,f2(xnew),color='blue',markersize=1,label='Cubic Splines')
#plt.xlim([0,10])
#plt.ylim([2.0*min(ynew),2.0*max(ynew)])
#plt.plot(xnew,poly(xnew),color='red',markersize=1,label='Lagrange')
#plt.xlim([0,max(xnew)])
#plt.ylim([0,8000])
plt.title("actual spline fit")

plt.legend(loc=1)
plt.show()