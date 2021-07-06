'''
Write a Python script to sort (ascending and descending) a dictionary by value
'''
import operator
d = {5:3 , 3:1 , 2:8 , 7: 2 }
s = sorted(d.items() , key=operator.itemgetter(1))
print (f'ascending order : {s}')

s = sorted(d.items() , key=operator.itemgetter(1) , reverse = True)
print(f'descending order: {s}')
