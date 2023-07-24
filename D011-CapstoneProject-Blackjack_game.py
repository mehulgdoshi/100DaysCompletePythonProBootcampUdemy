# import random
# import os

# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# player_score = 0
# dealer_score = 0

# player_cards = []
# dealer_cards = []

# def deal(cards_chosen, score):
#     cards_chosen.append(random.choice(cards))
#     score += cards_chosen[-1]
#     return score

# def play_game():
#     player_cards = []
#     dealer_cards = []

#     player_score = 0
#     dealer_score = 0

#     answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#     os.system('clear')
#     if answer.lower() == "y":
#         player_score = deal(player_cards, player_score)
#         player_score = deal(player_cards, player_score)

#         dealer_score = deal(dealer_cards, dealer_score)
        
#         print(f"Your cards: {player_cards}, current score: {player_score}")
#         print(f"Computer's first card: {dealer_cards[0]}")

#         continue_dealing = True
#         response = ""
#         while continue_dealing:
#             if player_score < 21 and (response == "" or response.lower() == "y"):
#                 response = input("Type 'y' to get another card, type 'n' to pass: ")
#                 if response.lower() == "y":
#                     player_score = deal(player_cards, player_score)

#                     print(f"Your cards: {player_cards}, current score: {player_score}")
#                     print(f"Computer's first card: {dealer_cards}")
#             elif dealer_score < 17:
#                 dealer_score = deal(dealer_cards, dealer_score)
#             else:
#                 continue_dealing = False
                
#         print(f"Your final hand: {player_cards}, final score: {player_score}")
#         print(f"Computer's final hand: {dealer_cards}, final score {dealer_score}")

#         if player_score > 21:
#             print("You went over. You lose.")
#         elif dealer_score > 21:
#             print("Dealer went over. You win!")
#         elif player_score > dealer_score:
#             print("You win!")
#         elif dealer_score > player_score:
#             print("Dealer win. You lose.")
#         else:
#             print("It's a draw.")

#         play_game()    

# play_game()
import random
import os

def deal_card():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lose, opponent has a Blackjack."
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_cards > computer_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score=user_score, computer_score=computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    os.system('clear')
    play_game() 

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]