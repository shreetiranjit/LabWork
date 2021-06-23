'''
Given a three-digit number. Find the sum of its digits.
'''
number = int(input("Enter the value:"))
a = number//100
print(f'{a} is first digit')
b= (number//10 ) % 10
print (f'{b}is second digit')
c= number % 10
print (f'{c} is third digit')
sum = a+b+c
print(sum)