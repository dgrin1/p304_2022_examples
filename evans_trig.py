import numpy as np
import matplotlib.pyplot as plt

def factorial(y):
    if y == 1 or y == 0:
        return 1
    else:
        return (y*factorial(y-1))

def sin(x,N):
    sum = 0
    for n in range(0, N+1):
        num = ((-1)**n)*(x**(2*n+1))
        den = (2*n+1)
        denom = factorial(den)
        term = num/denom
        sum += term
    return sum

def cos(x,N):
    sum = 0
    for n in range(0, N+1):
        num = ((-1)**n)*(x**(2*n))
        den = (2*n)
        denom = factorial(den)
        term = num/denom
        sum += term
    return sum


def tan(x,N):
    return sin(x,N)/cos(x,N)

def sec(x,N):
    return 1/cos(x,N)

def csec(x,N):
    return 1/sin(x,N)

def cotan(x,N):
    return 1/tan(x,N)


sin_y = []
theta = np.linspace(-2*np.pi,2*np.pi, 100)
for n in theta:
    res = sin(n, 70)
    sin_y.append(res)
    
delta_sin = sin_y - np.sin(theta) 

cos_y = []
theta = np.linspace(-2*np.pi,2*np.pi, 100)
for n in theta:
    res = cos(n, 60)
    cos_y.append(res)

delta_cos = cos_y - np.cos(theta)

tan_y = []
theta = np.linspace(-2*np.pi,2*np.pi, 100)
for n in theta:
    res = tan(n, 60)
    tan_y.append(res)

delta_tan = tan_y - np.tan(theta)

csec_y = []
theta = np.linspace(-2*np.pi,2*np.pi, 100)
for n in theta:
    res = csec(n, 60)
    csec_y.append(res)

delta_csec = tan_y - np.tan(theta)

sec_y = []
theta = np.linspace(-2*np.pi,2*np.pi, 100)
for n in theta:
    res = sec(n, 60)
    sec_y.append(res)

delta_sec = tan_y - np.tan(theta)

cotan_y = []
theta = np.linspace(-2*np.pi,2*np.pi, 100)
for n in theta:
    res = cotan(n, 60)
    cotan_y.append(res)

delta_cotan = cotan_y - np.tan(theta)

"""Sin"""

plt.subplot(211)

plt.plot(theta, sin_y)


plt.subplot(212)

plt.plot(theta, delta_sin)

plt.show()

"""Cos"""

plt.subplot(211)

plt.plot(theta, cos_y)


plt.subplot(212)

plt.plot(theta, delta_cos)

plt.show()


"""Tan"""


plt.subplot(211)

plt.plot(theta, tan_y)


plt.subplot(212)

plt.plot(theta, delta_tan)

plt.show()





    
