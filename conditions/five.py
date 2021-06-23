'''
Guess the secret number of game in 3 attempt using while loop.
'''
import random
number = random.randint(1 , 10)
attempt = 2
while attempt>=0:
    guess = int(input("Guess the number : "))
    if guess == number:
        print("Your number is correct")
        break
    else:
        print(f"You have {attempt} attempt left.")
    attempt = attempt - 1