'''
15. What will be the output of the following if a =2, b=3, c =4, d = 3?
a) a == b
b) a != d
c) b == d
d) a != c
e) a += c
f) b /= d
g) b > a
h) a < d
i) b-a == c-b
j) b >= d
'''

a = 2
b = 3
c = 4
d = 3
#a

if (a== b ):
    print ("True")
else:
    print("False")
#b
if a != d :
    print("True")
else:
    print("False")
#c
if b == d :
    print("True")
else:
    print("False")
#d
if a!=c :
    print("True")
else:
    print("False")

#e
a+=c
print(a)

#f
b/=d
print (b)

#g
if b>a :
    print("True")
else:
    print("False")

#h
if a<d :
    print("True")
else:
    print("False")

#i
if (b-a == c-b) :
    print("True")
else :
    print("False")
#j
if (b >= d) :
    print("True")
else :
    print ("False")
