"""
Author: Lavell McGrone
Date: 2024-11-14
Description: Utilize pyintputplus that book titles and prices, calculates total
average cost, and displays formatted information with validation based on user input.
"""

import pyinputplus as pyip  # Importing PyInputPlus for input validation


def main():
    """
    Main function to initiate the book list program, collect book data,
    calculate totals, and display information in a formatted table.
    """
    print("Welcome to the book list program.")  # Greeting message for the user

    # Ask the user for the number of books, using PyInputPlus to ensure input is a positive integer
    num_books = pyip.inputInt("\nEnter the number of books needed: ", min=1)

    # Function to collect book titles and prices
    book_titles, book_prices = get_book_info(num_books)

    # Calculate the total and average cost of the books
    total_cost, average_cost = calculate_totals(book_prices)

    # Display all information in a nicely formatted summary table
    display_summary(book_titles, book_prices, total_cost, average_cost)

    restart_program()   # Ask if the user wants to restart the program


def get_book_info(num_books):
    """
    Input function to gather titles and prices for each book.
    :param num_books: Number of books to get information for
    :return: A tuple containing lists of book titles and book prices
    """
    book_titles = []  # List to store book titles
    book_prices = []  # List to store book prices

    # Loop through the number of books specified by the user
    for i in range(1, num_books + 1):  # have num_books + 1, so it's user-friendly and don't start at 0.
        # Prompt for the book title with validation to ensure it's not blank, by using Blank=False
        # The user must enter some text, if the user simply presses enter without typing anything, won't accept input.
        title = pyip.inputStr(f"Enter the title of book #{i}: ", blank=False)
        book_titles.append(title.title())  # Add the book title to the list in title-case format

        # Prompt for the book price with validation to ensure it's between $1.00 and $100.00
        price = pyip.inputFloat("Enter the price: $ ", min=1.00, max=100.00)
        book_prices.append(price)  # Add the price to the list of book prices

    return book_titles, book_prices   # Return both lists (titles and prices) so other functions can use them


def calculate_totals(book_prices):
    """
    Processing function to calculate the total and average cost of books.
    :param book_prices: List of book prices
    :return: A tuple containing the total and average cost
    """
    total_cost = sum(book_prices)  # Sum all prices to get the total cost
    # Calculate average by dividing total by the number of books, total_cost / len(book_prices)
    # If book_prices else 0 part; handles if book_prices are an empty list which then len(book_prices) would be 0
    # which would cause a division by zero error.
    # Instead, the condition ensures that if the list is empty, average_cost is set to 0
    average_cost = total_cost / len(book_prices) if book_prices else 0
    return total_cost, average_cost  # Return both total and average cost


def display_summary(book_titles, book_prices, total_cost, average_cost):
    """
    Output function to display the book titles, prices, total cost, and average cost in a formatted table.
    :param book_titles: List of book titles
    :param book_prices: List of book prices
    :param total_cost: Total cost of all books
    :param average_cost: Average cost of the books
    """
    print("\nInfo on the books needed:")  # Print the section title.
    print(f"{'Title':<25}{'Price':>10}")  # Table header: Title and Price.
    print("-" * 45)  # Separator line.

    # Loop through the indices of the book_titles list.
    for i in range(len(book_titles)):
        title = book_titles[i]  # Make a book title from the book_titles list using current index (i) of the loop.
        price = book_prices[i]  # Make a book price from the book_prices list using the same index (i).

        # Print each title and price, formatted in a table.
        print(f"{title:<25} $ {price:>7.2f}")

    # Display the total and average cost in a formatted table.
    print("-" * 45)  # Another separator line.
    print(f"{'Total':<25} $ {total_cost:>7.2f}")
    print(f"{'Average':<25} $ {average_cost:>7.2f}")


def restart_program():
    """
    Asks the user if they want to start a new order.
    Restarts the program if yes, exits if no.
    """
    # Ask the user if they want to start a new order using 'yes' or 'no'
    choice = pyip.inputYesNo("\nDo you want to enter more books? Enter yes/no: ")
    if choice == "yes":
        main()  # Restarts the main program if user says yes
    else:
        print("Thank you for using the book list program. Goodbye!")  # Goodbye message if user says no


# Start the program by calling the main function
if __name__ == "__main__":
    main()
