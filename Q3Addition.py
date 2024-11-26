# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
streak = 1
while True:
    A = random.randint(1,10**streak)
    B = random.randint(1,10**streak)
    if random.randint(1,2) == 1:
        c = True
        print ("What is",A,"+",B)
        while c == True:
            try:
                inp = int(input())
                if inp == A+B:
                    print("Good Job!")
                    streak = streak + 1
                    c = False
                else:
                    print("Wrong! Try again!")
                    print("Streak Lost:", streak)
                    streak = 1
                    A = random.randint(1,10**streak)
                    B = random.randint(1,10**streak)
                    print ("What is",A,"+",B)
            except:
                if inp == "Exit":
                    break
    else:
        c = True
        print ("What is",A,"-",B)
        while c == True:
            try:
                inp = int(input())
                if inp == A-B:
                    print("Good Job!")
                    c = False
                    streak = streak + 1
                else:
                    print("Wrong! Try again!")
                    print("Streak Lost:", streak)
                    streak = 1
                    A = random.randint(1,10**streak)
                    B = random.randint(1,10**streak)
                    print ("What is",A,"-",B)
            except:
                if inp == "Exit":
                    break