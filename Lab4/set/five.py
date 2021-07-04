'''
Write a Python program to remove an item from a set if it is present in the set
'''
d_set = {23,45,67,89,90,12}
print(f'original: {d_set}')
d_set.discard(76)
print(f'after removing: {d_set}')
