from art import logo

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

functions = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    should_accumulate = True

    num1 = float(input("what is first number?"))

    while should_accumulate:
        for symbol in functions:
            print(symbol)
        operators_ask = input("what is your operator ?")
        num2 = float(input("give us second number?"))
        result = functions[operators_ask](num1,num2)

        print(f"{num1} {operators_ask} {num2} = {result}")

        user_second_choice = input("would you continue ?")

        if user_second_choice == "yes":
            num1 = result
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()




calculator()