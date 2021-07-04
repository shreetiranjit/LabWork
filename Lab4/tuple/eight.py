'''
Write a Python program to create the colon of a tuple
'''
from copy import deepcopy

tuple = ("HELLO", 5, [],[])
print(tuple)

tuple_clone = deepcopy(tuple)
tuple_clone[2].append(50)
print(tuple_clone)
print(tuple)