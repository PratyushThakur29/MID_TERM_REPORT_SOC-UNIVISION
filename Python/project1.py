import random

S={
    "S":1,
    "W":2,
    "G":3
}
F={
    1:"S",
    2:"W",
    3:"G"
}
i=0
while(i<3):
    i += 1    
    number = random.choice([1,2,3])

    number1 = str(input("Enter your choice: "))

    print(F"Computer choice: {F[number]}")
    print(F"Your choice: {number1}") 

    if(number == S[number1]):
       print("It's a tie") 
    else:
        if((number == 1 and S[number1] == 2) or (number == 2 and S[number1] == 3) or (number == 3 and S[number1] == 1)):
          print("Computer wins")
        else:
          print("You win")