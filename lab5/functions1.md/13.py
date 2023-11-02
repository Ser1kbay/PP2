import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    attempts = 0
    print("HELLO, What is your name?")
    name = input()

    print(f"Welcome to the Guess the Number game {name}!")
    print("I'm thinking of a number between 1 and 20. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()