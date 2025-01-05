"""
Author: Lavell McGrone
Date: 2024-24-11
Description: This program downloads a webpage, extracts text content using BeautifulSoup4, and displays it. Also,
it parses HTML websites to extract meaningful information or structure. For the purpose of web scraping, parsing
involves using tools like BeautifulSoup to break down a webpage's HTML into readable and usable components,
such as text or specific elements.
"""

import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
import pyinputplus as pyip  # For input validation


def main():
    # Intro welcome statement to the user
    print("\nWelcome to Lavell's Web Scraping Program!\n")
    print("This program downloads a webpage and extracts its text content using BeautifulSoup4.\n")

    while True:  # Create a loop for the following functions that will be later called.
        url = get_input()   # Input from the user
        html_content = process_webpage(url)   # Process the input based on what is inserted, access input accordingly.
        #  Call the parsing function to extract readable text from the HTML content
        extracted_text = process_parsing(html_content)
        display_output(extracted_text)  # Display the extracted text to the user
        # Ask the user if they want to restart or exit the program
        # If the user chooses not to restart, print a goodbye message and exit
        if not restart_program():
            print("Exiting the program. Goodbye!")
            break   # use break to exit the program


def get_input():  # Input Function
    while True:  # Start a while loop to keep asking for input until valid data is provided
        try:
            # Prompt the user to enter a URL and remove any leading or trailing spaces
            webpage_url = input("Enter the URL of the webpage you want to scrape: ").strip()

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


def process_webpage(webpage_url):  # Processing Function 1: Download Webpage
    try:
        # Inform the user that the program is trying to access the webpage
        print("\nAccessing the webpage...")

        # Send a GET request to the URL and set a timeout for the request
        response = requests.get(webpage_url, timeout=10)

        # Check if the request was successful
        # HTTP status code 200 indicates a successful response, the server has provided the requested webpage content.
        # If the status code is not 200, it means something went wrong, for example,
        # the webpage doesn't exist, there's a server issue, or the URL is invalid. This will prevent the program from
        # processing invalid or incomplete data, which could lead to errors later in the code.
        if response.status_code != 200:
            print("Error: Failed to access the webpage. Please check the URL and try again.")
            return process_webpage(get_input())  # Restart the process with a new URL

        # Validate if the URL points to an HTML page
        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            print("Error: The URL does not point to an HTML page. Please try a different URL.")
            return process_webpage(get_input())  # Restart the process with a new URL

        # If no issues, confirm the webpage was successfully accessed
        print("Webpage accessed successfully!")

        # Return the HTML content of the webpage as text
        return response.text

    # Handle exceptions for request errors (i.e. invalid URL)
    except requests.exceptions.RequestException as e:
        # This block will execute if any request-related error occurs (like a bad URL)

        # Inform the user about the error by printing the exception message (e)
        print(f"Error during webpage access: {e}")

        # After an error, restart the process by asking the user to input a new URL
        return process_webpage(get_input())  # Loop the function again after taking new input from the user
    except ValueError:  # If the webpage content is not HTML
        # Notify the user that the page is not HTML
        print("Error: The URL does not point to an HTML page.")

        # Ask for a new URL and retry
        return process_webpage(get_input())  # Loop through the function again with the new input


def process_parsing(html_content):  # Processing Function 2: Parse HTML Content
    try:
        # Step 1: Notify the user that the program is starting to parse the HTML content.
        print("\nParsing the webpage content...")

        # Step 2: Use BeautifulSoup to parse the HTML content, based on user input.
        # Use BeautifulSoup library used to process and navigate HTML pages.
        soup = BeautifulSoup(html_content, "html.parser")

        # Step 3: Extract the text from the parsed HTML
        # `soup.get_text()` will grab all visible text from the webpage and combine it into one large string.
        # Use "\n"` for a new line for better readability.
        extracted_text = soup.get_text(separator="\n").strip()  # Remove extra whitespace at the ends.

        # Step 4: If parsing was successful, notify the user accordingly.
        print("Parsing successful!")

        # Step 5: Return the extracted text so it can be used later.
        return extracted_text

    except Exception as e:
        # Step 6: If an error occurs during parsing (invalid HTML), print the error.
        # The variable `e` stores the error message and shows specific error to the user.
        print(f"An error occurred during parsing: {e}")

        # Step 7: Retry the parsing process by calling the same function again with the same input.
        # If there was a failure in parsing process, the program should attempt to fix it by trying again.
        return process_parsing(html_content)  # Restart parsing if it fails


def display_output(extracted_text):   # Output Function
    # Step 1: Print a heading for the extracted text output.
    # This helps inform the user what they are about to see, regarding the text from the webpage.
    print("\nExtracted Text from the Webpage:")

    # Step 2: Print a line of 40 dashes.
    # Create a clear boundary that is readable and organized.
    print("-" * 40)
    """
    Step 3 and 5 are optional and added this particular detail when debugging the code by myself with multitude of 
    different websites, not specifying a character limit from the website that will be extracted. For example, when 
    parsing a book with over 100 pages, would be shown in the console and that would be too much. I just played around 
    with the code and wanted to try something new. 
    """
    # Step 3 (optional): Display the first 1000 characters of the extracted text for readability.
    # Slice `extracted_text[:1000]` to ensure only the first 1000 characters are shown.
    # In the case the website is very large
    print(extracted_text[:1000])  # Display the first 1000 characters.

    # Step 4: Print another line of 40 dashes
    print("-" * 40)

    # Step 5 (Optional): Print a message informing the user only first 1000 characters will be shown.
    print("(Display the first 1000 characters)\n")


# Restart Program Prompt using pyinputplus
# inputYesNo ensures the user provides a valid yes or no response.
def restart_program():
    restart = pyip.inputYesNo("Would you like to scrape another webpage? (yes/no): ").lower()
    return restart == 'yes'

# Run the Main Function
if __name__ == "__main__":
    main()
