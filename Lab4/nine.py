'''
Write a program to find the factorial of a number.
'''
num = int(input("Enter the value to find the factorial :"))
fact = 1
for i in range (2,num+1) :
    fact = fact * i
print(fact)
fact = fact + 1




