import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    
    print("Guess the number between 1 and 100.")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            break

# Start the game
guess_number()
