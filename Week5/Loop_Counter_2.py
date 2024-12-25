"""
Author: Lavell McGrone
Date: 2024-10-03
Description: Counting program that validates and prints numbers between a small and large number (inclusive),
calculates their sum, and displays the result.
"""

def main():
    """
    Main execution control method.
    :return: None
    """
    print("Welcome to Lavell's Loop Counter 2 program.")
    try:
        small_num, large_num = inputs()   # Gather input numbers from the user
        total_sum = processing(small_num, large_num)   # Process the numbers to calculate the total sum
        outputs(small_num, large_num, total_sum)  # Output the results to the user
        restart = input("Would you like to try again? Enter y or n: ")
        if restart == 'y' or restart == 'Y':  # Ask the user if they want to restart the program
            main()  # Restart the program
        else:
            print("Thanks for using the program! ")
    except Exception as err:
        print(f"An error occurred: {err} ")   # Handle any unexpected errors and prompt for restart
        main()

def inputs():
    """
    Gather and validate the small and large numbers input from the user.

    :return: small_num, large_num (both integers and validated)
    """
    # Get the small number from the user
    small_num = get_valid_num("Please enter a small whole number (0 or higher): ")
    # Get the large number from the user, ensuring it is larger than the small number
    large_num = get_valid_num(f"Please enter a whole number larger than {small_num}: ", small_num)
    return small_num, large_num

def processing(small_num, large_num):
    """
    Process the user input of the numbers between small_num and large_num (inclusive).
    :param small_num: The small number input by the user.
    :param large_num: The large number input by the user.
    :return: The total sum of numbers between small_num and large_num (inclusive).
    """
    total_sum = 0  # Initialize the total_sum
    # Loop through the range of numbers and print each one
    for number in range(small_num, large_num + 1):  # Loop numbers from small_num to large_num (inclusive)
        print(number)  # Print the current number
        total_sum = total_sum + number  # Calculate the sum
    return total_sum  # Return the calculated total sum

def outputs(small_num, large_num, total_sum):
    """
    Display the total sum of the numbers between small_num and large_num (inclusive).
    :param small_num: The smaller of the two input numbers.
    :param large_num: The larger of the two input numbers.
    :param total_sum: The sum of the numbers between small_num and large_num.
    :return: None
    """
    print()  # Print an empty line for spacing
    # Output the result to the user
    print(f"The total sum of numbers between {small_num} and {large_num} is {total_sum}. ")
    print()  # Print another empty line for spacing

def get_valid_num(prompt, min_value=None):
    """
    Validates that the input is a whole number (integer) and greater than the specified small number.
    :param prompt: The prompt message for user input.
    :param min_value: The minimum value allowed for input. If None, no minimum restriction is applied.
    :return: A valid integer that meets the requirements.
    """
    while True:  # Start an infinite loop to get valid input
        try:
            # Attempt to convert the input to an integer
            whole_num = int(input(prompt))  # use int directly for whole numbers
            # Check if the number is valid based on user input
            if whole_num >= 0 and (min_value is None or whole_num > min_value):
                return whole_num
            elif min_value is not None and whole_num <= min_value:
                print(f"Please enter a whole number greater than {min_value}.")
            else:
                print("Please enter a valid whole number (0 or higher).")
        except ValueError:
            # Give user error if they input anything that does not meet the above requirements.
            print("Invalid input. Please enter a valid whole number.")

# Run the program
main()
