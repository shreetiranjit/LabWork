'''
Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
other than 1 and itself.
'''
def primenumber(num) :
    check = 0
    for i in range (2,num) :
        if num % i == 0:
            check+=1
    if check >=1 :
        print(f"{num} is not a prime number")
    else:
        print (f"{num} is a prime number ")
num = int(input("Enter the value:"))
primenumber(num)



