'''
Write a Python program to reverse a string.
'''
def reverse(txt) :
    print(txt[ :: -1 ])
    return txt
txt= str(input("Enter the word:"))
reverse(txt)
