def takeUserInput():
    numbr = input('What number would you like to assess? \n  ')
    try:
        numbr = int(numbr)
    except:
        print("WARNING: You did not enter a number. Please enter an integer number\n*\n")
        numbr = takeUserInput()
    return numbr

numbr = takeUserInput()
if(numbr%2==1):
    print("Your number is odd.")
elif(numbr%2==0):
    print("Your number is even.")
else:
    print("idk")
