'''
Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
other than 1 and itself.
'''
def prime(a) :

    if a > 1 :
        for i in range (2,a) :
           if a % i == 0 :
               print (f'{a} is not a prime number.')
               break
           else :
               print (f'{a} is a prime number.')
               break
    else :
        print(f'{a} is not a prime number.')
a = int (input("Enter the number:"))
prime(a)