
import random

def guess_the_number():
    print("🎉 Welcome to the 'Guess the Number' game! 🎉")
    print("I am thinking of a number between 1 and 100, try to guess it!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    while True:
        # Take input from the player
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if user_guess < number_to_guess:
            print("Too low! Try again. ⬇️")
        elif user_guess > number_to_guess:
            print("Too high! Try again. ⬆️")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts! 🎉")
            break  # End the game if the user guesses correctly

guess_the_number()

