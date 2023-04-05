from numpy import array,empty,matmul
from numpy import size
from numpy.linalg import inv,solve
from numpy import copy,dot
#
A = array([[ 0,  1,  4,  1 ],
            [ 3,  4, -1, -1 ],
            [ 1, -4,  1,  5 ],
            [ 2, -2,  1,  3 ]], float)
v = array([ -4, 3, 9, 7 ],float)
N = len(v)

largestValue=0
largestRow=0

#for each diagonal element equal to 0
for m in range(v.size):
    if A[m,m]==0:

        #save the row and value of the highest element in that column
        for n in range(v.size):
            value=A[n,m]
            if value>largestValue:
                largestValue=value
                largestRow=n

        #swap row m and row largestRow 
        for n in range(v.size):
            tempValue=A[m,n]
            A[m,n]=A[largestRow,n]
            A[largestRow,n]=tempValue

        #reset for loop in case a new diagonal element equal to 0 is now above the row we are checking
        m=0

B=copy(A)
vold=copy(v)

#A = array([[ 4,  -1, -1,  -1 ],
#           [ -1,  3, 0, -1 ],
#           [ -1, 0,  3,  -1 ],
#           [ -1, -1,  -1,  4 ]], float)
#v = array([ 5, 0, 5, 0 ],float)
#N = len(v)

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
print(matmul(inv(A),v))
