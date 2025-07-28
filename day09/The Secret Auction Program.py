from judges_gavel import logo
print(logo)

bid = {}
while True:
    name = input("What is your name? ")
    bid_rate = int(input("What is your bid? "))
    bid[name] = bid_rate

    question = input("Do you want to bid again? (yes or no): ").lower()
    if question == "no":
        break
    else:
        print("\n"*100)




def find_winner(bid):
    highest_bid = 0
    winner = ""
    for name in bid:
        if bid[name] > highest_bid:
            highest_bid = bid[name]
            winner = name
    print(f"The winner is {winner} with a bid of {highest_bid}")



find_winner(bid)