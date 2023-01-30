import numpy as np

numbr = input("Can you take the square root of this number?")
numbr_assess=float(numbr)

if (np.sqrt(numbr_assess))==1:
	print("The square root of this number is: ", np.sqrt(numbr_assess))
	
elif (np.sqrt(numbr_assess))==0:
	print("The square root of this number is a decimal.")
else:
	print("The computer has no idea what you're asking.")