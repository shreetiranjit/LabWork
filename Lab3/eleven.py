'''
Write a program to find the factorial of a number using functions.
'''
def factorial(num):
    '''
    factorial of number
    :param num: float , integer
    :return: float , integer
    '''
    for i in range (2,num+1) :
        product = product * i
        return product