import re

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Real-Time Calculator!")
    print("Enter 'quit' to exit.")

    while True:
        expression = input("Enter an expression: ")

        if expression.lower() == 'quit':
            print("Exiting calculator. Goodbye!")
            break

        # Using regular expression to split the expression into operands and operator
        match = re.match(r'^([-+]?\d+(\.\d+)?)\s*([-+*/])\s*([-+]?\d+(\.\d+)?)$', expression)
        
        if match:
            num1 = float(match.group(1))
            operator = match.group(3)
            num2 = float(match.group(4))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                result = "Invalid operator"

            print("Result:", result)
        else:
            print("Invalid expression. Please enter a valid expression.")

calculator()
