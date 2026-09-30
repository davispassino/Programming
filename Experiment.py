import random

print("Welcome to the game!")

#Get a random number for the user to guess
solution = random.randint(1, 100)


#get and validate user input 
guess = int(input("Guess a number between 1 and 100: "))

while guess != solution:

    while not (guess >= 1 and guess <=100):
        print ("Invalid guess")
        guess= int(input("Guess a number between 1 and 100?"))

    #Determine the need of guess adjustment
    if guess > solution:
        print("Guess a lower number!")
    elif guess < solution:
        print("Guess a higher number!")

        guess= int(input("Guess again: "))

print("Correct!")



