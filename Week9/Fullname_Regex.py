"""
Author: Lavell McGrone
Date: 2024-11-02
Description: Validate and format a full name by checking for 'First Middle Last'
"""


import re


def main():
    """
    Main execution control method.
    :return: None
    """
    print("Welcome to the full name validation program.")  # Introductory statement

    while True:
        try:
            name = inputs()  # Get the full name input from the user
            is_valid, formatted_name = process_name(name)  # Validate and format the full name
            outputs(is_valid, formatted_name)  # Display the result

            # Loop to ask if the user wants to validate another name
            while True:
                # Use .strip() method to trim unnecessary spaces before or after the y/n input from user, to read error.
                # Use .lower() so that so both uppercase and lowercase responses (like "Y/N" or "y/n") will match.
                restart = input("\nWould you like to validate another name? (y/n): ").strip().lower()
                if restart == 'y':  # Restart the program
                    print("\nRestarting the program...\n")
                    main()  # Restart from the beginning
                    break
                elif restart == 'n':  # Exit the program
                    print("Thanks for using the program!")
                    break  # Exit the program
                    '''
                    Erik:
                        Restart wasn't required, so no deduction, but the exit doesn't work because you have two 
                        nested loops.
                    '''
                else:
                    print("Invalid input. Please enter 'y' for yes or 'n' for no.")  # Error message for invalid input
        except Exception as err:
            print(f"\nAn error occurred: {err}")  # Handle unexpected errors


def inputs():
    """
    Ask the user to enter a full name in 'First Middle Last' format.
    A valid user-provided full name that meets requirements.
    :return: None
    """
    # Prompt the user for full name input
    name = input("Please enter a full name (format: 'First Middle Last'): ").strip().lower()
    return name   # Return the valid, trimmed full name entered user


def process_name(name):
    """
    Process and validate the full name using a regular expression.
    :param name: The original name input by the user.
    :return: A full name (first, middle, last) that meets the requirements.
    ^: Anchors the pattern to the start of the string.
    $: Anchors the pattern to the end of the string.
    """
    # Pattern to match names in 'First Middle Last' format
    pattern = r"^[A-Za-z]+ [A-Za-z]+ [A-Za-z]+$"
    # Check if the input matches the pattern
    if re.match(pattern, name):   # Use re.match to see if 'name' fits the 'pattern' from start to end
        # Properly capitalize each part of the name
        # Split 'name' into words (first, middle, last), capitalize each, and join them back together with spaces
        formatted_name = ' '.join([word.capitalize() for word in name.split()])
        # If user enters the following that meets the above requirements, return output.
        return True, formatted_name
    else:
        # If name do not meet the general requirements, this boolean statement will be false.
        return False, None


def outputs(is_valid, formatted_name):
    """
    Display the validation result to the user.
    :param is_valid: Boolean indicating if the name is valid.
    :param formatted_name: The properly capitalized name, if valid.
    :return: None
    """
    if is_valid:
        print(f"The name '{formatted_name}' looks like a valid full name.")  # Display valid result
    else:
        # Display invalid result to the user
        print("The input does not look like a valid full name. Please enter in 'First Middle Last' format.")
        return None


# Run the program
if __name__ == "__main__":
    main()
