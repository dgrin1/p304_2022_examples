from __future__ import division,print_function
from petratriglib2 import tan, sin, cos, csec, sec, cot


from scipy import constants as sc
from numpy import linspace,log
import numpy as np
from math import pi

import matplotlib.pyplot as plt

def error(x,Nmax):
	err=np.divide(sin(x,2*Nmax)-sin(x,Nmax),sin(x,Nmax))
	return err
N=[]
Elist=[]
errs=[]
for j in range (1,30):
	N.append(j)
	for i in linspace(0.1,np.pi/2,1000):

		errs.append(error(i,j))
	E=np.average(errs)
	Elist.append(E)
#print(errs)

plt.rc('text',usetex=True)
plt.rc('font', family='serif',serif='Palatino')

plt.plot(np.log10(N),np.log10(Elist), 'g-')





# plt.ylabel('y-axis', fontsize=20)
# #plt.xlabel('x-axis', fontsize=20)
# plt.ylabel(r'$~f(\theta)$')

# plt.ylabel('f(', r'$~\theta t$',')',fontsize=24)
# plt.xlabel(r'$~\theta$',fontsize=16)
# plt.savefig('sintest.pdf',format='pdf',dpi=1000)

plt.show()