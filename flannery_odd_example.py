# Author: Seamus Flannery
# Run this file from the command line, all functions are called in the executable.
# Basic interactive program that tests various divisibilities
numbr = float(input("What number would you like to assess?"))
# could use regex to decide what to type this variable instead of imposing float and throwing errors on strings

if type(numbr) == float and numbr % 2 != 0 and numbr % 2 != 1:
    print("Your number contains a decimal.")

if numbr % 2 == 1:
    print("Your number is odd.")
    if numbr % 3 == 0:
        print("Your number is also divisible by 3 but not 6")

elif numbr % 2 == 0:
    print("Your number is even.")
    if numbr % 3 == 0:
        print("Your number is also divisible by 3 and 6")



