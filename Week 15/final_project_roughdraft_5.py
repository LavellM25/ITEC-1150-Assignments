import json
import pyinputplus as pyip


def main():
    # Define file paths for ingredients and order output
    ingredients_file = "ingredients.json"  # File containing ingredient options
    output_file = "order.json"  # File where the order will be saved

    # Initialize an empty list to store the pizzas in the order
    order = []

    # Attempt to load ingredients from the specified JSON file
    try:
        base_options, toppings = load_ingredients(ingredients_file)
    except FileNotFoundError:
        print(f"Error: The file '{ingredients_file}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file '{ingredients_file}' contains invalid JSON.")
        return

    # Step 1: Display the menu for reference
    display_menu(base_options, toppings)

    # Main program loop to display the menu and handle user input
    while True:
        print("\n========= Pizza Ordering System ==========")
        print("1. Add a Pizza")
        print("2. View Order")
        print("3. Place Order")
        print("4. Exit")

        # Prompt the user to select a menu option
        choice = input("Choose an option: ").strip()

        # Handle the user's choice
        if choice == '1':
            # Step 2: Add a new pizza to the order
            pizza, base_price = get_base_options_selection(base_options)
            topping_selection, topping_price = get_toppings_selection(toppings)
            pizza.update(topping_selection)  # Add toppings to the pizza
            order.append(pizza)  # Add the pizza to the order list
            print("\nPizza added to your order!")
            view_single_pizza(pizza, base_price + topping_price)  # Show the added pizza's details
        elif choice == '2':
            # Step 3: View all pizzas currently in the order
            if order:
                view_order(order)
            else:
                print("Your order is empty.")
        elif choice == '3':
            # Step 4: Place the order if there are pizzas in the order list
            if order:
                view_order(order)  # Show the full order before finalizing
                grand_total = sum([sum(price for _, price in pizza.values()) for pizza in order])

                # Step 5: Calculate tax and display total with tax
                total_with_tax = calculate_total_with_tax(grand_total)
                print(f"\nTotal with 7% sales tax: ${total_with_tax:.2f}")

                # Step 6: Ask for tip and display final total
                final_total = calculate_total_with_tip(total_with_tax)
                print(f"\nFinal total (with tax and tip): ${final_total:.2f}")

                # Step 7: Place the order and save to a file
                place_order(order, output_file)
                break  # Exit the loop after placing the order
            else:
                print("You cannot place an empty order.")
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Handle invalid menu option
            print("Invalid option. Please try again.")


def load_ingredients(file_path):
    """
    Load the ingredients from a JSON file.
    :param file_path: The path to the JSON file.
    :return: A tuple containing the base options list and toppings dictionary.
    """
    # Open the file and load its contents as JSON
    with open(file_path, 'r') as file:
        ingredients = json.load(file)
    return ingredients['base_options'], ingredients['toppings']  # Return base options and toppings


def get_base_options_selection(base_options):
    """
    Prompt the user to select base options for their pizza.
    :param base_options: List of available base options.
    :return: A dictionary representing the selected pizza and its base price.
    """
    pizza = {}  # Initialize an empty dictionary to store selected base options
    total_price = 0  # Initialize total price for the pizza

    # Loop through each category of base options (e.g., crust, sauce)
    for option in base_options:
        category = option['category']  # e.g., 'Crust'
        choices = option['options']  # Available choices for the category

        print(f"\nWhat kind of {category} do you want?")
        for i, (choice, price) in enumerate(choices.items(), start=1):
            print(f"{i}. {choice} (${price:.2f})")

        # Prompt the user to make a selection and validate input
        while True:
            try:
                user_choice = int(input("Choose an option: ")) - 1
                selected = list(choices.keys())[user_choice]
                pizza[category] = (selected, choices[selected])  # Add choice to pizza dictionary
                total_price = total_price + choices[selected]  # Add price to total
                break
            except (IndexError, ValueError):
                print("Invalid choice. Please try again.")

    return pizza, total_price


def get_toppings_selection(toppings):
    """
    Prompt the user to select toppings for their pizza.
    :param toppings: Dictionary of available toppings and their prices.
    :return: A dictionary of selected toppings and their total price.
    """
    selected_toppings = {}  # Initialize an empty dictionary for selected toppings
    total_price = 0  # Initialize total price for the toppings

    # Loop through available toppings and prompt the user
    for topping, price in toppings.items():
        choice = pyip.inputYesNo(f"Do you want {topping}? (y/n): ").strip().lower()
        if choice == 'y':
            selected_toppings[topping] = price  # Add topping to selection
            total_price = total_price + price  # Add price to total

    return selected_toppings, total_price


def view_single_pizza(pizza, total_price):
    """
    Display the details of a single pizza.
    :param pizza: Dictionary representing the pizza.
    :param total_price: Total price of the pizza.
    """
    print("\n=== Pizza Details ===")
    for ingredient, selection in pizza.items():
        try:
            # Attempt to unpack the selection (works for base options)
            name, price = selection
            print(f"{ingredient.capitalize()}: {name} (${price:.2f})")
        except:
            # Skip handling the error and just print the raw value (for toppings)
            print(f"{ingredient.capitalize()}: (${selection:.2f})")
    print(f"Total Price: ${total_price:.2f}")
    print("====================")


def view_order(order):
    """
    Display the details of all pizzas in the order.
    :param order: List of pizzas in the order.
    """
    print("\n=== Your Order ===")
    grand_total = 0  # Initialize the grand total for the entire order

    for i, pizza in enumerate(order, start=1):
        print(f"\nPizza #{i}:")
        total_price = 0  # Initialize the total price for the current pizza

        for ingredient, (name, price) in pizza.items():
            print(f"{ingredient.capitalize()}: {name} (${price:.2f})")
            total_price = total_price + price  # Add price to total for this pizza

        print(f"Total for Pizza #{i}: ${total_price:.2f}")
        grand_total = grand_total + total_price  # Add to the grand total

    print(f"\nGrand Total: ${grand_total:.2f}")
    print("====================")


def calculate_total_with_tax(total_order):
    """
    Add 7% sales tax to the total order amount.
    :param total_order: The total price before tax.
    :return: The total price after adding sales tax.
    """
    tax_rate = 0.07
    total_with_tax = total_order + (total_order * tax_rate)
    return total_with_tax


def calculate_total_with_tip(total_with_tax):
    """
    Ask the user to select a tip percentage and add it to the total amount.
    :param total_with_tax: The total price after adding sales tax.
    :return: The total price including the tip.
    """
    print("\nWould you like to leave a tip?")
    print("1. 0%")
    print("2. 10%")
    print("3. 20%")
    print("4. 30%")

    tip_choices = {'1': 0.00, '2': 0.10, '3': 0.20, '4': 0.30}
    while True:
        tip_choice = input("Choose an option (1-4): ").strip()
        if tip_choice in tip_choices:
            break
        print("Invalid choice. Please select a valid option.")

    tip_percentage = tip_choices[tip_choice]
    tip_amount = total_with_tax * tip_percentage
    total_with_tip = total_with_tax + tip_amount

    print(f"\nSubtotal with tax: ${total_with_tax:.2f}")
    print(f"Tip ({int(tip_percentage * 100)}%): ${tip_amount:.2f}")
    print(f"Total with tip: ${total_with_tip:.2f}")
    return total_with_tip


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





# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
