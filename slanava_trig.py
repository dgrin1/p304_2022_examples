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

def sin_sl(x):
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

def cos_sl(x):
    sumcos=0
    for n in range(0,Nmax+1):
        numcos=((-1)**n)*(x**(2*n))
        int_want_cos=2*n
        denomcos=factorial(int_want_cos)
        termcos=numcos/denomcos
        sumcos+=termcos
    return sumcos

def tan_sl(x):
    termtan=sin_sl(x)/cos_sl(x)
    return termtan

def csc_sl(x):
    termcsc=1/sin_sl(x)
    return termcsc

def sec_sl(x):
    termsec=1/cos_sl(x)
    return termsec

def cot_sl(x):
    termcot=cos_sl(x)/sin_sl(x)
    return termcot

ysin=[]
ycos=[]
ytan=[]
ycsc=[]
ysec=[]
ycot=[]

xaxis=np.linspace(0,2*np.pi)
for i in xaxis:
    ysin.append(sin_sl(i))
    ycos.append(cos_sl(i))
    ytan.append(tan_sl(i))
    ycsc.append(csc_sl(i))
    ysec.append(sec_sl(i))
    ycot.append(cot_sl(i))

plt.subplot(321)
plt.plot(xaxis,ysin,'r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin(x)")

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
