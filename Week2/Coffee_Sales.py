"""
Author: Lavell McGrone
Date: 2024-09-16
Description: Calculate and display coffee sales
"""

# Ask the user for the price and number of cups sold for each drink type
coffee_price = float(input("What was the price of coffee? "))
coffee_sold = float(input("How many cups of coffee sold? "))

tea_price = float(input("What was the price of tea? "))
tea_sold = float(input("How many cups of tea sold? "))

cappuccino_price = float(input("Enter the price of cappuccino "))
cappuccino_sold = float(input("Enter the number of cups of cappuccino sold "))

# Calculate the total cost for each drink type
coffee_total = coffee_sold * coffee_price
tea_total = tea_sold * tea_price
cappuccino_total = cappuccino_sold * cappuccino_price

# Calculate total of all drink types
total_cups_sold = coffee_sold + tea_sold + cappuccino_sold
total_revenue = coffee_total + tea_total + cappuccino_total

# Display results of total drink types with proper alignment
print(f"{'Drink Type':<12} {'Cups Sold':<10}{'Price':>11}    {'Total':>17}")
print(f"{'Coffee':<12} {coffee_sold:<10.0f} ${coffee_price:>9.2f}     ${coffee_total:>16.2f}")
print(f"{'Tea':<12} {tea_sold:<10.0f} ${tea_price:>9.2f}     ${tea_total:>16.2f}")
print(f"{'Cappuccino':<12} {cappuccino_sold:<10.0f} ${cappuccino_price:>9.2f}     ${cappuccino_total:>16.2f}")
print(f"{'Total':<12} {total_cups_sold:<10.0f} {'':>11}    ${total_revenue:>16.2f}")
