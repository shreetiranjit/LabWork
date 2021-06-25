'''
Write a Python function that checks whether a passed string is palindrome or not.Note: A palindrome
is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
'''
def palindrome(a) :
    print(a[::-1])
    b = a[::-1]
    print(f'{b} is a reverse of {a}')


    if a == b :
        print (f'{a} is palindrome.')
    elif a!=b :
        print (f'{a} is not palindrome.')
    return a
a = str(input("Enter the word , phrase or sequence to check if it's palindrome :"))
palindrome(a)