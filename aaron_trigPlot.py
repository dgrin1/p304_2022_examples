import aaronTrigLib as atl
import numpy as np
import matplotlib.pyplot as plt

t = np.transpose(np.arange(0,10,0.1))
print(t)

sinDat = list(map(atl.sin,t))
cosDat = [atl.sin(tt) for tt in t]
#tanDat = atl.tan(t)
#cscDat = atl.csc(t)
#secDat = atl.sec(t)
#cotDat = atl.cot(t)

plt.plot(t,sinDat)
plt.plot(t,cosDat)

plt.show()
