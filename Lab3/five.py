'''
 Write a function called show_stars(rows).If rows is 5, it should print the following:
 *
 **
 ***
 ****
 *****
'''
def show_stars(a):
    for i in range (a) :
        for j in range (i+1) :
           print ('*' , end = '')
        print()
    return a
show_stars(5)