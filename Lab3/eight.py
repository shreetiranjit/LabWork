'''
Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
other than 1 and itself.
'''
#firstoptiondoesntprint1and2
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

p = int (input("Enter the number:"))
prime(p)

#secondoptionprints1and2
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
print(test_prime(2))

#third
def prime(num):

    checker = 0
    for i in range(1,num+1):
        if num % i == 0:
            checker += 1
    if checker == 2:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
num = int(input("Enter any positive real number : "))
prime(num)
