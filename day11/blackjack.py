import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)


    return sum(cards)


def compare(u_score,c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0:
        return "computer wins"
    elif u_score == 0:
        return "user wins"
    elif u_score > 21:
        return "computer wins +"
    elif c_score > 21:
        return "user wins +"
    elif u_score > c_score:
        return "user wins"
    else:
        return "you lose"




def play_game():
    print(logo)
    user_card = []
    computer_card = []
    computer_score = None
    user_score = None

    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:

        user_score = calculate_cards(user_card)
        computer_score = calculate_cards(computer_card)

        print(f"user cards: {user_card}, and user score: {user_score}")
        print(f"computer first card: {computer_card[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over=True
        else:
            user_question = input("hit or stand").lower()
            if user_question == "hit":
                user_card.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score <17:
        computer_card.append(deal_card())
        computer_score = calculate_cards(computer_card)

    print(f"your final hand: {user_card}, final score : {user_score}")
    print(f"computer final hand {computer_card}, final score: {computer_score}")
    print(compare(user_score,computer_score))







while input("Do you want to play a game Blackjack? Type 'y'") == "y":
    print("\n" * 20)
    play_game()
