'''
WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
'''

marks_in_first_subject = int(input("Enter your first marks:"))
marks_in_second_subject = int(input("Enter your second marks:"))
marks_in_third_subject = int(input("Enter your third marks:"))
marks_in_fourth_subject = int(input("Enter your fourth marks:"))
total = marks_in_first_subject + marks_in_second_subject + marks_in_third_subject + marks_in_fourth_subject
total_percentage = (total/400)*100
if total_percentage > 70 :
    print("congrats you scored distinction.")
elif total_percentage > 60 :
    print("congrats you scored first division.")
elif total_percentage > 40 :
    print("Pass")
else :
    print("Sorry but you are fail")