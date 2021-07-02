'''
Write a Python program that accepts a string and calculate the number of digits and letters
'''
string = str(input("Enter the string:"))
digit = 0
letter = 0
for i in string :
    if i.isdigit():
        digit = digit + 1

    elif  i.isalpha():
        letter += 1
print (f"The total number of letters are {letter}")
print(f"The total number of digits are {digit}")

