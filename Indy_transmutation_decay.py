import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# The original nucleus before the decay is called the parent nucleus,
# and the nucleus remaining after the decay is called the daughter nucleus.

# Initial condition of the decay t = 1000 => N = 1000
N0 = 1000
# T_half_int = input("What is the initial half life for radioactively decay (years)?: ")
# T_half = int(T_half_int)
T_half = 270
lamda = 0.693 / T_half  # The constant rate of half life of a first-order reaction (ln of 2 = 0.693)

# Creating an array of time
t_int, t_final, step = 0, 1000, 1
t = np.arange(t_int, t_final, step)


# Formula of radioactively decay
def decay(N, t):
    return -lamda * N


# Solving the linear differential equation using odeint method from scipy
sol = odeint(decay, N0, t)
N = sol[:, 0]

plt.plot(t, N, label="Parent nucleus")
plt.plot(t, N0 - N, label="Daughter nucleus")
plt.title("The plot of radioactive transmutation decay")
plt.xlabel("Time (half lives)")
plt.ylabel("Numbers of remaining nucleus")
plt.legend()
plt.show()
