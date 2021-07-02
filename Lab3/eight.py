'''
Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
other than 1 and itself.
'''
def primenumber(num) :
    not_prime = 0
    for i in range (2,num) :
        if num % i == 0:
            not_prime+=1
    if not_prime >=1 :
        print(f"{num} is not a prime number")
    else:
        print (f"{num} is a prime number ")
num = int(input("Enter the value:"))
primenumber(num)

#secondoption

def prime(p):
    if p > 1:
        for i in range(2, p):
            if p % i == 0:
                print(f'{p}is not a prime number.')
                break
            else:
                print(f'{p} is a prime number.')
                break
    else:
        print(f'{p} is not a prime number.')


p = int(input("Enter the number:"))
prime(p)






