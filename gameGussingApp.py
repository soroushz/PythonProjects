import random

print("Wecome to Guess & Win application")

print("Please enter two numbers to start the game")

randNumber1 = int(input())
randNumber2 = int(input())

# Generating a random number from the range giving by the user in inputs
chosenNum = random.randrange(randNumber1, randNumber2)

#print("Gussed number is: ", chosenNum)

while True: 
    # Ask the user for input 
    guessedNum = int(input("Enter your guess:"))

    #Conditions 
    if guessedNum == chosenNum:
        print("Awsome! You gussed the correct number")
        break
    elif guessedNum > chosenNum:
        print("Too high! Try again.")
    else: 
        print("Too low! Try again.")








