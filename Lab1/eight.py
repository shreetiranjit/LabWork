'''
 Write a Python program which accepts the radius of a circle from the user and compute the
area. (area of circle = PI * r2)
'''

PI = float(input('Enter_The_Value_Of_PI:'))
Radius = float(input("Enter_The_Radius_Of_Circle:"))
area = PI * (Radius**2)
print(f'The area of circle is {area}:')