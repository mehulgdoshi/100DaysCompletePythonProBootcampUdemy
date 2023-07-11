import random
from hangman_words import word_list
from hangman_art import stages, logo


print(logo)
chosen_word = random.choice(word_list)
print(f"It's secret! the chosen word is {chosen_word}")
display = []
for letter in chosen_word:
    display.append("_")
print(display)

lives_left = len(stages)
while True:
    guess = input("Guess a letter:\n").lower()
    print(chr(27) + "[2J") #To clear the Terminal window

    if guess in display:
        print(f"You've already guessed letter '{guess}'")

    for index in range(len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess
        index += 1
        
    if guess not in chosen_word:
        print(f"You guess letter '{guess}', that's not in the word. You lose a life.")
        print(stages[lives_left - 1])
        lives_left -= 1
        if lives_left == 0:
            print("You lose.")
            break
        
    print(display)
    if "_" not in display:
        print("You win.")
        break
