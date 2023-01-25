import numpy as np

exitFlag = False
while exitFlag == False:
	r=input("How far away is the point of interest?")
	theta=input("What is the angle?")

	x=float(r)*np.cos(float(theta))
	y=float(r)*np.sin(float(theta))
	print("x=",x,"and y=",y)
	exitAnswer = ""
	while exitAnswer != 'yes' and exitAnswer != 'no':
		exitAnswer = input("Do another calculation? [yes/no]")
		#print(exitAnswer == "yes",exitAnswer == "no")
		if exitAnswer == "yes":
			exitFlag = False
		elif exitAnswer == "no":
			exitFlag = True
    
    
    
