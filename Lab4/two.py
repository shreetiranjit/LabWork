'''
Write a Python program to convert temperatures to and from celsius, fahrenheit.
C = (5/9) * (F -32)
'''
temperature = float(input("Enter the temperature :"))
unit = str(input("Enter 'F' if it's in fahrenheit and 'C' if it's in celsius:"))
if unit.upper() == 'F' :
    C = (5/9) * (temperature-32)
    print (f'The conversion of {temperature} in celsius is {C} .')
elif unit.upper() == 'C' :
    F = (temperature - 32) * (5/9)
    print(f'The conversion of {temperature} in fahrenheit is {F} .')

