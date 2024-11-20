"""
Author: Lavell McGrone
Date: 2024-09-13
Description: Calculate and display the purchase order price, including state and county taxes.
"""

# Define variables for taxation
# These are fixed tax rates: state tax is 5% (0.05) and county tax is 2.5% (0.025)
state_sales_tax = 0.05
county_sales_tax = 0.025

# Ask the user for the purchase order amount
# The program prompts the user to enter the total price of the purchase order
while True:
    try:
        # Input is taken as a string and converted to a floating-point number for calculations
        purchase_order = float(input("Enter the total price of your purchase order: "))
        # Ensures the user doesn't enter a negative amount
        if purchase_order < 0:
            print("Purchase order amount cannot be negative. Please try again.")
        else:
            break  # Exit the loop once a valid input is received
    except ValueError:
        # Handles cases where the user enters non-numeric input
        print("Invalid input. Please enter a valid number.")

# Calculate purchase order price
# Here, we assume the purchase price is equivalent to the purchase order amount
po_amount = purchase_order  # This is the base amount before tax is added

# Calculate and round the state and county sales tax
# State tax is calculated as 5% of the purchase order amount
state_tax = round(purchase_order * state_sales_tax, 2)
# County tax is calculated as 2.5% of the purchase order amount
county_tax = round(purchase_order * county_sales_tax, 2)
# The total amount is the sum of the purchase order amount, state tax, and county tax
total = round(state_tax + po_amount + county_tax, 2)

# Display sales report
# The results are displayed in a formatted table with properly aligned columns
# - Left alignment (<) for labels like "PO Amount," "State Tax," "Total"
# - Right alignment (>) for the dollar amounts to ensure numbers are visually aligned
print(f"\n{'PO Amount':<17}$    {purchase_order:<15.2f}")  # Base purchase order amount
print(f"{'State Tax':<17}$     {state_tax:<15.2f}")       # State tax amount
print(f"{'County Tax':<17}$     {county_tax:<15.2f}")     # County tax amount
print(f"{'Total':<17}$    {total:<15.2f}")               # Total amount including taxes
"""
The labels ("PO Amount," "State Tax," "County Tax," and "Total") are left-aligned using <17, 
ensuring they are positioned to the left and padded with spaces to 17 characters.
The dollar amounts (purchase_order, state_tax, county_tax, and total)
right-aligned within a 15-character space using <15.2f.
"""
