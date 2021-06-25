'''
Write a program to find the factorial of a number using functions.
'''
def factorial(num):

    fact = 1
    for i in range (2, num + 1) :
        fact = fact * i

    return fact
num = int(input("Enter the value:"))
print (factorial(num))


