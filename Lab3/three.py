
'''
 Write a function called showNumbers that takes a parameter called limit.It should print all the numbers
 between 0 and limit with a label to
 identify the even and odd numbers. For example, if the limit is 3, it should print:0 EVEN1 ODD2 EVEN
'''
def showNumbers(a,b) :
   for i in range (a,b) :
        if i%2 == 0 :
            print (f'{i} is even')
        elif i%2 == 1 :
            print (f'{i} is odd')
   i = i+1
showNumbers(0,5)