numbr=input("what number would you like to asses?")
numbr_assess=float(numbr)
if (numbr_assess%2==2):
	print("Your number is Odd!")
elif (numbr_assess%2==0):
	print("Your Number is Even!")
else:
	print("This has got to be a decimal.")