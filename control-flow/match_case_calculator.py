# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Prompt the user to select an operation
operation = input("Choose the operation (+, -, *, /): ").lower()
# Perform the operation using a match case statement
match operation:
    case "+": result = num1 + num2
    case "-": result = num1 - num2
    case "*": result = num1 * num2
    case "/":
        if num2 != 0: result = num1 / num2
        else: result = "Error: Cannot divide by zero."
    case _: result = "Error: Invalid operation selected."
    # Display the result
print(f"The result is: {result}")
    # Run the calculator

