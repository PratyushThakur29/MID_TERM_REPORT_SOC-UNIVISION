import random

x=random.randint(1, 100)
z=0
while(True):
    y=int(input("Enter your guess: "))
    z+=1
    if y > x:
        print("Too high")
    elif y < x:
        print("Too low")
    else:
        print("Congratulations! You guessed the number.")
        print("Number of guesses:", z)
        break