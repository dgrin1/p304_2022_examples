import aaronTrigLib as atl
import numpy as np
import matplotlib.pyplot as plt

def errorCalc(standardFunc,testFunc): # create function to create functions that calculate error
	return lambda x, term: abs((standardFunc(x,2*term)-testFunc(x,term))/standardFunc(x,term))

# Create the error comparisons for every function I have in my trig library 
testSin = errorCalc(atl.sin,atl.sin)
testCos = errorCalc(atl.cos,atl.cos)
testTan = errorCalc(atl.tan,atl.tan)
testCsc = errorCalc(atl.csc,atl.csc)
testSec = errorCalc(atl.sec,atl.sec)
testCot = errorCalc(atl.cot,atl.cot)

# create the points to evalueate my finctions at. 
t = np.transpose(np.arange(-2*np.pi,2*np.pi,1))
print(t)
# create function that finds the maximum error in
def findMaxErr(t,terms):
	maxErrIndex = 0
	errors = testSin(t,terms)
	maxErrIndex = errors.index(max(errors))
	return maxErrIndex

print(testSin(np.pi,2))

error = [0.]*len(t)
#print(error)
maxN = np.zeros_like(np.arange(1,5),dtype=float)

print(maxN)
for n,N in enumerate(maxN):
	for i,x in enumerate(t):
		error[i] = testSin(x,n+1)
	print(error)
	#print(maxN)
	maxN[n] = max(error)
		
plt.plot(np.arange(1,5),maxN)
plt.show()
	# generate list of errors for each N. 2*N comparison 



	# pick the biggest error for each N 2*N compariosn 


#increase N

