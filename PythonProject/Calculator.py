# Calculator App
logo = """
 _____________________
|  _________________  |
| |   Calculator   0.| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        op_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[op_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {op_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()  # restart the calculator

calculator()
