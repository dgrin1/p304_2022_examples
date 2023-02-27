import matplotlib.pyplot as plt
import numpy as np
x=0.3
Nmax=25

def factorial(x):
  if(x==0 or x==1):
    fac=1
  else:
    fac=x*factorial(x-1)
  return fac

def sin_sl(x,Nmax):
    sumsin=0
#loop up to Nmax
    for n in range(0,Nmax+1):
        #print(n)
        numsin=((-1)**n)*(x**(2*n+1)) #taylor series numerator
        #sum+=term
        int_want_sin=2*n+1 #determine integer whose factorial we want
        #print(int_want)
        #factorial=1
        #for j in range(int_want,0,-1): #write downward running loop that gets from factorial target to 1
            #factorial=factorial*j
        #print(n,int_want,factorial)
        denomsin=factorial(int_want_sin)
        termsin=numsin/denomsin
        sumsin+=termsin
        #print(n,factorial)
    return sumsin

def cos_sl(x,Nmax):
    sumcos=0
    for n in range(0,Nmax+1):
        numcos=((-1)**n)*(x**(2*n))
        int_want_cos=2*n
        denomcos=factorial(int_want_cos)
        termcos=numcos/denomcos
        sumcos+=termcos
    return sumcos

def tan_sl(x,Nmax):
    termtan=sin_sl(x,Nmax)/cos_sl(x,Nmax)
    return termtan

def csc_sl(x,Nmax):
    termcsc=1/sin_sl(x,Nmax)
    return termcsc

def sec_sl(x,Nmax):
    termsec=1/cos_sl(x,Nmax)
    return termsec

def cot_sl(x,Nmax):
    termcot=cos_sl(x,Nmax)/sin_sl(x,Nmax)
    return termcot

ysin=[]
ycos=[]
ytan=[]
ycsc=[]
ysec=[]
ycot=[]

xaxis=np.linspace(0,2*np.pi)
for i in xaxis:
    ysin.append(sin_sl(i,Nmax))
    ycos.append(cos_sl(i,Nmax))
    ytan.append(tan_sl(i,Nmax))
    ycsc.append(csc_sl(i,Nmax))
    ysec.append(sec_sl(i,Nmax))
    ycot.append(cot_sl(i,Nmax))

plt.subplot(322)
plt.plot(xaxis,ycsc,'r')
plt.xlabel("x")
plt.ylim([-20,20])
plt.ylabel("y")
plt.title("csc(x)")

plt.subplot(323)
plt.plot(xaxis,ycos,'r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("cos(x)")

plt.subplot(324)
plt.plot(xaxis,ysec,'r')
plt.xlabel("x")
plt.ylim([-20,20])
plt.ylabel("y")
plt.title("sec(x)")

plt.subplot(325)
plt.plot(xaxis,ytan,'r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("tan(x)")

plt.subplot(326)
plt.plot(xaxis,ycot,'r')
plt.xlabel("x")
plt.ylim([-20,20])
plt.ylabel("y")
plt.title("cot(x)")

plt.show()
plt.close()

def E(x,Nmax):
    fmax=sin_sl(x,Nmax)
    f2max=sin_sl(x,2*Nmax)
    Enum=np.abs((f2max-fmax)/sin_sl(x,Nmax))
x=np.linspace(0,2*np.pi)

n_values=[]

for i in range(np.size(x)):
    n_values.append(Enum(i,Nmax))
np.mean(n_values)
