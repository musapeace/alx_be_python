# simple calculator with match case

# first question
num1 = input("Enter the first number:")

# second question
num2 = input("Enter the second number:")

# type of operation
operation = input("Choose the operation (+, -, *, /): ").strip()

# performing operation
match operation:
    case "+":
        print(f"the result is {num1 + num2}.")
    case "-":
        print(f"The result is {num1 - num2}.")
    case "*":
        print(f"The result is {num1 * num2}.")
    case "/":
        if num2 != 0:
            print(f"The result is {num1 / num2}.")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation! Please choose one of +, -, *, /.")  