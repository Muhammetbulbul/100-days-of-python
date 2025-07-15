print("Welcome to my tip calculator")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15: "))
person = int(input("How many people to split the bill? "))

# calculate ratio of tip out of 100
total_tip_amount = (bill * tip) / 100

# total bill with tips
total_amount = bill + total_tip_amount

# per person share
bill_person = total_amount / person

# final rounded result
final_amount = round(bill_person, 2)

print(f"Each person should pay: ${final_amount}")




