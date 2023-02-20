import wharesch_trig_functions as mytrg
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2*np.pi)
ysin=mytrg.sin_wharesch(x)
npsin=np.sin(x)
ycos=mytrg.cos_wharesch(x)
npcos=np.cos(x)
ytan=mytrg.tan_wharesch(x)
nptan=np.tan(x)
ysec=mytrg.sec_wharesch(x)
npsec=1/np.cos(x)
ycsc=mytrg.csc_wharesch(x)
npcsc=1/np.sin(x)
ycot=mytrg.cot_wharesch(x)
npcot=1/np.tan(x)

plt.subplot(231)
plt.ylim([-1,1])
plt.plot(x,ysin)
plt.plot(x,npsin)

plt.subplot(232)
plt.ylim([-1,1])
plt.plot(x,ycos)
plt.plot(x,npcos)

plt.subplot(233)
plt.ylim([-1,1])
plt.plot(x,ytan)
plt.plot(x,nptan)

plt.subplot(234)
plt.ylim([-10,10])
plt.plot(x,ysec)
plt.plot(x,npsec)

plt.subplot(235)
plt.ylim([-10,10])
plt.plot(x,ycsc)
plt.plot(x,npcsc)

plt.subplot(236)
plt.ylim([-1,1])
plt.plot(x,ycot)
plt.plot(x,npcot)

plt.show()
