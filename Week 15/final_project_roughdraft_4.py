"""
Author: Lavell McGrone
Date: 2024-12-14
Description: Utilize PyInputPlus and JSON libraries to calculate the total cost of a custom pizza order.
             Give the user a choice to add pizzas, view current and previous orders, and calculate totals including
             tax and tips (optional for assignment, added this feature for my own development challenge).
             When the order is done, place the order by writing this order to a new JSON file.
"""

import json
import pyinputplus as pyip


def main():
    """
    Main function to control the pizza ordering process.
    """
    # Step 1) The program will read the ingredients.json file, if the file is missing or invalid,
    # I will use the try and except block to handle errors and an error message will be displayed to the user.
    try:
        base_options, toppings = load_ingredients("ingredients.json")
    except FileNotFoundError:
        print("Error: The ingredients file was not found.")
        return
    except json.JSONDecodeError:
        print("Error: The ingredients file is not valid JSON.")
        return

    # Display a cool restaurant menu prior to the user making the choices to add pizza, view order or submit order.
    display_menu(base_options, toppings)

    pizzas = []  # Create a empty list to store all pizzas in the order

    while True:
        # Display the main menu using PyInputPlus
        menu_choice = pyip.inputMenu(
            ["Add a Pizza", "View Order", "Submit Order"],
            prompt="\nChoose an option:\n",
            numbered=True,
        )
        if menu_choice == "Add a Pizza":
            num_pizzas = get_num_pizzas()  # Call the function that ask the user how many pizzas they wish to order.
            # Process the order for the specified number of pizzas (based on user-input).
            # It will return two values: a list of new pizzas (ingredients and cost) and a second value (not being used)
            new_pizzas, unused_value = process_order(num_pizzas, base_options, toppings)
            # Add new pizzas to the existing order
            pizzas.extend(new_pizzas)  # Used .extend() to add each pizza from 'new_pizzas' individually.
        elif menu_choice == "View Order":
            # Display the current order or previously ordered items by calling the view_previous_order() function.
            view_previous_order()

        elif menu_choice == "Submit Order":
            # Submit the order and save to JSON file
            if pizzas:   # Check if there are pizzas in the current order.
                total_order_cost = sum(pizza_cost for unused_value, pizza_cost in pizzas)

                # Step 2: Calculate the sales tax (7%)
                tax_amount = total_order_cost * 0.07  # Sales tax is 7% of the total order cost.
                tax_amount = round(tax_amount, 2)  # Round the tax amount to 2 decimal places for currency formatting.

                # Step 3: Calculate the total cost after tax
                total_with_tax = total_order_cost + tax_amount  # Add the tax amount to the total cost.
                total_with_tax = round(total_with_tax, 2)  # Round the result to 2 decimal places.

                # Step 4: Allow the user to select a tip percentage and calculate the tip amount
                tip_amount = calculate_total_with_tip(total_with_tax)
                # The function displays a menu of tip percentages (0%, 10%, 20%, etc.) and calculates the tip.

                # Step 5: Calculate the final total cost (after tax and tip)
                final_total = total_with_tax + tip_amount  # Add the tip amount to the total with tax.
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

            # Ask the user if they want to restart the program
            if restart_order():
                # If the user selects "yes," restart the program from the beginning.
                print("\nRestarting the program.......Loading in 3...2...1  ")
                main()  # Calls the main() function recursively to restart the program.

            else:
                # If the user selects "no," exit the program gracefully.
                print("Exiting the program. Thank you!")
                break  # Break out of the main loop to end the program.


def load_ingredients(file_path):
    """
    Step 1) The program will read the ingredients.json file, The program reads the ingredients.json file using the load_ingredients() function..
    :param file_path: Path to the ingredients file.
    :return: A tuple containing base options and toppings.
    """
    with open(file_path, 'r') as file:
        ingredients = json.load(file)
    return ingredients["base_options"], ingredients["toppings"]


def display_menu(base_options, toppings):
    """
    Display the ingredients and prices in a column-aligned format.
    :param base_options: List of base options with categories and prices.
    :param toppings: Dictionary of toppings and their prices.
    """
    print("\n=============== Pizza Menu ===============")
    print(f"{'Ingredient':<20} {'Price':>15}")
    print("-" * 42)

    for option in base_options:
        category = option['category'].capitalize()
        print(f"\n{category}:")
        print("*" * 42)
        for name, price in option['options'].items():
            print(f"{name:<20}           ${price:>8.2f}")

    print("\nToppings:")
    print("*" * 42)
    for topping, price in toppings.items():
        print(f"{topping:<20}           ${price:>8.2f}")

    print("=" * 42)


def get_num_pizzas():
    """
    Input function to get the number of pizzas from the user.
    :return: The number of pizzas to order as an integer.
    """
    return pyip.inputInt("How many pizzas would you like to order? ", min=1)


def get_pizza_ingredients(base_options, toppings):
    """
    Gather pizza ingredients and calculate the total cost for one pizza.
    Prompts the user to choose crust, sauce, cheese, and toppings.
    """
    ingredients = []  # List to store chosen ingredients with their costs
    total_cost = 0  # Initialize total cost for the pizza

    # Step 1: Select base options (e.g., crust, sauce, cheese)
    for option in base_options:
        category = option["category"]
        choices = option["options"]

        choice = pyip.inputMenu(list(choices.keys()), prompt=f"\nChoose a {category}:\n", numbered=True)
        ingredients.append((category.capitalize(), choice, choices[choice]))
        total_cost = total_cost + choices[choice]

    # Step 2: Select toppings
    for topping, price in toppings.items():
        if pyip.inputYesNo(f"Do you want {topping}? (yes/no): ") == "yes":
            ingredients.append(("Topping", topping, price))
            total_cost = total_cost + price

    return ingredients, total_cost


def process_order(num_pizzas, base_options, toppings):
    """
    Build each pizza and calculate the total order cost.
    :param num_pizzas: Number of pizzas to order.
    :param base_options: List of base options with categories and prices.
    :param toppings: Dictionary of toppings and their prices.
    :return: A list of pizzas with their ingredients and costs, and the total cost of the order.
    """
    pizzas = []  # List to store pizzas with their ingredients and costs
    total_order_cost = 0  # Total cost of the order

    for i in range(1, num_pizzas + 1):
        print(f"\nBuilding pizza #{i}...")
        ingredients, pizza_cost = get_pizza_ingredients(base_options, toppings)
        pizzas.append((ingredients, pizza_cost))
        total_order_cost = total_order_cost + pizza_cost

    return pizzas, total_order_cost


def calculate_total_with_tax(total_order):
    """
    Calculate the total price after adding 7% sales tax.
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
    Ask the user to select a tip percentage and add it to the total amount.
    :param total_with_tax: The total price after adding sales tax.
    :return: Total price including the tip.
    """
    # Define tip choices and display them as a menu
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

    # Get the corresponding tip percentage from the dictionary
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
    Display the summary of the pizza order.
    :param pizzas: List of pizzas with their ingredients and costs.
    :param final_total: Final total cost including tax and tip (optional).
    :param tip_amount: The amount the user tipped (optional, default is 0.00).
    :param tax_amount: Calculate the total order times sales tax (7%).
    """
    print("\nOrder Summary:")
    for i, (ingredients, pizza_cost) in enumerate(pizzas, start=1):
        print(f"\nPizza #{i}:")
        for category, name, price in ingredients:
            print(f"{category:<12}     {name:<20}         $ {price:>17.2f}")
        print("-" * 70)
        print(f"{'Subtotal':<32}              ${pizza_cost:>18.2f}")
    # Display tax amount
    print("-" * 70)
    print(f"{'Tax Amount':<32}              ${tax_amount:>18.2f}")

    # Display the tip amount
    if tip_amount is not None and tip_amount > 0:
        print("-" * 70)
        print(f"{'Tip':<32}              ${tip_amount:>18.2f}")

    # Display the final total
    if final_total is not None:
        print("=" * 70)
        print(f"{'Final Total':<32}              ${final_total:>18.2f}")


def place_order(pizzas, final_total, tax_amount=None, tip_amount=None):
    """
    Save the order to a JSON file and display a confirmation message.
    :param pizzas: List of pizzas in the order.
    :param final_total: Final total price including tax and tip.
    :param tax_amount: The total tax amount for the order.
    :param tip_amount: The tip amount added by the user.
    """
    order_data = {
        "pizzas": [
            {"ingredients": ingredients, "subtotal": round(pizza_cost, 2)}
            for ingredients, pizza_cost in pizzas
        ],
        "tax_amount": round(tax_amount, 2) if tax_amount is not None else 0.00,
        "tip_amount": round(tip_amount, 2) if tip_amount is not None else 0.00,
        "final_total": round(final_total, 2),
    }
    with open("order.json", 'w') as file:
        json.dump(order_data, file, indent=2)

    print("\nYour order has been placed! Thanks for ordering with us!")


def view_previous_order():
    """
    View a previously placed order by reading the order.json file.
    Displays the pizzas, their ingredients, and the totals.
    """
    try:
        with open("order.json", "r") as file:
            order_data = json.load(file)

        # Check if the order data is empty
        if not order_data or "pizzas" not in order_data or not order_data["pizzas"]:
            print("\nYour order is currently empty.")
            return

        # Display the order summary from the JSON data
        print("\n=== Previous Order Summary ===")

        # Display pizzas
        for i, pizza in enumerate(order_data["pizzas"], start=1):
            print(f"\nPizza #{i}:")
            for ingredient in pizza["ingredients"]:
                category, name, price = ingredient
                print(f"{category:<12}    {name:<20}         $ {price:>17.2f}")
            print("-" * 70)
            print(f"{'Subtotal':<32}             ${pizza['subtotal']:>18.2f}")

        # Display tax, tip, and final total
        print("-" * 70)

        # Use .get() to safely retrieve the tax amount
        tax_amount = order_data.get("tax_amount", 0.00)
        print(f"{'Tax Amount':<32}             ${tax_amount:>18.2f}")

        # Use .get() to safely retrieve the tip amount
        tip_amount = order_data.get("tip_amount", 0.00)
        if tip_amount > 0:
            print("-" * 70)
            print(f"{'Tip':<32}             ${tip_amount:>18.2f}")

        # Use .get() to safely retrieve the final total
        final_total = order_data.get("final_total", 0.00)
        if final_total > 0:
            print("=" * 70)
            print(f"{'Final Total':<32}             ${final_total:>18.2f}")

    except FileNotFoundError:
        print("\nError: No previous order found. Please place an order first.")
    except json.JSONDecodeError:
        print("\nError: The order file is not in a valid format. Please try again.")


def restart_order():
    """
    Ask if the user wants to restart the order.
    :return: True if the user wants to restart, False otherwise.
    """
    return pyip.inputYesNo("\nDo you want to start a new order? (yes/no): ") == "yes"


if __name__ == "__main__":
    main()
