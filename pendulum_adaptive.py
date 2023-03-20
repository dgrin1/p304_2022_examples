from math import sin,pi
from numpy import array,arange, copy,abs,sqrt
import matplotlib.pyplot as plt
g=9.81
l=0.1
om0=sqrt(g/l)
f=om0/(2.e0*pi)
T=1./f
#print(T)

#Same old equation of poin
def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta,fomega],float)
#Initial values and initial step size
a = 0.0
b = T*20
N = 1000
h0 = (b-a)/N
h=h0
i=0
t=a
delta=1.e-3

#points
thetapoints = []
omegapoints = []
tpoints=[]
dxarr=[] #error array

#arrays for different guesses
r = array([3.0,0.0],float)
r1= copy(r)
r2= copy(r)

#grab first value
thetapoints.append(r[0])
omegapoints.append(r[1])
tpoints.append(t)
dxarr.append(0)

while t<b: #condition on time
	i+=1 #increment to count steps
	#RK4 used throughout
	#One large step
	k1 = 2.*h*f(r,t)
	k2 = 2.*h*f(r+0.5*k1,t+h)
	k3 = 2.*h*f(r+0.5*k2,t+h)
	k4 = 2.*h*f(r+k3,t+2*h)
	r1 += (k1+2*k2+2*k3+k4)/6
	# Two small steps
	
	k1 = h*f(r,t)
	k2 = h*f(r+0.5*k1,t+0.5*h)
	k3 = h*f(r+0.5*k2,t+0.5*h)
	k4 = h*f(r+k3,t+h)
	r2 += (k1+2*k2+2*k3+k4)/6
	
	k1 = h*f(r2,t)
	k2 = h*f(r2+0.5*k1,t+0.5*h)
	k3 = h*f(r2+0.5*k2,t+0.5*h)
	k4 = h*f(r2+k3,t+h)
	r2 += (k1+2*k2+2*k3+k4)/6

	#Calculate rho value and assess error
	dx=r1[0]-r2[0]
	rho=30.*h*delta/abs(dx)
#	print(t,rho,delta,h,dx,r1[0],r2[0])
	#adjust step size
	if rho>=1.0:
		t+=2*h
		h*=min(rho**0.25,1.001)
		r=r2
		thetapoints.append(r[0])
		omegapoints.append(r[1])
		tpoints.append(t)
		dxarr.append(dx)
	else:
		h*=rho**0.25

#make a nice plot
print(i,max(abs(dxarr)))
plt.figure(2)
plt.plot(tpoints,thetapoints,'k.')
plt.xlabel("t")
plt.xlim([0,20*T])
plt.ylim([-4,4])
#plt.ion()
plt.show()
