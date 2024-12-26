"""
Author: Lavell McGrone
Date: 2024-10-27
Description: Collects, validates, and formats feedback phrases ensuring proper capitalization and punctuation.
"""


def main():
    """
    Main function to run the feedback collector program.
    """
    print("Welcome to the feedback generator.")

    while True:
        try:
            feedback_input = get_feedback()  # Get feedback phrases from user
            feedback_list = process_feedback(feedback_input)  # Process and format the feedback phrases
            outputs(feedback_list)  # Output the formatted feedback list

            # Prompt for restart
            restart = input("\nWould you like to try again? Enter y or n: ").strip().lower()
            if restart == 'y':  # Restart the program
                print("\nRestarting the program...\n")
                main()  # Restart from the beginning
                return  # Exit the current instance of main to prevent duplicate runs
            elif restart == 'n':  # Exit the program
                print("Thanks for helping us build our feedback library.")
                return
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        except Exception as err:
            print(f"An error occurred: {err}")  # Handle unexpected errors and allow the program to restart


def get_feedback():
    """
    Prompt the user to enter feedback phrases and validate the input.
    Ensure the user does not put in numbers.
    Ensure the user input ends with an exclamation mark.
    :return: A valid feedback string if no issues are found.
    """
    while True:
        # Ask for user input
        feedback = input("Please enter multiple feedback phrases, each ending in an exclamation point: ").strip()
        # Check if input is empty or only spaces
        if not feedback or feedback.isspace():
            print("The input cannot be blank or only spaces. Please try again.")
        # Check if input contains any numbers using a for loop
        else:
            #  Begin with variable 'has_number' to False, assume user doesn't have numbers in 'feedback'.
            has_number = False
            for character in feedback:
                if character.isdigit():  # Check if the current character is a digit
                    has_number = True   # Set 'has_number' to True if a number is found.
                    break  # Exit loop if one number is found.
            if has_number:
                print("Feedback should not contain numbers. Please enter only text phrases. ")
            # Check if there is at least one exclamation mark
            elif '!' not in feedback:
                print("Each phrase must end in an exclamation point. Please try again.")
            # If input passes all checks, return the feedback
            else:
                print("Here are your feedback phrases: ")
                return feedback


def process_feedback(feedback):
    """
    Process the feedback by cleaning, capitalizing, and adding exclamation points.
    :param feedback: The raw input string from the user.
    :return: A list of corrected feedback phrases.
    """
    # Split the feedback based on '!' but exclude any empty entries by filtering
    raw_phrases = [phrase.strip() for phrase in feedback.split('!') if phrase.strip()]
    # Create an empty list to store the corrected phrases
    corrected_phrases = []
    for phrase in raw_phrases:    # Loop through each phrase in the list of raw phrases
        # Capitalize the first letter, remove extra spaces, and add the exclamation point
        corrected_phrases.append(f"{phrase.capitalize()}!")
    return corrected_phrases   # Return the final list of corrected feedback phrases


def outputs(feedback_list):
    """
    Display the corrected list of feedback phrases.
    :param feedback_list: A list of formatted feedback phrases.
    :return: None
    """
    print("\nHere are your feedback phrases:")    # Print message to the user to introduce the list of feedback phrases
    for idx, phrase in enumerate(feedback_list, start=1):  # Access each item in feedback_list with feedback_list[idx]
        print(f"{idx}: {phrase}")    # Add 1 to idx so numbering start from 1 instead of 0 for readability
    print()     # Add extra line for spacing purposes


# Start the program
main()
