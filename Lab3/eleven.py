'''
Write a program to find the factorial of a number using functions.
'''
def factorial (number) :
    fact = 1
    for i in range (2,number+1) :
        fact = fact * i
    print(fact)
    fact = fact + 1
    return fact
number = int(input("Enter the value:"))
factorial(number)


