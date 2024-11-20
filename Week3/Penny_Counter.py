"""
Author: Lavell McGrone
Date: 2024-09-19
Description: Calculate and display the total value of coins (pennies, nickels, dimes, and quarters)
"""

# Ask the user for the number of each coin type
# Prompting the user to enter the quantity of each coin type
quarters = int(input("How many quarters do you have? "))
dimes = int(input("How many dimes do you have? "))
nickels = int(input("How many nickels do you have? "))
pennies = int(input("How many pennies do you have? "))

# Calculate the total amount for each coin type
# Each coin type is multiplied by its value to get the total monetary value of that coin
quarters_total = quarters * 0.25  # Each quarter is worth $0.25
dimes_total = dimes * 0.10        # Each dime is worth $0.10
nickels_total = nickels * 0.05    # Each nickel is worth $0.05
pennies_total = pennies * 0.01    # Each penny is worth $0.01

# Calculate the grand total
# Summing the total values of all coins
grand_total = quarters_total + dimes_total + nickels_total + pennies_total

# Round the grand total to 2 decimal places for display purposes
grand_total_rounded = round(grand_total, 2)

# Display a custom message based on the grand total
# The program outputs a message depending on whether the total is greater than, less than, or exactly $10
if grand_total > 10:
    message = "You have more than $10"
elif grand_total < 10:
    message = "You have less than $10"
else:
    message = "You have exactly $10"

# Print the results in a table with proper alignment
# Align numbers and values for consistent readability, ensuring decimal points are vertically aligned
print("\n")  # Print a blank line for spacing
print(f"{message}. You're rich in coins!")

# Table headers for clarity
print(f"{'Coin Type':<12}{'Count':>10}     {'Value':>12}")
print("-" * 40)

# Each row displays the coin type, count, and total value
print(f"{'Quarters':<12}{quarters:>10}     ${quarters_total:>12.2f}")
print(f"{'Dimes':<12}{dimes:>10}     ${dimes_total:>12.2f}")
print(f"{'Nickels':<12}{nickels:>10}     ${nickels_total:>12.2f}")
print(f"{'Pennies':<12}{pennies:>10}     ${pennies_total:>12.2f}")

# The total value is displayed on the last row, with count left blank for visual clarity
print(f"{'Total':<12}{'':>10}     ${grand_total_rounded:>12.2f}")
