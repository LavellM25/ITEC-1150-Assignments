
"""
Author: Lavell McGrone
Date: 2024-09-26
Description: Calculate and display the total cost of purchasing textbooks based on user input.
"""

# Ask the user how many textbooks they need to buy
while True:
    num_books_input = input("How many textbooks do you have to buy? ")
    if num_books_input.isnumeric():
        num_books = int(num_books_input)
        break # If user enters in correct value then break the loop
    else:
        print("Please enter a whole number. ")

# Initialize the grand total
grand_total = 0

# Ask for the price of each book
for book in range(1, num_books + 1):
    price_input = input(f"Enter price for book #{book}: ")
    price = float(price_input)

    # Define variable for the grand total
    grand_total = (grand_total + price)

    # Provide the subtotal after each book is entered
    print(f"Subtotal = ${grand_total:.2f}. ")

# Provide the grand total after all books are entered
print(f"Grand total = ${grand_total:.2f}. ")
