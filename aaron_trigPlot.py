import aaronTrigLib as atl
import numpy as np
import matplotlib.pyplot as plt

def errorCalc(standardFunc,testFunc):
	return lambda x: abs(standardFunc(x)-testFunc(x))

testSin = errorCalc(np.sin,atl.sin)
testCos = errorCalc(np.cos,atl.cos)
testTan = errorCalc(np.tan,atl.tan)

t = np.transpose(np.arange(-2*np.pi,2*np.pi,0.01))
#print(t)

#sinDat = list(map(atl.sin,t))
sinDat = [atl.sin(tt) for tt in t]
cosDat = [atl.cos(tt) for tt in t]
tanDat = atl.tan(t)
cscDat = atl.csc(t)
secDat = atl.sec(t)
cotDat = atl.cot(t)

sinErr = testSin(t)
cosErr = testCos(t)
tanErr = testTan(t)


plt.figure(1)
plt.subplot(261)
plt.plot(t,sinDat,label = "Sine")
plt.xlabel("Sin")
plt.ylabel("Number")
plt.xlim(0,2*np.pi)
plt.ylim(-1.2,1.2)
plt.subplot(262)
plt.plot(t,cosDat, label = "Cosine")
plt.xlabel("Cos")
plt.ylabel("Number")
plt.xlim(0,2*np.pi)
plt.ylim(-1.2,1.2)
plt.subplot(263)
plt.plot(t,tanDat,label = "Tangent")
plt.xlabel("Tan")
plt.ylabel("Number")
plt.xlim(0,2*np.pi)
plt.ylim(-20.2,20.2)
plt.subplot(264)
plt.plot(t,cscDat, label = "Cosecant")
plt.xlabel("Csc")
plt.ylabel("Number")
plt.xlim(0,2*np.pi)
plt.ylim(-20.2,20.2)
plt.subplot(265)
plt.plot(t,secDat, label = "Secant")
plt.xlabel("Sec")
plt.ylabel("Number")
plt.xlim(0,2*np.pi)
plt.ylim(-20.2,20.2)
plt.subplot(266)
plt.plot(t,cotDat, label = "Cotangent")
plt.xlabel("Cot")
plt.ylabel("Number")
plt.xlim(0,2*np.pi)
plt.ylim(-20.2,20.2)

plt.subplot(267)
plt.plot(t,sinErr, label = "Sin Err")
plt.xlim(0,2*np.pi)
plt.subplot(268)
plt.plot(t,cosErr, label = "Cos Err")
plt.xlim(0,2*np.pi)
plt.subplot(269)
plt.plot(t,tanErr, label = "Tan Err")
plt.xlim(0,2*np.pi)



plt.show()
