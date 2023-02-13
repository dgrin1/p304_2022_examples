import numpy as np
import matplotlib.pyplot as plt


def factorial(x):  # fastest simple to read factorial function
    result = x
    for i in range(x-1, 1, -1):
        result = result * i
    if x == 0:
        result = 1
    return result


# written for in class-example purposes, technically slower than the loop version of
# factorial on account of the call stack
def recursive_factorial(x):
    if x == 0:
        return 1
    else:
        return x * recursive_factorial(x-1)


def sin(x, nmax=50):
    result = 0
    for n in range(nmax+1):
        result += ((-1)**n) * (x**(2*n+1)) / (factorial(2*n+1))
    return result


def cos(x, nmax=50):
    result = 0
    for n in range(nmax+1):
        result += ((-1)**n) * (x**(2*n)) / factorial(2*n)
    return result


def tan(x, nmax=50):
    return sin(x, nmax) / cos(x, nmax)


def sec(x, nmax=50):
    return 1 / cos(x, nmax)


def csc(x, nmax=50):
    return 1 / sin(x, nmax)


def cot(x, nmax=50):
    return cos(x, nmax) / sin(x, nmax)


def sinh(x, nmax=50):
    result = 0
    for n in range(nmax + 1):
        result += (x ** (2 * n + 1)) / (factorial(2 * n + 1))
    return result


def cosh(x, nmax=50):
    result = 0
    for n in range(nmax + 1):
        result += (x ** (2 * n)) / factorial(2 * n)
    return result


def tanh(x, nmax=50):
    return sinh(x, nmax)*cosh(x, nmax)


def basic_trig_plot():
    x = np.linspace(0, 10 * np.pi, 1000)
    plt.subplot(121)
    y1 = [sin(num) for num in x]
    y2 = [cos(num) for num in x]
    plt.plot(x, y1, label="sin(x)")
    plt.plot(x, y2, label="cos(x)")
    plt.ylim(-1, 1)
    plt.xlim(0, 2 * np.pi)
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.legend()
    plt.subplot(122)
    y3 = [tan(num) for num in x]
    y4 = [cot(num) for num in x]
    y5 = [csc(num) for num in x]
    y6 = [sec(num) for num in x]
    plt.plot(x, y3, label="tan(x)")
    plt.plot(x, y4, label="cot(x)")
    plt.plot(x, y5, label="csc(x)")
    plt.plot(x, y6, label="sec(x)")
    plt.ylim(-20, 20)
    plt.xlim(0, 2 * np.pi)
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.legend()
    plt.title("Trig Functions")
    plt.show()


def plot_trig_error():
    x = np.linspace(0, 10 * np.pi, 1000)
    plt.subplot(121)
    y1 = [sin(num) for num in x]
    y1err = [abs((sin(num)-np.sin(num))/sin(num)) for num in x]
    plt.errorbar(x, y1, yerr=y1err, label="sin(x)")
    plt.subplot(122)
    y2 = [cos(num) for num in x]
    y2err = [abs((cos(num) - np.cos(num))/cos(num)) for num in x]
    plt.errorbar(x, y2, yerr=y2err, label="cos(x)")
    plt.show()


def error_calc(testfunc, npfunc):
    return lambda nmax: abs((testfunc(np.pi/2, nmax)-npfunc(np.pi/2))/npfunc(np.pi/2))


def plot_error_per_term(nmax_range):
    x = np.pi/2
    nmax_list = np.arange(0, nmax_range, 1)
    sin_test = error_calc(sin, np.sin)
    error_list = sin_test(nmax_list)
    # for nmax in nmax_list:
    #     error_list[nmax] = abs((func1(x, nmax) - func2(x))/func1(x, nmax))
    plt.plot(nmax_list, error_list)
    plt.show()




# print(sin(np.pi))
# basic_trig_plot()
# plot_trig_error()
# plot_error_per_term(50)



# test cases
# print(np.cos(0.3))
# print(cos(0.3))
# print(np.tan(1))
# print(tan(1))
# print(1/np.tan(1))
# print(cot(1))
# print(cosh(1))
# print(np.cosh(1))
# x = np.linspace(0, 10*np.pi, 1000)
# y1 = [sin(num) for num in x]
# y2 = [cos(num) for num in x]
# y3 = [tan(num) for num in x]
# y4 = [sinh(num) for num in x]
# y5 = [cosh(num) for num in x]
# y6 = [tanh(num) for num in x]
# plt.plot(x, y1, label="sin")
# plt.plot(x, y2, label="cos")
# # plt.plot(x, y3, label="tan")
# # plt.plot(x, y4, label="sinh")
# # plt.plot(x, y5, label="cosh")
# # plt.plot(x, y6, label="tanh")
# plt.xlabel("input")
# plt.ylabel("output")
# plt.ylim(-1, 1)
# plt.legend()
# plt.show()

# print(recursive_factorial(5))
# print(factorial(5))
# print(sin(0.3, 7))
# print(np.sin(0.3))
#
# print(sine(1, 7))
# print(np.sin(1))
