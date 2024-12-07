"""
Author: Lavell McGrone
Date: 2024-12-05
Description: Create, manage store and view contact information in a CSV file based on user-input.
             Users can add new contacts by entering their name, email, and phone number, or view all saved contacts.
             Ensure the program does not crash if the file doesn't exist or empty and handle errors accordingly.
"""
import csv
import os
import pyinputplus as pyip


# Here is the file created to store contact information based on user input
CONTACTS_FILE = "contacts.csv"
# Here is where the contacts.csv file that is stored locally on my computer
print(f"The contacts.csv file is stored at: {CONTACTS_FILE}")


def main():
    while True:
        user_choice = display_menu()
        if user_choice == "View":
            view_contacts()
        elif user_choice == "Add":
            add_contact()
        elif user_choice == "Exit":
            print("\nThanks for using the program!")
            break


def display_menu():
    # Display the menu using PyInputPlus with view, add, and exit being the options
    menu_options = ["View", "Add", "Exit"]
    # Use numbered=True so that when users type 1, 2, or 3 to select an option instead of typing the full text.
    return pyip.inputMenu(menu_options, numbered=True)


def view_contacts():
    """Based on user input, read and display all the contact information from the contacts.csv file. Additionally,
    based on the requirements of the assignment, ensure the program does not crash if a file does not exist"""
    #  1) Check os.path.exists() if the file path specified by CONTACTS_FILE exists.
    # Display all contacts from the CSV file, handle error accordingly if the file don't exist to avoid crash.
    if not os.path.exists(CONTACTS_FILE):
        print("\nNo contacts found. The file does not exist yet.")
        return

    # 2) Open and Read the CSV File. Open the file in read mode ('r') and read its contents (based on user-input).
    with open(CONTACTS_FILE, mode='r') as file:
        # csv.DictReader(file) job is to read the CSV file and convert each row like a dictionary.
        # The csv.DictReader(file) creates keys in a dictionary to designate as column headers (like Name, Email, Phone)
        reader = csv.DictReader(file)
        # list(reader) makes a list of dictionaries
        contacts = list(reader)
        if not contacts:   # 3) Handle errors incase the CSV file does not have any info yet from user.
            print("\nNo contacts to display.")
        else:  # 4) If the CSV file exists and there is content to show the user, display the contacts.
            print("\nName\t\tEmail\t\t\tPhone")  # Display the contacts with "\\t" for double tab for horizontal spacing
            print("-" * 50)
            for contact in contacts:  # Create a loop that will loop through the contact list and print each contact
                print(f"{contact['Name']}\t{contact['Email']}\t{contact['Phone']}")


def add_contact():
    """ Prompts the user to enter a new contact's name, email, and phone number, and saves the information to the
    contacts.csv file. If the file doesn't exist, create the file and adds a column titles."""

    # 1) Prompt the user to enter new contact information
    # use the pyip.inputStr() method to ensure user string is entered, .strip() to remove not needed spaces
    # pyip.inputEmail(): Validates that the entered email follows the correct email format (e.g., user@example.com
    print("\nEnter the contact details:")
    name = pyip.inputStr("Enter the contact's name: ").strip()
    email = pyip.inputEmail("Enter the contact's email: ").strip()
    phone = pyip.inputStr("Enter the contact's phone: ").strip()

    # 2) If the file exists, the next step I will need to do next is create a column titles
    file_exists = os.path.exists(CONTACTS_FILE)

    # 3) Open the file in append mode. Add contents to .csv in append mode to not overwrite previous data
    with open(CONTACTS_FILE, mode='a', newline='') as file:
        # 4) Define column titles for the CSV file
        fieldnames = ['Name', 'Email', 'Phone']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # 5) Write column titles only if the file is new and did not exist previously
        if not file_exists:
            writer.writeheader()

        # 6) Add the new contact’s details as a row in the CSV file.
        # writer.writerow() creates a dictionary, where keys ('Name', 'Email', 'Phone') match the column titles
        writer.writerow({'Name': name, 'Email': email, 'Phone': phone})
    print("\nContact added successfully!")  # Print feedback once this has been completed


if __name__ == "__main__":  # Run the program
    main()
