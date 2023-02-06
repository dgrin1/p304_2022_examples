import matplotlib.pyplot as plt
import numpy as np
# plt.ion only works in interactive mode
# plt.ion()
plt.rc('text',usetex=True)
plt.rc('font', family='serif',serif='Palatino')
# plt.rc('font', sans-serif='Tahoma')



x=np.linspace(0,2*np.pi,100)
y=np.sin(x)
x2=np.linspace(0,2*np.pi,15)
y2=np.sin(x2)
y3=np.sin(x+.4)

plt.subplot(211)
plt.plot(x, y)
plt.title('Height of ocean swells'r'$~\Gamma$',fontsize=24,color='b')


al=plt.plot(x,y,'k')
bl=plt.plot(x2,y2,'g*',markersize=15)
plt.setp(al,linewidth=4.)
plt.ylim([-1.1,1.1])
plt.subplot(212)
al=plt.plot(x,y3,'k')
plt.setp(al,linewidth=4.)
plt.plot(x2,y2,'r^',markersize=15)
plt.ylim([-1.1,1.1])



plt.ylim([-1.3,1.3])
plt.ylabel(r'$~\Gamma$',fontsize=24)
plt.xlabel(r'$~\omega t$',fontsize=16)
plt.savefig('ocean.pdf',format='pdf',dpi=1000)
plt.show()
