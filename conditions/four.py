'''
Task -----------------condition------------------------------
Weight converter:
  Input the weight of a person in either kg or lbs. If the person provides his/her
  weight in kg then convert it into lbs
  else convert it to kg.
'''
weight = int(input("Enter the weight of the person : "))

unit = input("(L)bs or (K)g : ")

if unit.lower() == "l":
    converted_lbs = weight * 0.45
    print(f"The person weight is {converted_lbs} kilos")
elif unit.lower() == "k":
    converted_kg = weight / 0.45
    print(f"The person weight is {converted_kg} pounds")
else:
    print(f"Please enter appropriate character as K for Kg or L for Lbs !!")


#secondoption
weight_of_person = float(input("Enter your weight in kg : "))
weight_of_which_kind = input("Which kind of weight you have entered .\n Type 'kg' for kilogram and 'lbs' or pound:")
forKg = "kg"
forLbs = "lbs"
print()
if weight_of_which_kind == forKg:
    inLbs = weight_of_person * 2.20
    print(f"Your weight in pound is {inLbs}")
elif weight_of_which_kind == forLbs:
    inKg = weight_of_person / 2.20
    print(f"Your weight in kg is {inKg}")
else:
    print("Invalid typed !")