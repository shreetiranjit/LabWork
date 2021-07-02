'''
Write a Python program to count the number of even and odd numbers from a series of numbers.
'''
for i in range (1,201) :
    if i % 2 == 0 :
        print(f'{i} is even number .')
    elif i % 2 == 1 :
        print (f'{i} is odd number.')