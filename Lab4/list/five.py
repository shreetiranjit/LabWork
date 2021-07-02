'''
Write a Python program to count the number of strings where the string length is 2 or more and
the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''
def string(a):
    result = 0
    for i in a :
        if len(i) >=2 and i[0] == i[-1] :
            result += 1
    return result

print(string(['abc','xyz' , 'aba' , '1221', 'hihjh']))




