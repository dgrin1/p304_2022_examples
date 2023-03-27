from numpy import array,empty
from numpy.linalg import inv,solve
from numpy import copy,dot
#
A = array([[ 2,  1,  4,  1 ],
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

print(x)
