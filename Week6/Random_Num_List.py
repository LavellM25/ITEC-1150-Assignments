"""
Author: Lavell McGrone
Date: 2024-10-13
Description: Generate a sorted list of random numbers, with the total, minimum, and maximum values, given user input.
"""

import random


def main():
    """
    Main execution control method.
    :return: None
    """
    print("Welcome to the Random Number List Program.")
    try:
        num_randoms = inputs()  # Get user input for the number of random numbers to generate
        random_list = processing(num_randoms)  # Generate the random number list
        outputs(random_list)  # Display the results

        while True:  # Loop until a valid input is received
            restart = input("\nWould you like to generate another list? Enter y or n: ")
            if restart.lower() == 'y':  # Check for 'y' or 'Y'
                print("Generating a new list.")
                main()  # Restart the program
                break  # Exit the loop after restarting
            elif restart.lower() == 'n':  # Check for 'n' or 'N'
                print("Thanks for using the program!")
                break  # Exit the loop, if user enters correct value
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")  # Error message for invalid input
    except Exception as err:
        print(f"An error occurred: {err}")  # Handle any unexpected errors and prompt for restart
        main()  # Restart the program


def inputs():
    """
    Ask the user how many random numbers they want to generate, validate the input.
    :return: The number of random numbers (validated integer > 0).
    """
    num_randoms = get_valid_num("How many random #'s would you like to generate? Enter a whole number greater than 0: ")
    return num_randoms


def processing(num_randoms):
    """
    Generate a list of random numbers between 1 and 100.
    :param num_randoms: Generate the number of random numbers that are specified by the user.
    :return: A sorted list of random numbers from 1 and 100.
    """
    random_list = []  # Initialize the list
    for _ in range(num_randoms):
        random_list.append(random.randint(1, 100))  # Pick a random integer between 1 and 100 and add it to the list.
    random_list.sort()   # Sort the list in ascending order from least to greatest in the random list.
    return random_list   # Random numbers picked 1-100.


def outputs(random_list):
    """
    Display the sorted list, the total, minimum, and maximum of the random numbers.
    :param random_list: The list of random numbers.
    :return: None
    """
    total_sum = sum(random_list)  # Calculate the total sum
    min_value = min(random_list)  # Get the minimum value
    max_value = max(random_list)  # Get the maximum value

    # Display the results from user input picked numbers from 1-100, meeting the requirements
    print(f"Here is your sorted list of {len(random_list)} integers: {random_list}")

    # Shortcut method to convert the list of integers to strings and join them with commas for display.
    print("Here is your list printed with the shortcut method: ", end="")  # Keep on the same line.
    print(*random_list, sep=", ")  # Print the list separated by commas.

    # Loop method to print list with total sum calculation
    print("Here is your list, printed via a loop, with total: ", end="")  # Continue on the same line.
    for i in range(len(random_list)):  # Complete this action from random list using the range function
        if i == len(random_list) - 1:  # If it's the last element, print the number without a "+" after it
            print(f"{random_list[i]}", end="")  # Ensure no "+" for the last number.
        else:
            print(f"{random_list[i]} + ", end="")  # Print the number followed by a "+", until the end of the list

    print(f" = {total_sum}")  # Add space before total sum and print on the same line, took total_sum out of the loop.

    # Display the minimum and maximum values separately
    print(f"The minimum value is: {min_value} and the maximum value is: {max_value}")


def get_valid_num(prompt):
    """
    Validate that the input is a whole number > 0.
    :param prompt: The prompt message for user input.
    :return: A valid integer > 0.
    """
    while True:  # Continue the loop until user gives valid input.
        try:
            num = int(input(prompt))  # Get the user input as an integer
            if num > 0:  # Check if the input is a whole number > 0
                return num  # Return the valid integer
            else:
                print("The whole number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid whole number that is greater than 0.")


main()  # Run the program
