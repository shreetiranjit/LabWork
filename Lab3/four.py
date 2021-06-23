'''
 Write a function that returns the sum of multiples of 3 and 5 between 0 and limit(parameter). For
 example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20
'''
def multiples():
    i = 1
    a = int(input("Enter the value :"))
    for i in range (0, 11) :
        c = a * i
        if (c <=20) :
            print (f' {a} * {i} is {c}' )

    i = i + 1
    d = c
    sum = d+ c 

multiples()



