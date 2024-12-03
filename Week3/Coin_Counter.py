"""
Author: Lavell McGrone
Date: 2024-09-19
Description: Calculate and display the total amount in a coin jar.
"""


# Main function to organize the program logic
def main():
    # Input: Prompt the user for the number of each coin type
    print("Enter the number of each type of coin in your jar.")

    # Validate input for each coin type using the helper function
    quarters = get_valid_coin_input("Quarters: ")  # Number of quarters
    dimes = get_valid_coin_input("Dimes: ")        # Number of dimes
    nickels = get_valid_coin_input("Nickels: ")    # Number of nickels
    pennies = get_valid_coin_input("Pennies: ")    # Number of pennies

    # Processing: Calculate total values for each coin type
    total_quarters = quarters * 0.25  # Total value of quarters
    total_dimes = dimes * 0.10        # Total value of dimes
    total_nickels = nickels * 0.05    # Total value of nickels
    total_pennies = pennies * 0.01    # Total value of pennies

    # Calculate the grand total of all coins
    grand_total = total_quarters + total_dimes + total_nickels + total_pennies

    # Output: Display results in a formatted table
    print("\nCoin Count Summary")  # Header for the summary table
    print("-" * 45)
    print(f"{'Coin Type':<10}{'Count':>10}{'Value ($)':>15}")  # Column headers
    print("-" * 45)
    print(f"{'Quarters':<10}{quarters:>10}{total_quarters:>15.2f}")  # Quarters row
    print(f"{'Dimes':<10}{dimes:>10}{total_dimes:>15.2f}")          # Dimes row
    print(f"{'Nickels':<10}{nickels:>10}{total_nickels:>15.2f}")    # Nickels row
    print(f"{'Pennies':<10}{pennies:>10}{total_pennies:>15.2f}")    # Pennies row
    print("-" * 45)
    print(f"{'Total':<10}{'':>10}{grand_total:>15.2f}")             # Grand total row

    # Conditional logic to display a custom message based on the grand total
    if grand_total > 10:
        print("\nYou have more than $10!")  # Message for grand total > $10
    elif grand_total == 10:
        print("\nYou have exactly $10!")   # Message for grand total == $10
    else:
        print("\nYou have less than $10.")  # Message for grand total < $10


# Helper function to validate user input
def get_valid_coin_input(prompt):
    """
    This function ensures the user enters a valid whole number.
    If the input is not numeric, it prompts the user again.
    """
    while True:  # Loop until valid input is received
        coin_input = input(prompt)
        if not coin_input.isnumeric():  # Check if input is numeric
            print("Error: Please enter a whole number greater than or equal to 0.")
        else:
            return int(coin_input)  # Convert and return the input as an integer


# Run the program only if the script is executed directly
if __name__ == "__main__":
    main()  # Call the main function to start the program
