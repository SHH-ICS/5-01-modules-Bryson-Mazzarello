# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.

import random

while True:
    try:
       a = int(input()); b = int(input()); print(random.randint(min(a,b),max(a,b)))
    except:
        print("Fail, type Exit if you want to Exit")
        if input() == "Exit":
            break
        