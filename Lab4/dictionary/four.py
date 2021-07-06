'''
Write a Python script to check if a given key already exists in a dictionary.
'''
d = {1: 10, 2: 20, 3: 30}
def checkKey(d, value):
    if value in d:
        print(f'{keys} is present ')
        print('value =' , d[value])
    else:
        print(f"{keys} is not present")

keys= int(input("Enter the value to check if it is present as key :"))
checkKey(d,key1)

