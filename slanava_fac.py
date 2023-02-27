
def factorial(x):
  if(x==1):
    fac=1
  else:
    fac=x*factorial(x-1)
  return fac
print(factorial(3))
