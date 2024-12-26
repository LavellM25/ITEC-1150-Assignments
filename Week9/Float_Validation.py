"""
Author: Lavell McGrone
Date: 2024-11-02
Description: Validate user input to check if it is a correctly formatted float,
including integers and decimal numbers with optional minus signs. Use a regular expression so input consists
only of digits [0-9], a single (optional) decimal point[.], and optional leading minus sign[-]. Provide user feedback
on whether the entered value is a valid number based on requirements.
"""

import re

def main():
    """
    Main execution control method.
    :return: None
    """
    print("Welcome to the float validation program.")   # Introductory statement

    while True:
        try:
            # Prompts the user for input (number as a string).
            user_input = get_user_input()
            # Validates if the input string is a valid float or integer based on specific requirements.
            is_valid = validate_float(user_input)
            # Displays an message based on user input, that will be the output.
            display_result(user_input, is_valid)

            # Loop to ask if the user wants to validate another number
            restart = input("\nWould you like to validate another number? (y/n): ").strip().lower()
            if restart == 'y':  # Continue the outer loop to validate another number
                print("\nRestarting the program...\n")
                continue  # Restart the current loop iteration
            elif restart == 'n':  # Exit the program
                print("Thanks for using the program!")
                break  # Exit the while loop
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")  # Error message for invalid input

        except Exception as err:
            print(f"\nAn error occurred: {err}")  # Handle unexpected errors

# Input function to prompt the user for a number
def get_user_input():
    """
    Asks the user to enter a number, allowing both negative signs and decimal points.
    The user's input as a string (float).
    :return: None
    """
    return input("Enter a number. Negatives and decimals are allowed: ")

# Processing function to validate if the input is a valid float
def validate_float(number):
    """
    Validates the user's input to ensure it follows the format of a valid integer or decimal number.

    This regular pattern is structured as follows:
    `^`: Pattern that starts the beginning of the string.
    `-?`: Means that there is an optional minus sign (`-`). The question mark `?` means "0 or 1 occurrence"
    of the minus sign.
    `[0-9]+`: Means one or more digits (0-9). This ensures that there are digits before the decimal if it exists.
    After the decimal point, this entire part is optional (because of the `?` outside the parentheses).
    `[0-9]+`: Means one or more digits after the decimal point, ensuring that if a decimal exists,
    there are digits after it.
    - `$`: Pattern that starts the end of the string.
    This pattern will match the following:
    A negative or positive integer, such as "-123" or "456".
    A negative or positive decimal number, such as "-123.456" or "0.99".
    It will *not* match input with multiple decimal points (i.e. "1.2.3")
    or numbers with non-numeric characters (i.e. "12a").

    :param: number (str) The input string to validate.
    :return: True if the input string matches the valid number format, False otherwise.
    """
    # Pattern to match valid float
    pattern = r"^-?[0-9]+(\.[0-9]+)?$"
    match = re.match(pattern, number)
    if match:
        return True
    else:
        # If input do not meet the general requirements, this boolean statement will be false.
        return False

# Output function to display the result
def display_result(number, is_valid):
    """
    Displays the outcome of the validation to the user.
    :param: Number (str): The user's input that was validated.
    :param: The result of the validation, indicating if the input was a valid number.
    :return: None
    """
    if is_valid:
        print(f"{number} is a valid number!")
    else:
        # Display a message indicating whether the user's input is a valid number or not.
        print("This does not look like a valid number.")
        return None

# Run the main function
if __name__ == "__main__":
    main()
