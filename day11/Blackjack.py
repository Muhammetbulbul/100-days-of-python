import random
from art import logo

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card



def calculator(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score,c_score):
    if u_score == c_score:
        return "draw"
    elif u_score == 0:
        return "user win with blackjack"
    elif c_score == 0:
        return "computer win with blackjack"
    elif u_score > 21:
        return "computer wins"
    elif c_score > 21:
        return "user wins"
    elif u_score > c_score:
        return "user wins"
    else:
        return "computer wins"



def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())



    while not is_game_over:


        user_score = calculator(user_cards)
        computer_score = calculator(computer_cards)
        print(f"user cards : {user_cards} and user score : {user_score}")
        print(f"computer first card = {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            question = input("hit or stand").lower()
            if question == "hit":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculator(computer_cards)

    print(f"user final score = {user_score} and final cards = {user_cards}")
    print(f"computer final score = {computer_score} and final cards = {computer_cards}")
    print(compare(user_score, computer_score))



while input("Would u play Blackjack? ")== "yes":
    print("\n"*20)
    play_game()
