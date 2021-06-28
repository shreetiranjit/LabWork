'''
Write a python program to check whether the number is Armstrong number or not using function:
[Hint: 153 - 1*1*1 + 5*5*5 + 3*3*3]
'''
def armstrong(num) :
    length_of_num = len(str(num))
    print (f'The length of num is {length_of_num}.')
    sum = 0
    arm = num


    while arm > 0 :
        digit = arm % 10
        sum += digit**(length_of_num)
        arm = arm // 10
    if sum == num :
        print("ARMSTRONG")
    else:
        print("not ARMSTORNG")
num = int(input("Enter the value:"))
armstrong(num)
