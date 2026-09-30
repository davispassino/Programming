#Davis Passino

#Here is the beginning for the game loop

play_again = "y"

while play_again == "y":

#Here is where the code creates a random number and asks you to guess

    import random
    number = random.randint(1, 100)
    print ("I'm thinking of a number between 1 and 100")

    guess=int(input("Enter your guess: "))
    guess_count=1

    #Here is where the game evalutes each guess and gives feedback on the guess

    while (guess != number):

        if (guess > 100):
            print("Sorry, Enter a valid number")
        elif (guess < 0):
            print("Sorry, Enter a valid number")
        elif (guess <= number):
            print("Guess a higher number!")
            guess_count +=1
        else:
            print("Guess a lower number!")
            guess_count +=1

        guess= int(input("Guess again: "))

    #Here is the end of the game and the overall game feeback

    print("Correct!")

    if guess_count <= 3:
        print("Amazing!")

    elif guess_count <= 5:
        print("Impressive!")

    elif guess_count <= 7:
        print("Good Job!")

    elif guess_count <= 9:
        print("Took some time, but you got there!")

    elif guess_count >= 9:
        print("You need to lock in next time...")

    #Here is where it asks if you want to play again. It either loops or exits.

    play_again = input("Would you like to play again? (y/n) ")
