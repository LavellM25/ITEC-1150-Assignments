"""
Author: Lavell McGrone
Date: 2024-11-02
Description: Validate and format a full name by checking for 'First Middle Last' format
with optional punctuation that allow names to have apostrophes (i.e. O'Connor) and dashes (Smith-Jones).
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
                    break
                elif restart == 'n':  # Exit the program
                    print("Thanks for using the program!")
                    return  # Exit the program
                else:
                    print("Invalid input. Please enter 'y' for yes or 'n' for no.")  # Error message for invalid input
        except Exception as err:
            print(f"\nAn error occurred: {err}")  # Handle unexpected errors


def inputs():
    """
    Ask the user to enter a full name in 'First Middle Last' format.
    Additionally, will allow punctuation that allow names to have apostrophes (i.e. O'Connor) and dashes (Smith-Jones).
    :return: A valid user-provided full name that meets requirements.
    """
    # Prompt the user for full name input
    name = input("Please enter a full name (format: 'First Middle Last'): ").strip().lower()
    return name   # Return the valid, trimmed full name entered user


def process_name(name):
    """
    Process and validate the full name using a regular expression.
    Additionally, will allow punctuation that allow names to have apostrophes (i.e. O'Connor) and dashes (Smith-Jones).
    :param name: The original name input by the user.
    :return: A full name (first, middle, last) that meets the requirements.
    ^: Anchors the pattern to the start of the string.
    $: Anchors the pattern to the end of the string.
    [A-Za-z]+: Will match one or more letters, uppercase or lowercase (A-Z or a-z), will represent first name.
    (?:[-'][A-Za-z]+)?: matches the following (a,b,c,d)
    (?: ... ): a. is a non-capturing group, so will group everything in the parentheses() as a separate group output.
    [-']: b. allows for an apostrophe (') such as O'Connor or hyphen (-) such as Anne-Marie.
    ?: c. Is a quantifier that sits outside the () meaning to allow the entire group (?:[-'][A-Za-z]+)? 0 or 1 times.
    [A-Za-z]+: d. (+) sitting outside the () is a quantifier specifying this will happen one or more letters
    following the hyphen or apostrophe.
    ([A-Za-z](\\.)|[A-Za-z]+(?:[-'][A-Za-z]+)?): matches the middle name or initial for following qualities (a,b,c,d)
    [A-Za-z]\\.: a. Allows uppercase or lowercase letters followed by a period, representing an initial (like M.)
    |: b. (OR operator) provides an alternative.
    ([A-Za-z](\\.)|[A-Za-z]: c. Allows M. or M as the middle name/initial
    ([A-Za-z](\\.)|[A-Za-z]+: d. If the user middle name does not consist of 'M.' it will allow
    uppercase or lowercase letters one more times and treat it like a regular name (M. or Michael) with no error.
    [A-Za-z]+(?:[-'][A-Za-z]+)?: matches a full last name, with the following requirements (a,b,c,d)
    [A-Za-z]+(?:[-'][A-Za-z]+)?: Allows the user to enter full name following these parameters (a,b)
    [A-Za-z]+: a. Allows for uppercase and lowercase letters one or more times.
    (?:[-'][A-Za-z]+)?: b. Allows for the user to enter a hyphen or apostrophe within the last name one more times
    and treat it like a regular name (M. or Michael) with no error.
    """
    # Pattern to match names in 'First Middle Last' format, with optional apostrophes and hyphens
    pattern = r"^[A-Za-z]+(?:[-'][A-Za-z]+)? ([A-Za-z]\.|[A-Za-z]+(?:[-'][A-Za-z]+)?) [A-Za-z]+(?:[-'][A-Za-z]+)?$"

    # Check if the input matches the pattern
    if re.match(pattern, name):   # Use re.match to see if 'name' fits the 'pattern' from start to end
        # Properly capitalize each part of the name
        # Split 'name' into words (first, middle, last), capitalize each, and join them back together with spaces
        formatted_name = ' '.join([word.capitalize() for word in name.split()])
        # If user enters the following that meets the above requirements, return output.
        return True, formatted_name
    else:
        # If user does not enter in a name that meets the general requirements, this boolean statement will be false.
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


# Run the program
if __name__ == "__main__":
    main()
