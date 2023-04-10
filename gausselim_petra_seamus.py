import numpy as np
from numpy.linalg import inv,solve
from numpy import copy,dot
#
A = np.array([[ 0,  1,  4,  1 ],
            [ 3,  4, -1, -1 ],
            [ 1, -4,  1,  5 ],
            [ 2, -2,  1,  3 ]], float)
v = np.array([ -4, 3, 9, 7 ],float)
var_array = np.arange(1, len(v)+1, 1)
N = len(v)




# A = array([[ 4,  -1, -1,  -1 ],
#            [ -1,  3, 0, -1 ],
#            [ -1, 0,  3,  -1 ],
#            [ -1, -1,  -1,  4 ]], float)
# v = array([ 5, 0, 5, 0 ],float)
# N = len(v)


B=copy(A)
vold=copy(v)

def pivot(A, v, vars, m):
    A_m = np.copy(A[m,:]) # get row in need of swapping
    pivot_row_num = np.argmax(A[:,m]) # get index of row to swap WITH
    A_pivot = A[pivot_row_num,:] # get row to swap WITH
    A[m,:] = A_pivot  # make the swap
    A[pivot_row_num,:] = A_m
    v_m, v_piv = v[m], v[pivot_row_num] # swap the vector
    v[m], v[pivot_row_num] = v_piv, v_m
    vars_m, vars_piv = vars[m], vars[pivot_row_num] # swap the variable tags
    vars[m], vars[pivot_row_num] = vars_piv, vars_m
    return A, v, vars



# Gaussian elimination
for m in range(N):
    # Divide by the diagonal element
    if A[m,m] == 0:
        A, v, var_array = pivot(A, v, var_array, m)
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    # Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]
    
# Backsubstitution
x = np.empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

var_array, x = zip(*sorted(zip(var_array, x)))  # this sorting solution found at
# https://stackoverflow.com/questions/9764298/given-parallel-lists-how-can-i-sort-one-while-permuting-rearranging-the-other
print(x)
print(var_array)


