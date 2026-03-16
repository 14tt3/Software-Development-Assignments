import random
import math

def guessing_number():
    number = random.randint(1, 50)
    hints = ["too high", "too low", "warmer", "colder"]
    tries = []
    
    print ("I'm thinking of a number between 1 and 50. You'll have to guess it.")

    while True:
        try:
            gamemode = input("Choose a game mode: (1) 5 attempts or (2) for unlimited attempts: ")
            if gamemode == '1': 
                limited = 5 
                unlimited = False
                break
            elif gamemode == '2':
                limited = float('inf')
                unlimited = True
                break
            else:
                print ("Not an option.")
        except ValueError:
            print ("Invalid input. Choose 1 or 2.")
    
    attempts = 0
    while attempts < limited:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            tries.append(guess)
            if guess == number:
                print ("Congrats! You guessed the number correctly.")
                if unlimited:
                    print("Your guesses so far: ", tries)
                return
            elif math.fabs(guess - number) <= 5:
                print (hints[2])
            elif guess > number:
                print (hints[0])
            else:
                print (hints[1])

            attempts += 1

        except ValueError:
            print ("Invalid input. Please enter a number.")

    print(f"Wrong answer. The secret number was {number}.")
    if unlimited:
        print("Your guesses so far: ", tries)

if __name__ == "__main__":
    guessing_number()

#i almost crashed out

