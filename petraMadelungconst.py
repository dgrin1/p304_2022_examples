
import numpy as np #import the

x=int(input("How far our in the cube do you want to go in the x-direction?"))
y=int(input("How far our in the cube do you want to go in the y-direction?"))
z=int(input("How far our in the cube do you want to go in the z-direction?"))
sum=0

for i  in range (-x,x):
	for j in range(-y,y):
		for k in range (-z,z):
			if ((i!=0) and (j!=0) and (z!=0)):
				num=(-1)**(i+j+k)
				#print(num)
				den=np.sqrt((i**2)+(j**2)+(k**2))
				#print(den)
				M=num/den
				#print(M)
				sum+=M
print("The madelung constant for these positions is:", sum)