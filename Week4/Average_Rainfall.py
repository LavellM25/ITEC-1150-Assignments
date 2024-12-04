"""
Author: Lavell McGrone
Date: 2024-09-26
Description: Calculate and display the number of years and annual rainfall based on user input.
"""

# Ask the user for the number of years in their study
num_years = int(input("How many years are in the rainfall sample? "))

# Define the variables for average rainfall
total_rainfall_all_years = 0
total_months = (num_years * 12)

# For each year, ask the user for the amount of rainfall
for year in range(1, num_years + 1):
    print(f"Rainfall data for year #{year}: ")

    # Initialize the total rainfall for the current year
    total_rainfall_year = 0

    # For each month, ask the user for the amount of rainfall (12 months in a year)
    for month in range(1, 13):
        while True:
            rainfall_input = input(f"Enter rain for month #{month} (whole number only): ")
            if rainfall_input.isnumeric():
                rainfall = int(rainfall_input)
                break # If user enters in correct value then break the loop
            else:
                print("Please enter a valid whole number for the rainfall. ")

        total_rainfall_year = (total_rainfall_year + rainfall)

    # Calculate the average rainfall for the current year
    average_rainfall_year = (total_rainfall_year / 12)

    # Display the total and average rainfall for the current year (round to 2 decimal places)
    print(f"Total rainfall for year #{year}: {total_rainfall_year:.2f} ")
    print(f"Average monthly rainfall for year #{year}: {average_rainfall_year:.2f} ")

    # Add the yearly rainfall to the overall total
    total_rainfall_all_years = (total_rainfall_all_years + total_rainfall_year)

# Calculate and display the total and average rainfall for the entire study (round to 2 decimal places)
average_rainfall_all_years = (total_rainfall_all_years / total_months)
print(f"Total rainfall, all years: {total_rainfall_all_years:.2f} ")
print()
print(f"Average monthly rainfall, all years: {average_rainfall_all_years:.2f} ")
