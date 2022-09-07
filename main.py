name = input ("What is your name?")
print ("Hi",name, ",welcome to Rushdi's simple guessing game!")

import random
x = random.randint(1,6)
print ("I am thinking of an integer from 1-6")
while True:
    try:
        guess1 = int(input("You have 3 guesses... Input your first guess:"))
    except ValueError:
        print ("Your guess has to be an integer my guy... Try again")
    else:
        break

if guess1 == x:
    print ("Wtf... my integer was",x,",you won on the 1st guess. Well done you lucky yute O_O")
    exit()

elif guess1 > x:
    while True:
        try:
            guess2 = int(input("Your guess was too high buddy... Input your second guess:"))
        except ValueError:
            print("Your guess has to be an integer my guy... Try again")
        else:
            break

elif guess1 < x:
    while True:
        try:
            guess2 = int(input("Your guess was too low buddy... Input your second guess:"))
        except ValueError:
            print("Your guess has to be an integer my guy... Try again")
        else:
            break

if guess2 == x:
    print ("Well done... my integer was",x,",you won on the 2nd guess. HURRAH! :P")
    exit()

elif guess2 > x:
    while True:
        try:
            guess3 = int(input("Your guess was too high buddy... Input your third guess:"))
        except ValueError:
            print("Your guess has to be an integer my guy... Try again")
        else:
            break

elif guess2 < x:
    while True:
        try:
            guess3 = int(input("Your guess was too low buddy... Input your third guess:"))
        except ValueError:
            print("Your guess has to be an integer my guy... Try again")
        else:
            break

if guess3 == x:
    print ("Well done... my integer was",x,",you won on the final 3rd guess. Which is a MEH")
    exit()

elif guess3 != x:
    print ("I gave you 3 guesses and you still can't get it right YOU FAILURE! My integer was",x,"lul")
