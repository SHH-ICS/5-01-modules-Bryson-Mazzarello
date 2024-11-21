# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random

for _ in range(10):
    try:
       a = random.randint(0,100); b = random.randint(0,100); print( str(a) + " + " + str(b) + " = " + str(a+b)  )
    except:
        print("Fail")