birth_year=input("What year were you born?")
year=int(birth_year)

if (year>=2005):
    print("You seem a little young to be in a college class.")
elif (year<=1920):
    print("Wow, that's impressive, good for you!")
elif (year<=2005&year>=1920):
    print("Cool, thanks!")
else:
    print("I don't think you entered a year.")
