"""
Author: Lavell McGrone
Date: 2024-12-19
Description: Utilize PyInputPlus and downloaded ingredients from URL to calculate the total cost of a custom
             pizza order. Give the user a choice to add pizzas, view current and previous orders, and calculate
             totals including tax and tips (optional for assignment, added this feature for my own development
             challenge). When the order is done, place the order by writing this order to a new JSON file.
"""

import json
import pyinputplus as pyip
import requests


def main():
    """
    Main function to control the pizza ordering process.
    """
    # Step 1) The program will load data from URL
    # I will use the try and except block to handle errors and an error message will be displayed to the user.
    url = "https://itec-minneapolis.s3.us-west-2.amazonaws.com/ingredients.json"
    try:
        base_options, toppings = load_ingredients(url)
        # Check if the ingredients are loaded properly
        if not base_options and not toppings:
            print("Error: Ingredients file is empty or missing required data.")
            return
    except Exception as e:
        print(f"Error: Unable to load ingredients. Reason: {e}")
        return

    # Display a cool restaurant menu prior to the user making the choices to add pizza, view order or submit order.
    display_menu(base_options, toppings)

    pizzas = []  # Create an empty list to store all pizzas in the order

    while True:
        # Display the main menu using PyInputPlus
        menu_choice = pyip.inputMenu(
            ["Add a Pizza", "View Current Order", "View Previous Order", "Submit Order"],
            prompt="\nChoose an option:\n",
            numbered=True,
        )
        if menu_choice == "Add a Pizza":
            # Display a message indicating which pizza is being added to the order.
            # `len(pizzas)` gives the current number of pizzas in the list, and adding 1 ensures
            # the next pizza is numbered correctly (starting from 1, not 0).
            print(f"\nAdding Pizza #{len(pizzas) + 1}...")
            ingredients, pizza_cost = get_pizza_ingredients(base_options, toppings)
            # Call the `get_pizza_ingredients` function to gather the user's selections for the pizza.
            # The function returns two values:
            # - ingredients: A list of the chosen categories, options, and their prices (ex: crust type, toppings).
            # - pizza_cost: The total price of the pizza based on the user's selections.
            pizzas.append((ingredients, pizza_cost))  # Add the pizza to the list
        elif menu_choice == "View Current Order":
            # if users try to view a current order when no pizzas have been added, it may display an empty summary.
            # so I added check to validate the list of pizzas are not empty.
            if not pizzas:
                print("\nYour current order is empty. ")
            display_order_summary(pizzas)  # Display the current order
        elif menu_choice == "View Previous Order":
            view_previous_order()  # Display the previous order
        elif menu_choice == "Submit Order":
            # Submit the order and save to JSON file
            if pizzas:  # Check if there are pizzas in the current order.
                total_order_cost = sum(pizza_cost for unused_value, pizza_cost in pizzas)
                # Step 2: Calculate the sales tax (7%)
                tax_amount = total_order_cost * 0.07  # Sales tax is 7% of the total order cost.
                tax_amount = round(tax_amount, 2)  # Round the tax amount to 2 decimal places for currency formatting.

                # Step 3: Calculate the total cost after tax
                total_with_tax = round(total_order_cost + tax_amount, 2)  # Add the tax amount to the total cost.

                # Step 4: Allow the user to select a tip percentage and calculate the tip amount
                tip_amount = calculate_total_with_tip(total_with_tax)
                # The function displays a menu of tip percentages (0%, 10%, 20%, etc.) and calculates the tip.

                # Step 5: Calculate the final total cost (after tax and tip)
                final_total = round(total_with_tax + tip_amount, 2)  # Add the tip amount to the total with tax.
                final_total = round(final_total, 2)  # Round the result to 2 decimal places.

                # Step 6: Display the final order summary
                display_order_summary(pizzas, final_total, tip_amount, tax_amount)
                # This function prints out:
                # - Each pizza with its ingredients and cost.
                # - The subtotal, tax, tip, and final total.

                # Step 7: Save the order to a JSON file
                place_order(pizzas, final_total, tax_amount, tip_amount)
                # The place_order function writes the order details to "order.json" for record-keeping.

                # Step 8: Exit the loop after submitting the order
                print("Your order has been submitted!")
                break  # Exit the main loop, ending the program.

            else:
                # If no pizzas have been added, display an error message.
                print("\nYou cannot submit an empty order.")


def load_ingredients(url):
    """
    Step 1) Download the ingredients.json file from the URL.
    :param url: URL of the ingredients.json file.
    :return: Base options and toppings as lists/dictionaries.
    """
    try:
        # Get JSON data from the URL.
        # The `requests.get(url)` sends a GET request to retrieve the file contents.
        response = requests.get(url)

        # Check if the HTTP response indicates success (status code 200-299).
        # If not, this will raise an HTTPError and jump to the `except` block.
        response.raise_for_status()

        # Parse the response content as JSON and load it into the `ingredients` dictionary.
        # If the content is not valid JSON, this will raise a `JSONDecodeError`.
        ingredients = response.json()

        # Validate the structure of the JSON data
        base_options = ingredients.get("base_options", [])
        toppings = ingredients.get("toppings", {})

        # Check if both base_options and toppings are missing
        if not base_options and not toppings:
            print("Error: Ingredients file is empty or missing required data. Exiting program.")
            return [], {}

        # Return the base options and toppings
        return base_options, toppings

    except requests.RequestException as e:
        print(f"Error fetching ingredients from URL: {e}")
        return [], {}


def display_menu(base_options, toppings):
    """
    Step 2) (Optional) I added a restaurant menu stand that will show users the menu while they are waiting to order.
    Display the ingredients and prices.
    :param base_options: List of base options with categories and prices.
    :param toppings: List of toppings and their prices.
    """
    # Header for the menu
    print("\n=============== Pizza Menu ===============")
    print(f"{'Ingredient':<20} {'Price':>15}")  # Ingredients on the left and Prices on the right
    print("-" * 42)  # Horizontal line break

    # Loop through each category of base options (crust, sauce, cheese)
    for option in base_options:
        category = option['category'].capitalize()  # Capitalize the category name
        print(f"\n{category}:")  # Display the category (ex. "Crust", "Cheese",etc.)
        print("*" * 42)  # Horizontal line break

        # Loop through each item in the category's options and display its name and price
        for name, price in option['options'].items():  # Ex: Cheese type mozzarella, price is $2.00
            print(f"{name:<20}           ${price:>8.2f}")  # Format the name on the left and price on the right.

    # Toppings section header
    print("\nToppings:")
    print("*" * 42)   # Horizontal line break

    # Loop through each topping and display its name and price
    for topping, price in toppings.items():  # Ex: Pepperoni is $2.00
        print(f"{topping:<20}           ${price:>8.2f}")  # Format the topping name on the left and price on the right.

    # Footer line for the menu
    print("=" * 42)


def get_pizza_ingredients(base_options, toppings):
    """
    Step 3) Gather pizza ingredients and calculate the total cost for one pizza.
    Prompts the user to choose crust, sauce, cheese, and toppings.
    """
    ingredients = []  # List to store chosen ingredients with their costs
    total_cost = 0  # Initialize total cost for the pizza

    # Step 1: Select base options (ex: crust, sauce, cheese)
    for option in base_options:  # Loop through each category in the base options
        category = option["category"]  # Get the specific category if it is picked.
        choices = option["options"]   # Get the specific options from the ingredients.json file if it is picked.
        # Step 2a: Prompt the user to choose an option from the category
        choice = pyip.inputMenu(list(choices.keys()), prompt=f"\nChoose a {category}:\n", numbered=True)
        # Step 2b: Add the chosen option to the ingredients list along with its category and price
        ingredients.append((category.capitalize(), choice, choices[choice]))
        # Step 2c: Add the price of the chosen option to the total cost
        total_cost = total_cost + choices[choice]

    # Step 3: Select toppings
    # Check if there are available toppings before prompting the user
    if not toppings:
        print("\nNo toppings are available.")  # Inform the user if no toppings are provided
    else:   # Loop through each available topping
        for topping, price in toppings.items():  # For every topping, ask the user if they want this topping (yes or no)
            if pyip.inputYesNo(f"Do you want {topping}? (yes/no): ") == "yes":
                # If the user selects "yes", add the topping to the ingredients list
                ingredients.append(("Topping", topping, price))
                # Add the topping's price to the total cost
                total_cost = total_cost + price
    # Return the list of selected ingredients and the total cost of the pizza
    return ingredients, total_cost


def process_order(num_pizzas, base_options, toppings):
    """
    Step 4) Based on the answer of the user in step 3 if they want to add a pizza,
    I will build x amount of pizza's and calculate the total order cost.
    :param num_pizzas: Number of pizzas to order.
    :param base_options: List of base options with categories and prices.
    :param toppings: Dictionary of toppings and their prices.
    :return: A list of pizzas with their ingredients and costs, and the total cost of the order.
    """
    pizzas = []  # List to store pizzas with their ingredients and costs
    total_order_cost = 0  # Total cost of the order

    # Starts at 1, ends at the smaller value between num_pizzas and 25,
    # Use min(num_pizzas, 25) so loop never goes 25 times.
    for i in range(1, min(num_pizzas, 25) + 1):
        print(f"\nBuilding pizza #{i}...")  # Each iteration represents building one pizza in the index of "i".
        # Call get_pizza_ingredients() to gather ingredients and cost for a single pizza
        ingredients, pizza_cost = get_pizza_ingredients(base_options, toppings)
        # Add (.append) the pizza details (ingredients and cost) to the pizzas list to be used later in final order
        pizzas.append((ingredients, pizza_cost))
        # Add the cost of this pizza to the total order cost
        total_order_cost = total_order_cost + pizza_cost
    # Return the list of pizzas and the total order cost to be used later in final order summary.
    return pizzas, total_order_cost


def calculate_total_with_tax(total_order):
    """
    Step 5 (optional step) Calculate the total price after adding 7% sales tax.
    :param total_order: The total price before tax.
    :return: A tuple containing the tax amount and total price after tax.
    """
    tax_rate = 0.07  # Define the tax rate
    # Calculate the tax amount
    tax_amount = total_order * tax_rate
    # Calculate the total with tax
    total_with_tax = total_order + tax_amount
    # Round the results to two decimal places
    tax_amount = round(tax_amount, 2)
    total_with_tax = round(total_with_tax, 2)
    return tax_amount, total_with_tax


def calculate_total_with_tip(total_with_tax):
    """
    Step 6 (optional) Ask the user to select a tip percentage and add it to the total amount.
    :param total_with_tax: The total price after adding sales tax.
    :return: Total price including the tip.
    """
    # Define tip choices that the user will have to pick from.
    tip_choices = {
        '0%': 0.00,
        '10%': 0.10,
        '20%': 0.20,
        '30%': 0.30,
        '40%': 0.40
    }
    # Use pyip.inputMenu to let the user select a tip percentage directly
    tip_choice = pyip.inputMenu(
        list(tip_choices.keys()),
        prompt="\nSelect a tip percentage:\n", numbered=True)
    # Get the corresponding tip percentage from the dictionary that is chosen from the user.
    tip_percentage = tip_choices[tip_choice]
    # Calculate the tip amount
    tip_amount = total_with_tax * tip_percentage
    tip_amount = round(tip_amount, 2)
    # Display a thank-you message if the user tipped.
    if tip_amount > 0:
        print(
            f"Thank you so much for the generous tip of ${tip_amount:.2f}! "
            f"Your support means a lot to me and helps me continue providing great service."
        )
    return tip_amount


def display_order_summary(pizzas, final_total=None, tip_amount=None, tax_amount=None):
    """
    Step 7) Display the summary of the pizza order.
    Provides a detailed summary of the user's pizza order, including ingredients, costs, tax, tip, and the final total.
    :param pizzas: List of pizzas with their ingredients and costs.
    :param final_total: Final total cost including tax and tip (optional).
    :param tip_amount: The amount the user tipped (optional, default is 0.00).
    :param tax_amount: Calculate the total order times sales tax (7%).
    """

    print("\n" + "Order Summary:".center(60))  # Header that I want to be center-aligned
    print("=" * 70)  # Add a horizontal line breaker
    # Iterate through the list of pizzas to display their details
    for i, (ingredients, pizza_cost) in enumerate(pizzas, start=1):
        print(f"\nPizza #{i}:")  # Display which pizza in the order which the user ordered, followed with ingredients.

        for category, name, price in ingredients:  # Loop through ingredients of the current pizza
            print(f"{category:<12}     {name:<20}         $ {price:>17.2f}")
            # For each ingredient (like crust, sauce, or topping), display its category, name, and price
        print("-" * 70)  # Separator for each pizza's subtotal
        print(f"{'Subtotal':<32}              ${pizza_cost:>18.2f}")
        # Display the subtotal for this pizza, which is the sum of all its ingredients.
    print("-" * 70)  # Separator line for the total cost
    # After listing all pizzas, add a separator line to transition into the overall costs like tax and tip.

    # Display tax amount (0.00 if None)
    tax_amount = tax_amount if tax_amount is not None else 0.00
    print(f"{'Tax Amount':<32}              ${tax_amount:>18.2f}")

    # Display the tip amount (0.00 if user did not leave a tip)
    # If the user added a tip, we include it here. If no tip was given, this section is skipped.
    if tip_amount is not None and tip_amount > 0:
        print("-" * 70)
        print(f"{'Tip':<32}              ${tip_amount:>18.2f}")
    # Display the final total (0.00 if None)
    final_total = final_total if final_total is not None else 0.00
    print("=" * 70)  # Line separator for the final total
    print(f"{'Final Total':<32}              ${final_total:>18.2f}")
    # Concludes with the grand total, which includes the subtotal, tax, and tip.
    # A double line separator is used to highlight the final amount.


def place_order(pizzas, final_total=None, tax_amount=None, tip_amount=None):
    """
    Step 8) Save the order to a JSON file and display a confirmation message.
    :param pizzas: List of pizzas in the order.
    :param final_total: Final total price including tax and tip.
    :param tax_amount: The total tax amount for the order.
    :param tip_amount: The tip amount added by the user.
    """
    # Create an order summary dictionary
    order_data = {
        "pizzas": [
            {
                "ingredients": ingredients,  # List of ingredients for each pizza
                "subtotal": round(pizza_cost, 2)  # Rounded subtotal for each pizza to two decimal places
            }
            for ingredients, pizza_cost in pizzas  # Loop through the pizzas list
        ],
        "tax_amount": round(tax_amount, 2) if tax_amount is not None else 0.00,  # Tax amount, 0.00 if None,
        "tip_amount": round(tip_amount, 2) if tip_amount is not None else 0.00,  # Tip amount, 0.00 if None
        "final_total": round(final_total, 2) if final_total is not None else 0.00,  # Final total 0.00 if None
    }   # Final total, rounded to two decimals

    # Attempt to save the order data to a JSON file
    try:
        with open("order.json", 'w') as file:
            json.dump(order_data, file, indent=2)  # Save the data in a readable JSON format
        # Display a confirmation message to the user if the file been saved.
        print("\nYour order has been placed! The details are saved in 'order.json'. Thank you!")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}, and was unable to save your order to 'order.json'. Reason: {e}")


def view_previous_order():
    """
    Step 9) View a previously placed order by reading the order.json file.
    Displays the pizzas, their ingredients, and the totals.
    """
    try:
        # Open the order.json file in read mode.
        with open("order.json", "r") as file:
            order_data = json.load(file)  # Load the JSON data

        # Check if the file contains valid order data or if the pizzas list is empty.
        if not order_data or "pizzas" not in order_data or not order_data["pizzas"]:
            print("\nYour order is currently empty.")  # Inform the user accordingly, if there's no data to display
            return

        # Display a header for previous order summary.
        print("\n===================== Previous Order Summary =====================")

        # Create a for loop to display each pizza in the order, start at 1, no negative values
        for i, pizza in enumerate(order_data["pizzas"], start=1):
            print(f"\nPizza #{i}:")  # Print the pizza number to the user for clarity.
            for ingredient in pizza["ingredients"]:  # Iterate through the list of ingredients.
                category, name, price = ingredient  # Show the ingredient details
                print(f"{category:<12}    {name:<20}         $ {price:>17.2f}")
            print("-" * 70)  # Separator line for readability
            print(f"{'Subtotal':<32}             ${pizza['subtotal']:>18.2f}")  # Display the pizza subtotal, for each
        # After listing the pizzas, display the tax, tip, and final total if available.
        print("-" * 70)
        # Display tax amount, 0.00 if None
        tax_amount = order_data.get("tax_amount", 0.00)
        print(f"{'Tax Amount':<32}             ${tax_amount:>18.2f}")
        # Display tip amount if greater than 0
        tip_amount = order_data.get("tip_amount", 0.00)
        if tip_amount > 0:
            print("-" * 70)
            print(f"{'Tip':<32}             ${tip_amount:>18.2f}")
        # Display final total if greater than 0
        final_total = order_data.get("final_total", 0.00)
        if final_total > 0:
            print("=" * 70)
            print(f"{'Final Total':<32}             ${final_total:>18.2f}")
        # Write a message to the user confirming that the order was displayed.
        print("\nYour previous order has been successfully displayed.")
    except FileNotFoundError:
        # Handle the case where the order.json file does not exist.
        print("\nError: No previous order found. Please place an order first.")
    except json.JSONDecodeError:
        # Handle the case where the file content is not valid JSON.
        print("\nError: The order file is not in a valid format. Please try again.")


if __name__ == "__main__":
    main()
