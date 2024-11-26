# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math

while True:
    try:
       a = int(input()); b = int(input()); print(math.sqrt(a**2 + b**2))
    except: 
        print("Fail, type Exit if you want to Exit")
        if input() == "Exit":
            break
        