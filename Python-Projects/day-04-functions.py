def check_even(number):

    if number % 2 == 0:
        return "Even"

    else:
        return "Odd"

result = check_even(8)

print(result)

def largest(a, b):

    if a > b:
        return a

    else:
        return b

print(largest(10, 7))

def calculator(a, b, operation):

    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        return a / b

print(calculator(10, 5, "*"))