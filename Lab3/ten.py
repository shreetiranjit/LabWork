'''
Accept string from the user and display only those characters which are present at an even index
'''

def string(a):
   evenstring = a[::2]
   print (f'{evenstring} are the characters in even index.')
   return evenstring
a = str(input("Enter the word:"))
string(a)




