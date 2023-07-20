import os
def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": substract,
    "/": divide,
    "*": multiply
}

def calculator():
    number1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(number1, number2)

        print(f"{number1} {operation_symbol} {number2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if choice.lower() == 'y':
            number1 = answer
        else:
            should_continue = False
            os.system('clear')
            calculator()

calculator()
    
 
    


    
