# Guessing Game

import random

def guess_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter an integer.")
        
    
if __name__=="__main__":
    guess_game()