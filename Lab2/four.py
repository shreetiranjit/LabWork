'''
 Given three integers, print the smallest one. (Three integers should be user input)
'''
num_1 = int(input("Enter the first integers:"))
num_2 = int(input("Enter the second integers:"))
num_3 = int(input("Enter the third integers:"))
if num_1 < (num_2 and num_3) :
    print (f"{num_1} is the smallest integers.")
elif num_2 < (num_1 and num_3) :
    print (f"{num_2} is the smallest integers.")
elif num_3 < (num_1 and num_2) :
    print (f"{num_3} is the smallest integers")