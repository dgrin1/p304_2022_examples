import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#make grid
x = np.arange(-5,5,0.2)
y = np.arange(-5,5,0.2)
z = np.arange(-5,5,0.2)

#define derivative function
def grad(f):
    gx = np.zeros_like(f)
    gy = np.zeros_like(f)
    gz = np.zeros_like(f)
    for n in range(1,len(x)-1):
        for m in range(1,len(y)-1):
            for k in range(1,len(z)-1):
#Two-point finite difference rule
                gx[n,m,k] = (T[n+1,m,k]-T[n-1,m,k])/(x[n+1]-x[n-1]);
                gy[n,m,k] = (T[n,m+1,k]-T[n,m-1,k])/(y[m+1]-y[m-1]);
                gz[n,m,k] = (T[n,m,k+1]-T[n,m,k-1])/(z[k+1]-z[k-1]);
    return gx, gy, gz

T = np.zeros((len(x), len(y), len(z)))

#Compute a potential function
for n in range(len(x)):
    for m in range(len(y)):
        for k in range(len(z)):
        	T[n,m,k] = np.sin((x[n] - y[m])/3.0) + 0.3*np.cos(y[m]) + z[k]**2

        	#T[n,m,k] = (x[n]**2-y[n]**2)
        #	T[n,m,k]=np.sin((x[n] - y[m])/3.0) + 0.3*np.cos(y[m]) + z[k]**2

gx,gy,gz = grad(T)
fig, ax = plt.subplots(figsize =(6, 6))

#2d Grid
Y, X= np.meshgrid(y,x)

#define bounds
ax.axis([-5, 5, -5, 5])

#make contour plot
ax.contour(Y, X, T[:,:,round(len(z)/2)], 64)

#Make vector plot
ax.quiver(Y, X, 10000000*gy[:,:,round(len(z)/2)], 10000000*gx[:,:,round(len(z)/2)])

#plt.colorbar()
plt.show()
