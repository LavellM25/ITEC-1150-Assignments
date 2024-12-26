"""
Author: Lavell McGrone
Date: 2024-20-10
Description: Manage authors and book titles with options to view, add, edit, and delete readings.
"""


def main():
    """
    Main execution control method.
    :return: None
    """
    print("Welcome to the Reading List Management Program.")  # Print the introductory statement

    try:
        # Define the readings of authors and book titles
        readings = {
            'alice smith': 'Python Primer',
            'bill bower': 'Clojure Code',
            'hassan hassan': 'Deep Learning Dive',
            'carol smith': 'Dora The Explorer'}

        display_menu()   # Display the command menu to the user
        print()  # Extra line for spacing
        while True:
            command = get_command()  # Prompt user for a command (e.g., view, add, edit, etc.)
            readings = processing(command, readings)  # Process the input command and update readings

            # Ask the user if they want to continue or exit the program
            while True:  # Loop until a valid input is received
                restart = input("\nWould you like to continue? Enter y or n: ").lower()
                if restart == 'y':  # If the user wants to continue
                    print("\nRestarting the program...")
                    display_menu()  # Show the menu again when restarting
                    print()  # Extra line for spacing
                    break  # Exit this loop and continue with the main loop
                elif restart == 'n':  # If the user wants to exit
                    print("Thanks for using the program!")
                    return  # End the program
                else:   # Prompt the user to enter valid input
                    print("Invalid input. Please enter 'y' for yes or 'n' for no.")
    except Exception as err:
        # If any unexpected errors occur, handle them gracefully.
        print(f"An error occurred: {err}")  # Display the error message
        display_menu()  # Redisplay the menu instead of restarting the entire program


def get_command():
    """
    Get user command input and validate it.
    :return: A valid command from one of the few options (view, add, edit, del, exit)
    """
    return input("Command: ").lower()   # Ensure input is lowercase-sensitive


def processing(command, readings):
    """
    Process the user input and perform actions accordingly.
    :param command: The command entered by the user.
    :param readings: Dictionary of authors and book titles.
    :return: Updated readings from the dictionary.
    """
    if command == 'view':
        view(readings)  # View the readings list
    elif command == 'add':
        add(readings)  # Add a new reading
    elif command == 'edit':
        edit(readings)  # Edit an existing reading
    elif command == 'del':
        delete(readings)  # Delete a reading
    elif command == 'exit':
        print("Bye!")  # Exit message
        return readings  # Return the readings unchanged
    else:
        print("Not a valid command. Please try again.\n")  # Resolve invalid commands
        display_menu()  # Redisplay the menu after an invalid command
    return readings  # Return the updated readings list


def outputs(message):
    """
    Output a given message.
    :param message: Message to display to the user.
    :return: None
    """
    print(message)


def display_menu():
    """
    Display the available command menu.
    :return: None
    """
    outputs("COMMAND MENU")  # Display the command menu title
    outputs("view  - View the reading list")
    outputs("add   - Add a reading")
    outputs("edit  - Edit a reading")
    outputs("del   - Delete a reading")
    outputs("exit  - Exit program")


def view(readings):
    """
    View the reading list by entering an author's name.
    :param readings: Dictionary of authors and book titles.
    :return: None
    """
    print("Authors: " + ", ".join([author.title() for author in readings.keys()]))  # Display list of authors
    author = input("Enter the name of the reading author to view: ").lower()  # Ensure input is lowercase-sensitive
    if author in readings:
        title = readings[author].title()  # Get the title associated with the author
        outputs(f"Title: {title}.\n")  # Output the title in proper title case
    else:
        outputs("There is no reading with that author name.\n")  # If the author doesn't exist, notify the user


def add(readings):
    """
    Add a new reading by entering an author and book title.
    :param readings: Dictionary of authors and book titles.
    :return: None
    """
    print("Authors: " + ", ".join([author.title() for author in readings.keys()]))  # Display list of authors
    author = input("Enter the author for the new reading: ").lower()  # Ensure input is lowercase-sensitive
    if author in readings:
        outputs(readings[author].title() + " is already associated with this author.\n")  # If author exists, notify
    else:
        title = input("Enter the title of the reading: ").title()  # Store the title in title case
        readings[author] = title  # Add the new author and title to the dictionary
        outputs(f"Author {author.title()} and title {title} were added.\n")  # Notify user that the reading was added


def edit(readings):
    """
    Edit the title of an existing reading.
    :param readings: Dictionary of authors and book titles.
    :return: None
    """
    print("Authors: " + ", ".join([author.title() for author in readings.keys()]))  # Display list of authors
    author = input("Enter the author to edit: ").lower()  # Ensure input is lowercase-sensitive
    if author in readings:
        # If the author of the book exists, prompt the user to enter the new title of the book
        title = input(f"Enter the new title for {author.title()}: ").title()  # Ask for the new title
        readings[author] = title  # Update the dictionary with the new title
        outputs(f"The reading for {author.title()} has been updated to the title {title}.\n")  # Confirm the update
    else:
        outputs("There is no reading with that author name.\n")  # If the author doesn't exist, notify the user


def delete(readings):
    """
    Delete a reading from the list.
    :param readings: Dictionary of authors and book titles.
    :return: None
    """
    while True:  # Loop to allow retry if input is wrong
        # Display both authors and their book titles
        print("Current Readings:")
        for author, title in readings.items():
            print(f"{author.title()} - {title.title()}")  # Show both author and title in title case
        # Prompt user to input the author to delete
        author = input("\nEnter the author of the reading to delete: ").lower()
        if author in readings:
            title = readings.pop(author).title()  # Remove the reading and get the title
            outputs(f"Author {author.title()} and title {title} were deleted.\n")  # Notify the user
            break  # Exit the loop after successful deletion
        else:
            # If the input is incorrect, show available authors and book titles again
            outputs(f"There is no reading with the author name '{author.title()}'.\n")
            retry = input("Would you like to try deleting another reading? (y/n): ").lower()
            if retry != 'y':  # If the user doesn't want to retry, exit the function
                outputs("Returning to the main menu.\n")
                break  # Exit the outer while loop and return to main


if __name__ == "__main__":
    main()
