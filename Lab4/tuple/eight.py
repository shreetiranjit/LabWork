'''
Write a Python program to create the colon of a tuple
'''
from copy import deepcopy

tuple = ("HELLO", 5, [],[])
print(tuple)

tuple_colon = deepcopy(tuple)
tuple_colon[2].append(50)
print('deepcopy:' , tuple_colon)
print('original:' , tuple)