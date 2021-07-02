'''
Write a Python program to clone or copy a list.
'''
def clone(list1) :
    clonelist = list1.copy()
    print(f'Clone of {list1} is {clonelist} ')

clone([1,5,6,7])