MAX_ELEMENTS = 100

def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.

    Args:
        numbers (list): List of integers.

    Returns:
        int: Sum of the numbers.
    """
    return sum(numbers)

def get_integer_input(prompt):
    """
    Prompt the user for an integer input.

    Args:
        prompt (str): The input prompt message.

    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    """
    Main function to handle user input and calculate the sum of numbers.
    """
    print("Welcome to the Sum Calculator!")

    # Get the number of elements
    n = get_integer_input(f"Enter the number of elements (1-{MAX_ELEMENTS}): ")
    if not 1 <= n <= MAX_ELEMENTS:
        print(f"Invalid input. Please provide a number between 1 and {MAX_ELEMENTS}.")
        return

    # Get the list of integers
    numbers = []
    print(f"Enter {n} integers:")
    for i in range(n):
        num = get_integer_input(f"Number {i + 1}: ")
        numbers.append(num)

    # Calculate and display the sum
    total = calculate_sum(numbers)
    print("Sum of the numbers:", total)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")