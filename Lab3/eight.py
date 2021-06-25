'''
Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
other than 1 and itself.
'''
def prime(p) :

    if p > 1 :
        for i in range (2,p) :
           if p % i == 0 :
               print (f'{p} is not a prime number.')
               break
           else :
               print (f'{p} is a prime number.')
               break
    else :
        print(f'{p} is not a prime number.')
    return p
p = int (input("Enter the number:"))
prime(p)