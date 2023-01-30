numbr=input('what number would you like to assess')
numbr_assess=int(numbr)
sec_numbr=input('what number would you like to check is a multiple of the first number')
sec_numbr_assess=int(sec_numbr)

if (numbr_assess%sec_numbr_assess==0):
    print('your number is a multiple of the first number')
else:
    print('your number is not a multiple')