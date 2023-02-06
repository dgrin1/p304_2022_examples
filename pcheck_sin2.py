import matplotlib.pyplot as plt
import numpy as np
#plt.ion only works in interactive mode
plt.ion()
plt.rc('text',usetex=True)
plt.rc('font', family='serif')

x=np.linspace(0.0001,8*np.pi,100)
y=np.abs(np.sin(x))
x2=np.linspace(0,8*np.pi,40)
y2=np.abs(np.sin(x2))
y3=np.abs(np.sin(x+.4))

plt.subplot(211)
plt.title('Height of ocean swells'r'~\Gamma',fontsize=24,color='b')
plt.yscale('log')
al=plt.plot(x,y,'k',label='theory')
bl=plt.plot(x2,y2,'r^',markersize=8,label='data')
plt.ylabel(r'\Gamma',fontsize=24)

plt.setp(al,linewidth=4.)
plt.legend(loc=1)

plt.ylim([1.e-2,1.e2])

plt.subplot(212)
al=plt.plot(x,y3,'k',label='bad theory')
plt.setp(al,linewidth=4.)

plt.plot(x2,y2,'r^',markersize=8,label='data')

plt.legend(loc=1)
plt.yscale('log')


#plt.ylim([0,1.3])
plt.ylim([1.e-2,1.e2])

plt.ylabel(r'\Gamma',fontsize=24)
plt.xlabel(r'\omega t',fontsize=16)
plt.show()
plt.savefig('ocean.pdf',format='pdf',dpi=1000)