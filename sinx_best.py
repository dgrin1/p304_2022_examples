import numpy as np
import math

#read in x and compute it modulo 2*pi, so argument of sine is always moderate
x = float(input('x = '))%(2.e0*np.pi)

#initialize iterator and sum
i = 0
s,sold = 0.e0,0.e0

#Keep at most 1000 terms in the Taylor series
while i<1000:
    #save last estimate
    sold= s
    #add next term in taylor series
    s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
    #iterate index
    i += 1
    #if sum has converged to machine precision set iterator well beyond its max to exist loop
    #in the while implementation this avoids breaking the factorial function with huge number
    if sold == s: i=1000000
print s
    

