import matplotlib.pyplot as plt
import numpy as np
import wharesch_trig_functions as mytrg

errorValues=[]

for N in range(1,50):

    sum=0
    count=0

    for x in np.linspace(0,2*np.pi):

        if np.sin(x)>0.001:
            
            sum+=(mytrg.sin_wharesch(x,N)-np.sin(x))/np.sin(x)
            count+=1

    errorValues.append(abs(sum/count))

plt.plot(range(1,50),errorValues)
plt.xscale("log")
plt.yscale("log")
plt.ylim([1.e-15,1.e1])
plt.show()
