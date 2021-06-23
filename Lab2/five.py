'''
For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’
 if it is 0.
'''
x = int(input("Enter your value:"))
if x>0 :
    print(f"{x} : True ")
elif x<0 :
    print(f"{x} : False ")
elif x==0 :
    print (f"{x} : zero ")