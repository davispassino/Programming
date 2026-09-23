
#Computer generates a random number 

import random
number = random.randint(1, 100)
print ("I'm thinking of a number between 1 and 100")
print (number)

guess=int(input("Enter your guess:"))
guess_count=1


while (guess != number):
    
    guess_count += 1

    if (guess <= number):
        print("Guess a higher number!")
    else:
        print("Guess a lower number!")

    

    guess = int(input("Guess again: "))

print("Correct!")


if guess_count == 1:
    print("Mesmerizing! You guessed it your first try!")

elif guess_count <= 3:
    print("Amazing!")

elif guess_count <= 5:
    print("Impressive!")

elif guess_count <= 7:
    print("Good Job!")

elif guess_count <= 9:
    print("Took some time, but you got there!")

elif guess_count >= 9:
    print("You need to lock in next time...")