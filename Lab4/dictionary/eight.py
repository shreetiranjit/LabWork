'''
Write a Python script to merge two Python dictionaries.
'''
d = {1:999}
d1 = {2:888}
merge_value = dict(d | d1 )
print(merge_value)