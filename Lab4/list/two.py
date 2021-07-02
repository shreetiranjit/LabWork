'''
Write a Python program to multiplies all the items in a list.
'''
def mutiplies(list):
    multiply = 1
    for i in list :
        multiply *= i
    print(multiply)
    return multiply
mutiplies([9,6,7,5,4])