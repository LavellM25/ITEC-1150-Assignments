import os
import json

def main():
    # File name for the JSON data
    file_name = 'lab_16_forecast.json'
    os.startfile(os.path.dirname(os.path.abspath(file_name)))

    try:
        # Open and read the JSON file
        with open(file_name, 'r') as file:
            data = json.load(file)  # Convert JSON string to Python dictionary

        # Loop through forecast periods and print details
        forecasts = data.get("periods", [])  # Get the list of periods from the data
        for forecast in forecasts:
            # Extract the name (day/period) and detailed forecast
            period_name = forecast.get("name", "Unknown Period")
            detailed_forecast = forecast.get("detailedForecast", "No detailed forecast available.")

            # Print in the specified format
            print(f"{period_name} {detailed_forecast}")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_name}' is not in valid JSON format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
