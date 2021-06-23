'''
 Given an integer number, print its last digit.
'''

number = int(input("Enter the number with more than one digit :"))
last_digit = number % 10
print(f"The last digit of {number} : {last_digit}")