'''
2.Write a program that reads the length of the base and the height of a right-angled triangle and prints
 the area. Every number is given on a separate line.
'''


base = int(input("enter the value of base:"))
height = int(input("enter the value of height:"))
area = (base*height)//2
print(area)
print(f"The area of right-angled triangle is {area}")
