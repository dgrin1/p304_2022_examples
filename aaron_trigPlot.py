import aaronTrigLib as atl
import numpy as np
import matplotlib.pyplot as plt

def errorCalc(standardFunc,testFunc):
	return lambda x, term: abs((standardFunc(x,term)-testFunc(x,term))/standardFunc(x,term))

testSin = errorCalc(atl.sin,atl.sin)
testCos = errorCalc(atl.cos,atl.cos)
testTan = errorCalc(atl.tan,atl.tan)
testCsc = errorCalc(atl.csc,atl.csc)
testSec = errorCalc(atl.sec,atl.sec)
testCot = errorCalc(atl.cot,atl.cot)

t = np.transpose(np.arange(-2*np.pi,2*np.pi,0.01))
#print(t)

def findMaxErr(t,terms):
	maxErrIndex = 0
	errors = testSin(t,terms)
	maxErrIndex = errors.index(max(errors))
	return maxErrIndex




sinDat = list(map(atl.sin,t))
sinDat = [atl.sin(tt,terms) for tt in t]
cosDat = [atl.cos(tt,terms) for tt in t]
tanDat = atl.tan(t,terms)
cscDat = atl.csc(t,terms)
secDat = atl.sec(t,terms)
cotDat = atl.cot(t,terms)

N_max = 50
sinErr = testSin(t,N_max)
cosErr = testCos(t,N_max)
tanErr = testTan(t,N_max)
cscErr = testCsc(t,N_max)
secErr = testSec(t,N_max)
cotErr = testCot(t,N_max)

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




plt.show()
