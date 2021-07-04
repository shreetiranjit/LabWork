'''
Write a Python program to convert a tuple to a string
'''
def changing(c_tuple) :
    string = ''
    for i in c_tuple :
        string +=i
    return string
c_tuple = ('1' , '1')
print(changing(c_tuple))