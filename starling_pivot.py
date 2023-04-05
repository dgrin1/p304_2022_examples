from numpy import array,empty
from numpy.linalg import inv,solve
from numpy import copy,dot
#
"""
A = array([[ 2,  1,  4,  1 ],
            [ 3,  4, -1, -1 ],
            [ 1, -4,  1,  5 ],
            [ 2, -2,  1,  3 ]], float)
v = array([ -4, 3, 9, 7 ],float)
N = len(v)
"""

A = array([[ 0,  1,  4,  1 ],
           [ 3,  4, -1, -1 ],
           [ 1, -4,  1,  5 ],
           [ 2, -2,  1,  3 ]], float)
v = array([ -4, 3, 9, 7 ],float)
N = len(v)

# A = array([[ 4,  -1, -1,  -1 ],
#            [ -1,  3, 0, -1 ],
#            [ -1, 0,  3,  -1 ],
#            [ -1, -1,  -1,  4 ]], float)
# v = array([ 5, 0, 5, 0 ],float)
# N = len(v)


B=copy(A)
vold=copy(v)



# Gaussian elimination
for m in range(N):
	
	if A[m,m] == 0: # pivoting code
		for i in range(N):
			large = A[m,m] # keep track of largest val
			if abs(A[i,m]) > large: # find row w/ largest abs val
				large = A[i,m]
				pivrow = i # keeps track of which row has largest abs val of m
		for i in range(N):
			A[m,i], A[pivrow,i] = A[pivrow,i], A[m,i] # swap matrix rows
		v[m], v[pivrow] = v[pivrow], v[m] # swap vector rows
			

    # Divide by the diagonal element
	div = A[m,m]
	A[m,:] /= div
	v[m] /= div

    # Now subtract from the lower rows
	for i in range(m+1,N):
		mult = A[i,m]
		A[i,:] -= mult*A[m,:]
		v[i] -= mult*v[m]
    
# Backsubstitution
x = empty(N,float)
for m in range(N-1,-1,-1):
	x[m] = v[m]
	for i in range(m+1,N):
		x[m] -= A[m,i]*x[i]

print("my alg: ",x)
print("numpy: ",solve(B,vold))
