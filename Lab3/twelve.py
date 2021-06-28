'''
Write a python program to check whether the number is Armstrong number or not using function:
[Hint: 153 - 1*1*1 + 5*5*5 + 3*3*3]
'''
def armstrong(num) :
    sum = 0

    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10


    if num == sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")
num = int(input("Enter the value:"))
armstrong(num)
