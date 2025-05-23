# Create a basic calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def clear():
    """Clear the current result (set to 0)."""
    return 0

def reset():
    """Reset calculator state (set both numbers to 0)."""
    return 0, 0

if __name__ == "__main__":
    print("Basic Calculator")
    result = None
    num1 = None
    num2 = None
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Clear")
        print("6. Reset")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")
        if choice == '7':
            print("Exiting calculator.")
            break
        elif choice not in ('1', '2', '3', '4', '5', '6'):
            print("Invalid input")
            continue

        if choice in ('1', '2', '3', '4'):
            try:
                if result is not None:
                    use_result = input("Use previous result as first number? (y/n): ").lower()
                    if use_result == 'y':
                        num1 = result
                    else:
                        num1 = float(input("Enter first number: "))
                else:
                    num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                print("Result:", result)
            except ValueError as e:
                print("Error:", e)
        elif choice == '5':
            result = clear()
            print("Result cleared. Current result is 0.")
        elif choice == '6':
            num1, num2 = reset()
            result = None
            print("Calculator reset. Both numbers set to 0, result cleared.")


