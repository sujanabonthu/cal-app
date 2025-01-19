# Simple calculator program

# Function to perform arithmetic operations
def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation"

# Prompt user for input
print("Welcome to the simple calculator!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

# Perform calculation and display the result
result = calculator(num1, num2, operation)
print(f"The result of {operation}ing {num1} and {num2} is: {result}")
