import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0

    while True:
        guess = int(input("Take a guess: "))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

guess_the_number()