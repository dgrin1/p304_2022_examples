numbr = input("What number would you like to assess?")
try:
    numbr = int(numbr)
except:
    print("You did not enter a number, please enter an integer number")
    numbr = input("What number would you like to assess?")
if(numbr%2==1):
    print("Your number is odd.")
elif(numbr%2==0):
    print("Your number is even.")
else:
    print("idk")
