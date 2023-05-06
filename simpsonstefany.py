import numpy as np

def f(x):
    # Define the function to integrate
    return np.sin(x)

def simpson_rule(f, a, b, n):
    # Implement Simpson's rule
    h = (b - a) / n
    sum_odd = 0
    sum_even = 0
    
    # Calculate sum of f(x) at even and odd indices
    for i in range(1, n, 2):
        sum_odd += f(a + i * h)
    for i in range(2, n, 2):
        sum_even += f(a + i * h)
        
    integral = (1 / 3) * h * (f(a) + f(b) + 4 * sum_odd + 2 * sum_even)
    return integral

# Test the function with the sine function from 0 to pi
a = 0
b = np.pi
n = 100
integral = simpson_rule(f, a, b, n)
print("The approximate integral of sin(x) from 0 to pi is:", integral)
