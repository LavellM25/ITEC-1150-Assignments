"""
Author: Lavell McGrone
Date: 2024-10-13
Description: Calculate book titles and prices, then displays a summary with total and average costs based on user input.
"""


def main():
    """
    Main execution control method.
    :return: None
    """
    print("This program summarizes a book list.")  # Print introductory statement to the user
    try:
        num_books, book_list, price_list = inputs()  # Get number of books, titles, and their prices
        total, average = processing(price_list)  # Calculate total and average price
        outputs(num_books, book_list, price_list, total, average)  # Display the results
        while True:  # Loop until a valid input is received
            restart = input("\nWould you like to generate another list? Enter y or n: ")
            if restart.lower() == 'y':  # Check for 'y' or 'Y'
                print("Generating a new list.")
                main()  # Restart the program
                break  # Exit the loop after restarting
            elif restart.lower() == 'n':  # Check for 'n' or 'N'
                print("Thanks for using the program!")
                break  # Exit the loop, if user enters correct value
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")  # Error message for invalid input
    except Exception as err:
        print(f"An error occurred: {err}")  # Handle any unexpected errors and prompt for restart
        main()  # Restart the program


def inputs():
    """
    Collect the number of books, book titles, and the price for each book.
    :return: num_books: Number of books the user needs (int).
    :return: books_list: List of book titles.
    :return: price_list: List of prices for each book.
    """
    print("Enter the number of books that you need. ")
    num_books = get_pos_int()  # Validate and get the number of books
    book_list = []  # List to store book titles
    price_list = []  # List to store book prices

    # Collect the title and price for each book
    for index in range(num_books):
        book_title = input("Enter the book title: ")  # Get book title
        book_list.append(book_title)  # Add title to book list
        print(f"Enter the cost of book#{index + 1}, to the nearest dollar: ")
        book_cost = get_pos_int()  # Validate and get book price from the user
        price_list.append(book_cost)  # Add price to price list, given the user input

    return num_books, book_list, price_list


def get_pos_int():
    """
    Validates that the user inputs a positive integer.
    :return: pos_int: Validated positive integer from the user.
    """
    while True:
        pos_int = input("Please enter a whole number: ")
        try:
            pos_int = int(pos_int)  # Try converting input to an integer
            if pos_int > 0:  # Check if it's a positive number
                return pos_int  # Return if valid
            else:
                print("Enter a number greater than 0. ")
        except ValueError:
            # Handle non-integer inputs that does not meet the above requirements
            print("Invalid input. Please enter a valid whole number. ")


def processing(price_list):
    """
    Calculate the total and average cost of the books.
    :param: price_list: List of book prices.
    :return: total: Total cost of the books.
    :return: Average cost of the books, rounded to two decimal places.
    """
    total = sum(price_list)  # Calculate the total sum of book prices
    price_list_len = len(price_list)  # This is how many prices we have
    average = total / price_list_len  # Calculate the average price
    average_rounded = round(average, 2)  # Round the average to two decimals
    return total, average_rounded  # Return the total and the rounded average


def outputs(num_books, book_list, price_list, total, average):
    """
    Display the price of each book along with its title, as well as the total and average cost.
    :param: num_books: Number of books, integer that is > 0.
    :param: book_list: List of book titles.
    :param: price_list: List of book prices.
    :param: total: Total cost of the books rounded to two decimal places.
    :param: average: Average cost of the books rounded to two decimal places.
    """
    print(f"Info on {num_books} Books Needed ")
    print(f'{"Book#":<40}{"Price":>10}')

    # Display each book's title and price
    for index in range(num_books):
        print(f"{book_list[index]:<40} ${price_list[index]:>8.2f}")

    # Display total and average price
    print(f'{"Total":<40} ${total:>8.2f}')      # Total cost of the books rounded to two decimal places.
    print(f'{"Average":<40} ${average:>8.2f}')  # Average cost of the books rounded to two decimal places.


main()  # Start the program
