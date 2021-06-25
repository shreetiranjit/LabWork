'''
Write a function called fizz_buzzthat takes a number.If the number is divisible by 3, it should return
 “Fizz”.If it is divisible by 5, it should return “Buzz”.If it is divisible by both 3 and 5, it should
 return “FizzBuzz”.Otherwise, it should return the same number.
'''
def fizz_buzzthat () :

    if (a//3) :
        print ("Fizz")
    elif (a//5) :
        print ("Buzz")
    elif (a//5 and a//3) :
        print ("FizzBuzz")
    else :
        print (a)
a = int(input("Enter the value for a  :"))
fizz_buzzthat()