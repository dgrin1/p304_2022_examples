import aaronTrigLib as atl
import numpy as np
import matplotlib.pyplot as plt

t = np.transpose(np.arange(-2*np.pi,2*np.pi,0.01))
#print(t)

#sinDat = list(map(atl.sin,t))
sinDat = [atl.sin(tt) for tt in t]
cosDat = [atl.cos(tt) for tt in t]
tanDat = atl.tan(t)
cscDat = atl.csc(t)
secDat = atl.sec(t)
cotDat = atl.cot(t)
plt.figure(1)
plt.subplot(121)
plt.plot(t,sinDat,label = "Sine")
plt.plot(t,cosDat, label = "Cosine")
#plt.plot(t,tanDat)
#plt.plot(t,cscDat)
#plt.plot(t,secDat)
#plt.plot(t,cotDat)
plt.xlabel("Sin, Cos functions")
plt.ylabel("Number")
plt.xlim(0,2*np.pi)
plt.ylim(-1.2,1.2)
plt.legend()
plt.subplot(122)
plt.plot(t,tanDat,label = "Tangent")
plt.plot(t,cscDat, label = "Cosecant")
plt.plot(t,secDat, label = "Secant")
plt.plot(t,cotDat, label = "Cotangent")
plt.xlim(0,2*np.pi)
plt.ylim(-20,20)
plt.legend()
plt.xlabel("Tan, Csc, Sec, and Cot functions")
plt.show()
