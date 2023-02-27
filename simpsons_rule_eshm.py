'''
Enter the formula for the integrand in line 9; the lower and upper limits of integration in lines 11 and 12, respectively;
and the desired value for N sample points in line 13
'''

import numpy as np

def f(theta): #defining nested function that does calculations of integrand, to be used for Simpson's rule
    f=np.cos(m*theta-x*theta) #ENTER INTEGRAND HERE
    return(f) #returns the value of the integrand when f is called in Simpson's rule below
a=0 #ENTER LOWER LIMIT OF INTEGRATION HERE
b=np.pi #ENTER UPPER LIMIT OF INTEGRATION HERE
N=1000 #ENTER NUMBER OF SLICES OVER WHICH TO INTEGRATE HERE
h=(b-a)/N #defining the width of slices to be a 1000th of the total range of integration, making the slices smaller and thus increasing the accuracy of the estimate
odd_terms=[] #defining empty array for the odd terms to be added to each time through the for loop
for k in range(1,N,2): #using for loop to store, in the variable "odd", the term in Simpson's rule with a sum over odd values
    odd=f(a+k*h) #calls the function f(theta) that stores the integrand, using it in the sum
    odd_terms.append(odd) #adds most recently calculated value of f(x) to the empty array of odd terms
odd_sum=sum(odd_terms) #calculating the sum of the now-populated array of odd terms calculated using the for loop above
even_terms = []  #defining empty array for the even terms to be added to each time through the for loop
for k in range(2,N,2):  #using for loop to store, in the variable "even", the term in Simpson's rule with a sum over even values
    even=f(a+k*h)  #calls the function f(theta) that stores the integrand, using it in the sum
    even_terms.append(even)  #adds most recently calculated value of f(x) to the empty array of even terms
even_sum=sum(even_terms)  #calculating the sum of the now-populated array of even terms calculated using the for loop above
Integral_=(1/3)*h*(f(a)+f(b)+4*odd_sum+2*even_sum) #calculating Simpson's rule where we integrate from x=a to x=b for given function f(x) (f(x)=J_m),
#where h=width of slices we're fitting quadratic to and integrating over.
print(Integral_)


