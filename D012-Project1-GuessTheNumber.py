from random import randint

HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 10

def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty.lower() == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif difficulty.lower() == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return 0

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    total_attempts = set_difficulty()

    while total_attempts > 0:
        print(f"You have {total_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)
        total_attempts -= 1
        
        if total_attempts == 0:
            print("You've run out of guesses, you lose.")
            break

        print("Guess again.")

play_game()

