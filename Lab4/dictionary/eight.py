'''
Write a Python script to merge two Python dictionaries.
'''
d1 = {1:10 ,2:'hi', 80:'jik' }
d2 = {'hi':'hello', 3:40, 50 :5}

d1.update(d2)  # append the d2 dictionary items into the d1 dictionary.
print("Merge two dictionaries :")
print(d1)