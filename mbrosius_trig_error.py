import numpy as np
import matplotlib.pyplot as plt
from mbrosius_trig_library import *


data = []
for n in range(0,100):
    temp=(2*np.pi/100)*n
    data.append(tan(temp))
    
x=np.linspace(0,2*np.pi,100)
y=data

plt.ylim([-1.1,1.1])

plt.scatter(x,y)
plt.show()
