'''
 If temperature is greater than 30, it's a hot day other wise if it's less than 10;
 it's a cold day; otherwise, it's neither hot nor cold.
'''

temperature = int(input("Enter the temperature :"))
if (temperature>30) :
    print ("it's a hot day")
elif (temperature<10) :
    print ("it's a cold day")
else :
    print ("it's neither hot nor cold")