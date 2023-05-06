import numpy as np
import math

x = float(input('x = ')) % (2.0 * np.pi)
s = 0.0
for i in range(1000):
    term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    s_old = s
    s += term
    if s == s_old:
        break
print("Sine of x is: ",s)

    

