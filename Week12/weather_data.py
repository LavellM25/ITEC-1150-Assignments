"""
Author: Lavell McGrone
Date: 2024-24-11
Description: Will accept a weather forecast URL from the user, downloads the page, and extracts forecast data.
If successful, it displays the weather conditions and time periods in a formatted table. If errors occur, the user is
prompted to try again.
"""

import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
import pyinputplus as pyip  # For input validation


def main():
    # Intro welcome statement to the user
    print("\nWelcome to the Weather Forecast Program!")
    print("This program downloads the weather forecast page and displays the forecast data.\n")

    while True:  # Create a loop for the following functions that will be later called.
        url = get_input()  # Get the URL from the user
        forecast_labels, forecast_text = process_webpage(url)  # Process the webpage and extract forecast data
        if forecast_labels and forecast_text:  # If data was extracted
            display_output(forecast_labels, forecast_text)  # Display the forecast data
        else:
            print("No data found. Please try again.\n")
            # Ask the user if they want to restart or exit the program
            # If the user chooses not to restart, print a goodbye message and exit
            if not restart_program():
                print("Exiting the program. Goodbye!")
            break


def get_input():   # Input Function: Get URL from the user
    while True:  # Start a while loop to keep asking for input until valid data is provided
        try:
            # Prompt the user to enter a URL and remove any leading or trailing spaces
            webpage_url = input("Enter the URL for the weather forecast: ").strip()
            # Check if the input is blank
            if not webpage_url:
                # If the input is blank, display an error message
                print("Error: The URL cannot be blank. Please try again.")
            else:
                # If the URL is valid (not blank), return it to be used by the rest of the program
                return webpage_url
        except ValueError as e:  # Handle the error if the input is invalid
            # The as e part stores the error message as a variable (e), so then (e) inserts actual error message to user
            # Inform the user about the error and prompt them to try again
            print(f"Invalid input: {e}")


def process_webpage(webpage_url):  # Processing Function: Download and Parse Webpage
    """
    This function is supposed to access the provided URL and extract weather data.
    If unsuccessful, it should handle errors and prompts the user to try again.
    """
    try:
        # Step 1: Inform the user that the program is attempting to access the webpage
        print("\nAccessing the webpage...")

        # Step 2: Send a GET request to the provided URL with a timeout of 10 seconds
        response = requests.get(webpage_url, timeout=10)

        # Step 3: Check if the status code is not 200 (success). If it's not, inform the user and restart.
        # HTTP status code 200 indicates a successful response, the server has provided the requested webpage content.
        # If the status code is not 200, it means something went wrong, for example,
        # the webpage doesn't exist, there's a server issue, or the URL is invalid. This will prevent the program from
        # processing invalid or incomplete data, which could lead to errors later in the code.
        if response.status_code != 200:
            print(f"Error encountered - Received status code {response.status_code}.")
            print("The webpage could not be accessed. Please try again with a valid URL.")
            return process_webpage(get_input())  # Restart with a new URL

        # Step 4: Check if the content type of the response is not HTML
        if "text/html" not in response.headers.get("Content-Type", ""):
            print("Error encountered - The URL does not point to an HTML page.")
            print("Please try again with a valid URL pointing to an HTML page.")
            return process_webpage(get_input())  # Restart with a new URL

        # Step 5: If the status code is 200 and content type is valid, inform the user of success
        print("Webpage accessed successfully!")
        print("\nExtracting forecast data from the webpage...")

        # Step 6: Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 7: Extract forecast labels (time periods) from elements with the class 'forecast-label'
        forecast_labels = [label.get_text() for label in soup.find_all(class_="forecast-label")]

        # Step 8: Extract forecast text (weather descriptions) from elements with the class 'forecast-text'
        forecast_text = [text.get_text() for text in soup.find_all(class_="forecast-text")]

        # Step 9: Return the two lists (labels and text) for further processing
        return forecast_labels, forecast_text

    except requests.exceptions.RequestException as e:
        # Step 10: Handle any request-related errors (invalid URL or network crashes)
        print(f"Error during webpage access: {e}")
        print("Please check the URL or your internet connection and try again.")
        return process_webpage(get_input())  # Restart with a new URL


def display_output(forecast_labels, forecast_text):
    """
    Displays the weather forecast by printing labels and text side by side.
    """
    # Step 1: Inform the user that the weather forecast will be displayed
    print("\nStep 1: Displaying the weather forecast:\n")
    print("-" * 40)  # Step 2: Create a separator line for clarity

    # Step 3: Check if both lists have the same length to avoid errors
    if len(forecast_labels) != len(forecast_text):
        print("Error: Forecast labels and text data do not match in length.")
        print("Please ensure the webpage has valid weather data.")
        return  # Exit the function if data is inconsistent

    # Step 4: Loop through the lists using an index-based approach
    for i in range(len(forecast_labels)):
        label = forecast_labels[i]  # Get the current label
        text = forecast_text[i]    # Get the corresponding text
        print(f"{label}: {text}")  # Step 5: Print the label and text together
        '''
        Erik: -0.5
            The output needs to be in two columns for readability.
        '''

    # Step 6: Print a closing separator line
    print("-" * 40)



# Restart Program Prompt using pyinputplus
# inputYesNo ensures the user provides a valid yes or no response.
def restart_program():
    restart = pyip.inputYesNo("Would you like to scrape another webpage? (yes/no): ").lower()
    return restart == 'yes'


# Start the program by calling the main function
if __name__ == "__main__":
    main()
