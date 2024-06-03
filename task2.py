def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please choose one of +, -, *, /.")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."

def main():
    print("Simple Calculator")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()
    
    result = calculate(num1, num2, operation)
    
    print(f"The result of {num1} {operation} {num2} is: {result}")

if __name__ == "__main__":
    main()
