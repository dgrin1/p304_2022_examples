from numpy import cos,sin


r=[5.0,2.33, 1.77]
theta=[0.01,3.141,0.9]
i=0



x=r*cos(theta)
y=r*sin(theta)

print(x,y)

for i in range(10):
	rinput=input("please tell me one star r")
	thetainput=input("please tell me one more theta")
	r.append(rinput)
	theta.append(thetainput)
