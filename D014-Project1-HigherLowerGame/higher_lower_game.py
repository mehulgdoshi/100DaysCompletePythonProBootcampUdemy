import art
import game_data
import random
import os

def choose_option():
    option = random.choice(game_data.data)
    return option
    
def show_option(option, message):
    print(f"{message}: {option['name']}, a {option['description']}, from {option['country']}.")
    return option["follower_count"]

def play_game():
    os.system('clear')
    follower_one_count = 0
    follower_two_count = 0
    score = 0
    is_right = True
    option_A = ""
    option_B = ""

    print(art.logo)
    option_A = choose_option()
    while is_right:
        follower_one_count = show_option(option_A, "Compare A")

        print(art.vs)

        option_B = choose_option()
        if option_A == option_B:
            option_B = choose_option()
        follower_two_count = show_option(option_B,"Against B")

        answer = input("Who has more followers? Type 'A' or 'B': ")
        os.system('clear')
        print(art.logo)
        if answer.upper() == "A" and follower_one_count > follower_two_count:
            score += 1
            option_A = option_B
            print(f"You're right! Current score: {score}.")
        elif answer.upper() == "B" and follower_two_count > follower_one_count:
            score += 1
            option_A = option_B
            print(f"You're right! Current score: {score}.")
        else:
            is_right = False
            print(f"Sorry, that's wrong. Final score: {score}.")


play_game()