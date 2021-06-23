'''
Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

seconds = int(input("Enter time in seconds : "))
One_day_in_sec = (24*60*60)
One_Hour_in_sec = (60*60)
One_minutes_in_sec = (60)
day = seconds/One_day_in_sec
hour = seconds/One_Hour_in_sec
minutes = seconds/One_day_in_sec
print(f"Number of days in {seconds} is {day}:")
print(f"Number of Hour in {seconds} is {hour}:")
print(f"Number of minutes in {seconds} is {minutes}:")
