# this is a trapezoidal integration function of N "blocks" from a to b

# the function we want to integrate over
def f(x):
    y = x**2
    return y

# trapezoidal integration
def trap(a, b, f, N):
    h = (b - a) / N
    sum = (f(a) + f(b)) * h
    # sum over all points
    for i in range(1, N):
        sum += 2. * f(a + i * h) * h  # add intermediate points
    sum /= 2.0
    return sum
