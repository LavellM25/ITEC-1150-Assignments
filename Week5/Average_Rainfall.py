"""
Author: Lavell McGrone
Date: 2024-10-03
Description: Calculate and display the number of years and annual rainfall based on user input.
"""

def main():
    """
    Main function controlling the flow of the program with exception handling.
    :return: None
    """
    try:
        num_years = get_number_of_years()  # Input: Ask for the number of years
        total_rainfall_all_years, total_months = processing(num_years)  # Processing rainfall data
        output(total_rainfall_all_years, total_months)  # Output: Display total and average rainfall
        restart = input("Continue? Enter y or n: ")
        if restart == 'y' or restart == 'Y':
            print("OK, let\'s calculate this program again. ")
            main()
        else:
            print("Thanks for using the program. ")
    except Exception as err:
        print(err)

def get_number_of_years():
    """
    Gets the number of years for the study from the user, validate the user input.
    :return: The number of years as an integer.
    """
    while True:
        try:
            num_years = int(input("How many years are in the rainfall sample? "))
            if num_years > 0:
                return num_years
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def processing(num_years):
    """
    Processes the rainfall data for each year and each month and defines variables for average rainfall.
    :param num_years: The number of years for the rainfall study.
    :return: total_rainfall_all_years (float), total_months (int)
    """
    total_rainfall_all_years = 0  # This variable is started here
    total_months = num_years * 12  # Total number of months is calculated from num_years

    # For each year, ask the user for the amount of rainfall
    for year in range(1, num_years + 1):
        print(f"\nRainfall data for year #{year}: ")

        # Initialize the total rainfall for the current year
        total_rainfall_year = 0

        # For each month, ask the user for the amount of rainfall (12 months in a year)
        for month in range(1, 13):
            rainfall = get_monthly_rainfall(month)  # Get the rainfall value for this month
            total_rainfall_year = total_rainfall_year + rainfall  # Accumulate rainfall for the current year

        # Calculate and display the total and average rainfall for the current year
        average_rainfall_year = total_rainfall_year / 12
        print(f"Total rainfall for year #{year}: {total_rainfall_year:.2f} ")
        print(f"Average monthly rainfall for year #{year}: {average_rainfall_year:.2f} ")

        # Add the yearly rainfall to the overall total after processing all months
        total_rainfall_all_years = total_rainfall_all_years + total_rainfall_year

    return total_rainfall_all_years, total_months  # Outputs are returned for further use in output

def output(total_rainfall_all_years, total_months):
    """
    Displays the total and average rainfall for all years, based on the user input.
    :param total_rainfall_all_years: The total rainfall over all years.
    :param total_months: The total number of months in the study.
    :return: None
    """
    average_rainfall_all_years = total_rainfall_all_years / total_months
    print(f"Total rainfall, all years: {total_rainfall_all_years:.2f} inches ")  # Round the output to 2 decimal places
    print(f"Average monthly rainfall: {average_rainfall_all_years:.2f} inches ")

def get_monthly_rainfall(month):
    """
    Gets valid rainfall input for a given month from the user.
    :param month: The month number for which rainfall is being requested.
    :return: A valid number representing rainfall for that month.
    """
    while True:
        try:
            rainfall = float(input(f"Enter rain for month #{month} (decimal number allowed): "))
            if rainfall >= 0:
                return rainfall
            else:
                print("Rainfall cannot be negative. Please enter a non-negative number. ")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()
