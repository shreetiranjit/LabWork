'''
Write a Python program to sum all the items in a list
'''
def items(list):
    sum = 0
    for i in list:
        sum += i
    print(sum)
    return sum
items([1,2,3,3,6])

