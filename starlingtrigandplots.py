import numpy as np
import matplotlib.pyplot as plt

Nmax=65

	
def mysin(x):
	sum=0
	#Big loop up to Nmax
	for n in range(0,Nmax+1):
		answer=((-1)**n)*np.power(x,2*n+1)/factorial(2*n+1) #taylor series, calls factorial function		
		sum+=answer
	return sum


def mycos(x):
	sum=0
	#Big loop up to Nmax
	for n in range(0,Nmax+1):
		answer=((-1)**n)*np.power(x,2*n)/factorial(2*n) #taylor series, calls factorial function
		sum+=answer
	return sum
	
def mytan(x):
	tan = mysin(x)/mycos(x)
	return tan
	
def mycsc(x):
	cosec = 1/mysin(x)
	return cosec

def mysec(x):
	sec = 1/mycos(x)
	return sec

def mycot(x):
	#cot = 1/mytan(x)
	cot = mycos(x)/mysin(x)
	return cot
	
def factorial(x):
	if(x==1):	
		fac=1
	elif(x==0):	
		fac=1
	else:
		fac=x*factorial(x-1)
	return fac	

x=np.linspace(0,2*np.pi,100)
ysin = []
for i in range(100):
	ysin.append(mysin(x[i]))

ycos = []
for i in range(100):
	ycos.append(mycos(x[i]))

ytan = []
for i in range(100):
	ytan.append(mytan(x[i]))

ysec = []
for i in range(100):
	ysec.append(mysec(x[i]))
	
ycot = []
for i in range(100):
	ycot.append(mycot(x[i]))
	
ycsc = []
for i in range(100):
	ycsc.append(mycsc(x[i]))


plt.subplot(321)
plt.plot(x,ysin)

plt.subplot(322)
plt.plot(x,ycos)

plt.subplot(323)
plt.scatter(x,ytan)
plt.ylim(10,-10)

plt.subplot(324)
plt.scatter(x,ysec)
plt.ylim(10,-10)

plt.subplot(325)
plt.scatter(x,ycot)
plt.ylim(10,-10)

plt.subplot(326)
plt.scatter(x,ycsc)
plt.ylim(10,-10)
plt.show()






