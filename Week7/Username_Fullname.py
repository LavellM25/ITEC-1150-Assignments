"""
Author: Lavell McGrone
Date: 2024-20-10
Description: Manage usernames and full names with options to view, add, edit, and delete users.
"""


def main():
    """
    Main execution control method.
    :return: None
    """
    print("Welcome to the Username and Full Name Management Program.")  # Print the introductory statement

    try:
        # Define the variables for the usernames for the users
        users = {'hhassan': 'Hassan Hadi', 'jdoe': 'Jane Doe', 'jsmith': 'John Smith', 'sstudent': 'Sally Strudel'}

        display_menu()   # Display to the user possible commands they can use in the program
        print()    # Extra line for spacing
        while True:
            command = inputs()  # Prompt user for input command (e.g., view, add, edit, etc.)
            users = processing(command, users)  # Process the input command and return updated user data

            # Ask the user if they want to continue or exit the program
            while True:  # Loop until a valid input is received
                restart = input("Would you like to continue? Enter y or n: ").lower()
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
        # If any unexpected errors occur, this will block the error message and display to the user what happened.
        print(f"An error occurred: {err}")  # Display error message
        main()  # Restart the program after an error


def inputs():
    """
    Get user command input and validate it.
    :return: A valid command from one of the few options (view, add, edit, del, exit)
    """
    # Prompt the user for a command.
    return input("Command: ").lower()   # Use the .lower so 'H' or 'h' is treated the same and handled with no errors.


def processing(command, users):
    """
    Process the user input and perform actions accordingly.
    :param command: The command entered by the user.
    :param users: Dictionary of usernames and full names.
    :return: Updated users from the dictionary.
    """
    # Match the command to the appropriate function
    if command == 'view':
        view(users)  # If 'view', call the view function
    elif command == 'add':
        add(users)  # If 'add', call the add function
    elif command == 'edit':
        edit(users)  # If 'edit', call the edit function
    elif command == 'del':
        delete(users)  # If 'del', call the delete function
    elif command == 'exit':
        print("Bye!")  # Exit message
        return users  # Return users unchanged
    else:
        print("Not a valid command. Please try again.\n")  # Resolve users input that are a invalid command.
    return users  # Return the (possibly) updated users list


def outputs(message):
    """
    Output a given message.
    :param message: Message to display to the user.
    :return: None
    """
    # Output the passed message to the user
    print(message)


def display_menu():
    """
    Display the available command menu.
    :return: None
    """
    # Show the user the list of commands they can use
    outputs("COMMAND MENU")  # Display the command menu title
    outputs("view  - View user name")
    outputs("add   - Add a user")
    outputs("edit  - Edit a user")
    outputs("del   - Delete a user")
    outputs("exit  - Exit program")


def view(users):
    """
    View a user's full name by entering a username.
    :param users: Dictionary of usernames and full names.
    :return: None
    """
    username = input("Enter username to view: ").lower()  # Ask for a username to view, and convert to lowercase
    if username in users:
        full_name = users[username]  # Get the full name associated with the username
        outputs(f"Full name: {full_name}.\n")  # Output the full name
    else:
        outputs("There is no user with that username.\n")  # If the username doesn't exist, notify the user


def add(users):    # Add a new user
    """
    Add a new user by entering a username and full name.
    :param users: Dictionary of usernames and full names.
    :return: Users (updated dictionary)
    """
    username = input("Enter new username to add: ").lower()  # Ask for the new username, convert to lowercase
    if username in users:
        # If the username already exists, notify the user
        outputs(users[username] + " is already using this username.\n")
    else:
        full_name = input("Enter full name: ").title()  # Ask for the full name, convert to title case
        users[username] = full_name  # Add the new username and full name to the dictionary
        outputs(full_name + " was added.\n")  # Notify the user that the user was added
    return users   # Return the updated dictionary


def edit(users):     # Edit a user from the dictionary
    """
    Edit the full name of an existing user.
    :param users: Dictionary of usernames and full names.
    :return: Users (updated from dictionary)
    """
    username = input("Enter username to edit: ").lower()  # Ask for the username to edit, convert to lowercase
    if username in users:
        # If the username exists, prompt for the new full name
        full_name = input("Enter the new full name of the user: ").title()  # Convert to title case
        users[username] = full_name  # Update the dictionary with the new full name
        outputs(f"xt5506ys has been updated to the full name {full_name}.\n")  # Confirm the update
    else:
        # If the username doesn't exist, notify the user
        outputs("There is no user with that username.\n")
    return users   # Return the updated dictionary


def delete(users):
    """
    Delete a user from the list.
    :param users: Dictionary of usernames and full names.
    :return: Users (updated from dictionary)
    """
    username = input("Enter username to delete: ").lower()  # Ask for the username to delete, convert to lowercase
    if username in users:
        full_name = users.pop(username)  # Remove the user from the dictionary and return the full name
        outputs(full_name + " was deleted.\n")  # Notify the user that the user was deleted
    else:
        outputs("There is no user with that username.\n")  # If the username doesn't exist, notify the user
    return users    # Return the updated dictionary


if __name__ == "__main__":
    main()
