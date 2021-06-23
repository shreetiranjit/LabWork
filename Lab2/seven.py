'''
 Given a positive real number, print its fractional part.
'''
import math
r = float(input("Enter the  real number:"))
if r > 0:
    i = int(r)
    f = r - i
    print(i)
    print(f)
    print(math.modf(r))  #this function will print (fractional , integers)
else :
    print("You have entered the negative number.")

#second option
r = float(input('Enter the real number:'))
if r > 0 :
    integer = int(r)
    Float = r - integer
    print(f"{float} is the fractional part of {r} :")
else :
    print("You have entered the negative number.")