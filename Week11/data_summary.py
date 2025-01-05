"""
Author: Lavell McGrone
Date: 2024-18-11
Description: Read integers from a file, calculate amount of numbers, total, average,
and write the stats in a formatted table.
"""


def main():
    # Step 1: Try to open the input file for reading
    try:
        # Open the file with a descriptive variable name
        text_file = open("ch_9_lab_data.txt", "r")

        # Read all lines from the file and process them into integers
        numbers = [int(line.strip()) for line in text_file if line.strip().isdigit()]

        # Close the file manually
        text_file.close()

        # Step 1: Perform calculations
        count, total, average = perform_calculations(numbers)

        # Step 2: Display results in a formatted table
        format_and_display_results(count, total, average)

        # Proceed to process the data if no errors occurred
        print(f"Successfully read {len(numbers)} numbers from the file.")
        print(f"Numbers: {numbers}")

    except FileNotFoundError:
        # This block runs if the file doesn't exist
        print("Error: The file 'ch_9_lab_data.txt' was not found.")
        return  # Exit the program, since we cannot proceed without the input file

    except ValueError:
        # This block runs if the file contains invalid (non-numeric) data
        print("Error: The file contains invalid data.")
        return  # Exit the program, since invalid data cannot be processed


def perform_calculations(numbers):
    """
    Perform calculations of a list of integers and return the count, total, and average.
    :param:numbers (list): A list of integers.
    :return: Tuple containing the count of integers, total sum, average.
    """
    # Step 1: Count the number of integers
    count = len(numbers)  # Use len() to get the total number of integers in the list

    # Step 2: Calculate the total sum of the integers
    total = sum(numbers)  # Use sum() to get the total of all integers in the list

    # Step 3: Calculate the average of the integers
    average = total / count  # Get the average by dividing total by count

    # Step 4: Return the results as a tuple
    return count, total, average  # Return all three calculated values


def format_and_display_results(count, total, average):
    """
    Format and display the summary of results in a table with labels left-aligned
    and values right-aligned.
    :param:
        count (int): The count of integers.
        total (int): The sum of integers.
        average (float): The average of integers, rounded to two decimal places.

    Output:
       -----------Summary of Results-----------
    Count of Integers:            54321
    Total Sum:                135534897
    Average:                    2495.07
    Successfully read 54321 numbers from the file.
    Numbers:  2751....
    """
    # Step 1: Print the header
    print("Summary of Results".center(40, "-"))

    # Step 2: Print the results in a formatted table
    # Labels ( Count of Integers, Total Sum, Average) are left-aligned (<).
    # Values are right-aligned (>).
    print(f"{'Count of Integers:':<20}{count:>15}")
    print(f"{'Total Sum:':<20}{total:>15}")
    print(f"{'Average:':<20}{average:>15.2f}")  # Two decimal places for the average


# Call the main function to run the program
main()
