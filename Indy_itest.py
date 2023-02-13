from __future__ import print_function, division
import numpy as np

# A 60 m climbing rope is hanging over the side of a tall cliff.
# How much work is performed in pulling the rope up to the top, where the rope has a mass of 66 g/m?


N = 100
a = 0
b = 60
g = 9.8 #m/s
m = 0.066 #kg

ivec = range(0, N + 1)
s = 0
x = 0
h = float(b - a) / float(N)


def f(x):
    f = m * g * (60 - x)  # np.power(x, 4.e0) - 2. * x + 1.
    return f


for i in ivec:
    s += f(x) * h
    x = a + i * h


def trape(a, b, f, N):
    h = (b - a) / N
    s = (f(a) + f(b)) * h
    for i in range(1, N):
        s += 2. * f(a + i * h) * h
    s /= 2.0
    return s


trape(a, b, f, N)

print(s, trape(a, b, f, N))
print("The work done is", trape(a,b,f,N), "J")