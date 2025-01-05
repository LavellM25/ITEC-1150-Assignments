"""
Author: Lavell McGrone
Date: 2024-18-11
Description: View existing users, add new users with usernames and emails, validate input, store data in a file.
"""


import pyinputplus as pyip


def main():
    """Main function to handle the user menu."""
    initialize_user_file()

    while True:
        choice = pyip.inputMenu(["view", "add", "exit"], numbered=True,)
        if choice == "view":
            view_users()
        elif choice == "add":
            add_users()
        elif choice == "exit":
            print("Thanks for using the program.")
            break


def initialize_user_file():
    """Initialize the user file with at least one record if it doesn't exist."""
    try:
        # Attempt to open the file in exclusive creation mode
        file = open("user_manager_txt", "x")  # mode "x" is used to create a new file named user_manager_txt.
        # Write the default user record, username = lmcgrone meets the requirements of no-space requirement
        # lmcgrone@minnstate.edu (a valid email format), \n (new line)
        file.write("lmcgrone lmcgrone@minnstate.edu\n")
        # Close the file manually
        file.close()
    except FileExistsError:
        # If the file already exists, print a message
        print("File already exists, no need to initialize.")


def view_users():
    """Read and display the contents of the user file."""
    try:
        # Open the file manually
        file = open("user_manager_txt", "r")  # Open the file in read mode
        lines = file.readlines()  # Read all lines from the file

        # Check if the file has any content, and if the file is empty or all lines are blank
        # The condition if not lines or all(line.strip() == "" for line in lines): ensures that the program checks
        # if the file is empty or contains only blank lines.
        # If not, print error message accordingly.
        if not lines or all(line.strip() == "" for line in lines):
            print("\nThere are no users to view. Please add users before viewing.\n")
        else:
            for line in lines:
                # Strip the line and check if it contains data
                stripped_line = line.strip()
                if stripped_line:  # Ignore empty lines
                    parts = stripped_line.split(" ")
                    if len(parts) == 2:  # Ensure there are exactly two parts: (username and email) after splitting.
                        username, email = parts
                        # {username:<15}: Username is left-aligned with a width of 15.
                        # {email:>30}: Email is right-aligned with a width of 30, enough space for large emails.
                        print(f"Username: {username:<15} Email:{email:>30}")
                    else:
                        print(f"Invalid entry found in file: {stripped_line}")
        file.close()  # Close the file manually
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Error: The user file does not exist. Please restart the program.")


def add_users():
    """Prompt the user to enter one or more users and write them to the file."""

    # 1. Prompt user input for usernames and emails.
    # The user is asked to enter multiple records separated by commas in the format 'username email'.
    user_input = pyip.inputStr(
        "Please enter users in the format 'username email'. Separate multiple records with commas: "
    )

    # 2. Split the input into individual user records and clean whitespace.
    # This step removes unnecessary spaces and filters out empty records.
    # The `strip()` ensures no trailing or leading spaces are included.
    user_records = [user.strip() for user in user_input.split(",") if user.strip()]

    # 3. Check if any valid records were provided.
    # If the list `user_records` is empty, print a message and exit the function.
    if not user_records:
        print("No valid user entries provided.")
        return  # Exit the function if no valid input is detected.

    file = None
    # 4. Try to open the file in append mode.
    # Append mode ('a') adds new content to the end of the file without overwriting existing data.
    try:
        file = open("user_manager_txt", "a")  # Open the file for appending
        for record in user_records:  # Loop through each user record.
            # 5. Split each record into parts: username and email.
            # This ensures the input contains exactly two parts separated by a space.
            parts = record.split(" ")
            # 6. Validate that the record has two parts and the second part contains '@' for an email address.
            if len(parts) == 2 and "@" in parts[1]:
                # 7. Write the valid record to the file, adding a newline character at the end.
                file.write(record + "\n")
            else:
                # 8. Handle invalid records by displaying an error message.
                print(f"Invalid record skipped: {record}")
        # 9. Confirm successful addition of valid records to the file.
        print("Users added successfully.")
    except FileNotFoundError:
        # 10. Handle the case where the file does not exist.
        # This error would occur if the file was deleted or not initialized properly.
        print("Error: The user file does not exist. Please restart the program.")
        file.close()   # Close the file


main()
