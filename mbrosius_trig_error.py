import numpy as np
import matplotlib.pyplot as plt
from mbrosius_trig_library import *


data = []
data2 = []
#error = []
for n in range(0,100):
    temp=(2*np.pi/100)*n
#    error_temp=[cos(temp)-cos((2*np.pi/100)*n)]/cos(temp)
    data.append(cos(temp))
    data2.append(np.cos(temp))
#    error.append(error_temp)
    
x=np.linspace(0,2*np.pi,100)
y=data
y2=data2


plt.ylim([-1.1,1.1])

plt.plot(x,y)
plt.plot(x,y2)

plt.plot
plt.show()
