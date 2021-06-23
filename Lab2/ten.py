
''' Write a Python program to sum of three given integers. However, if two values are equal sum
will be zero.
'''
a = int(input("Enter the first integer:"))
b = int(input("Enter the second integer:"))
c = int(input("Enter the third integer:"))
if a==b :
    print ("The value is zero .")
elif b==c :
    print ("The value is zero . ")
elif c == a :
    print ("The value is zero .")
else :
    totalsum = a+b+c
    print(f'The sum of three integer {a} and {b} and {c} is {totalsum}.')