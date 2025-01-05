"""
Author: Lavell McGrone  
Date: 2024-11-24  
Description: This program accepts a weather forecast URL from the user, downloads the page, and extracts forecast data.  
If successful, it displays the weather conditions and time periods in a formatted table. If errors occur, the user is  
prompted to try again.  
"""

import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
import pyinputplus as pyip  # For input validation


def main():
    """Main function to drive the program workflow."""
    print("\nWelcome to the Weather Forecast Program!")
    print("This program downloads a weather forecast page and displays the forecast data.\n")

    while True:
        url = get_input()  # Get the forecast URL from the user
        forecast_labels, forecast_text = process_webpage(url)  # Extract weather data from the webpage

        if forecast_labels and forecast_text:  # If data extraction is successful
            display_output(forecast_labels, forecast_text)  # Display the formatted forecast data
        else:
            print("No data found. Please try again.\n")

        # Prompt user to restart or exit the program
        if not restart_program():
            print("Exiting the program. Goodbye!")
            break


def get_input():
    """Input function to get the weather forecast URL from the user."""
    while True:
        try:
            webpage_url = input("Enter the URL for the weather forecast: ").strip()  # Get and trim user input
            if not webpage_url:  # Validate input is not blank
                print("Error: The URL cannot be blank. Please try again.")
            else:
                return webpage_url  # Return valid URL
        except ValueError as e:
            print(f"Invalid input: {e}")  # Display specific error and retry


def process_webpage(webpage_url):
    """Downloads and parses the weather forecast webpage."""
    try:
        print("\nAccessing the webpage...")
        response = requests.get(webpage_url, timeout=10)  # Make HTTP GET request with a 10-second timeout

        if response.status_code != 200:  # Check if the response status is successful
            print(f"Error: Received status code {response.status_code}. Please try again.")
            return None, None

        if "text/html" not in response.headers.get("Content-Type", ""):  # Validate response content type
            print("Error: The URL does not point to an HTML page. Please try again.")
            return None, None

        print("Webpage accessed successfully! Extracting forecast data...\n")
        soup = BeautifulSoup(response.text, "html.parser")  # Parse the HTML content

        # Extract forecast labels and descriptions from HTML elements
        forecast_labels = [label.get_text() for label in soup.find_all(class_="forecast-label")]
        forecast_text = [text.get_text() for text in soup.find_all(class_="forecast-text")]

        return forecast_labels, forecast_text  # Return extracted data

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to access the webpage. {e}")
        return None, None


def display_output(forecast_labels, forecast_text):
    """Displays the extracted weather forecast in a formatted table."""
    print("\nWeather Forecast:\n")
    print(f"{'Time Period':<20} {'Forecast':<50}")  # Table headers
    print("-" * 70)

    if len(forecast_labels) != len(forecast_text):  # Ensure data consistency
        print("Error: Forecast data is inconsistent. Please try again.")
        return

    # Print the forecast in two columns
    for label, text in zip(forecast_labels, forecast_text):
        print(f"{label:<20} {text:<50}")

    print("-" * 70)


def restart_program():
    """Prompts the user to decide whether to restart the program."""
    return pyip.inputYesNo("Would you like to scrape another webpage? (yes/no): ").lower() == 'yes'


# Entry point of the program
if __name__ == "__main__":
    main()
