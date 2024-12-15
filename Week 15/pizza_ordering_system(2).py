"""
Author: Lavell McGrone
Date: 2024-12-14
Description: Utilize pyinputplus to calculate the total cost of a custom pizza order by gathering
ingredient choices, building pizzas, and displaying an order summary, based on user input.
"""

import json
import pyinputplus as pyip


# Prices dictionary for pizza ingredients
PRICES = {
    "crust": {"Thin": 10.99, "Traditional": 10.99, "Deep dish": 12.99, "Thick": 6.50, "Gluten-free": 7.00},
    "sauce": {"Traditional red": 0.00, "Olive oil": 0.00, "Marinara": 1.50, "Alfredo": 2.00, "BBQ sauce": 1.75},
    "cheese": {"Three-cheese blend": 0.00, "Tuscan Blend": 1.99, "Mozzarella": 2.00, "Cheddar": 2.50, "Vegan": 3.00},
    "toppings": {
        "Pepperoni": 2.00,
        "Sausage": 2.50,
        "Mushrooms": 1.50,
        "Onions": 1.25,
        "Bell peppers": 1.50,
        "Black olives": 1.75,
        "Pineapple": 2.00,
        "Bacon": 3.00,
        "Spinach": 1.50,
        "Jalapenos": 1.50,
    },
}


def main():
    """
    Main function to control the pizza ordering process.
    """
    # Load menu ingredients from the dictionary
    base_options = [
        {"category": "crust", "options": PRICES["crust"]},
        {"category": "sauce", "options": PRICES["sauce"]},
        {"category": "cheese", "options": PRICES["cheese"]},
    ]
    toppings = PRICES["toppings"]

    # Display the menu at the start of the program
    display_menu(base_options, toppings)

    while True:
        num_pizzas = get_num_pizzas()  # Step 1: Get the number of pizzas

        # Step 2: Build each pizza and calculate the total order cost
        pizzas, total_order_cost = process_order(num_pizzas)

        # Step 3: Calculate the total with sales tax
        total_with_tax = calculate_total_with_tax(total_order_cost)
        print(f"\nTotal with 7% sales tax: ${total_with_tax:.2f}")

        # Step 4: Allow the user to select a tip and calculate the final total
        final_total = calculate_total_with_tip(total_with_tax)

        # Step 5: Display the final order summary
        display_order_summary(pizzas, final_total)

        # Step 6: Place the order and save to a JSON file
        place_order(pizzas, final_total)

        # Step 7: Ask if the user wants to restart the order
        if not restart_order():
            print("Thanks for using the pizza ordering program!")
            break


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


def get_pizza_ingredients():
    """
    Gather pizza ingredients and calculate the total cost for one pizza.
    Prompts the user to choose crust, sauce, cheese, and toppings.
    """
    ingredients = []  # List to store chosen ingredients with their costs
    total_cost = 0  # Initialize total cost for the pizza

    # Step 1: Select crust
    crust_choice = pyip.inputMenu(list(PRICES["crust"].keys()), numbered=True)
    ingredients.append(("Crust", crust_choice, PRICES["crust"][crust_choice]))
    total_cost += PRICES["crust"][crust_choice]

    # Step 2: Select sauce
    sauce_choice = pyip.inputMenu(list(PRICES["sauce"].keys()), numbered=True)
    ingredients.append(("Sauce", sauce_choice, PRICES["sauce"][sauce_choice]))
    total_cost += PRICES["sauce"][sauce_choice]

    # Step 3: Select cheese
    cheese_choice = pyip.inputMenu(list(PRICES["cheese"].keys()), numbered=True)
    ingredients.append(("Cheese", cheese_choice, PRICES["cheese"][cheese_choice]))
    total_cost += PRICES["cheese"][cheese_choice]

    # Step 4: Select toppings
    for topping, price in PRICES["toppings"].items():
        if pyip.inputYesNo(f"Do you want {topping}? (yes/no): ") == "yes":
            ingredients.append(("Topping", topping, price))
            total_cost += price

    return ingredients, total_cost


def process_order(num_pizzas):
    """
    Build each pizza and calculate the total order cost.
    :param num_pizzas: Number of pizzas to order.
    :return: A list of pizzas with their ingredients and costs, and the total cost of the order.
    """
    pizzas = []  # List to store pizzas with their ingredients and costs
    total_order_cost = 0  # Total cost of the order

    for i in range(1, num_pizzas + 1):
        print(f"\nBuilding pizza #{i}...")
        ingredients, pizza_cost = get_pizza_ingredients()
        pizzas.append((ingredients, pizza_cost))
        total_order_cost += pizza_cost

    return pizzas, total_order_cost


def calculate_total_with_tax(total_order_cost):
    """
    Add 7% sales tax to the total order cost.
    :param total_order_cost: Total price before tax.
    :return: Total price after adding sales tax.
    """
    tax_rate = 0.07
    return total_order_cost + (total_order_cost * tax_rate)


def calculate_total_with_tip(total_with_tax):
    """
    Ask the user to select a tip percentage and add it to the total amount.
    :param total_with_tax: The total price after adding sales tax.
    :return: Total price including the tip.
    """
    print("\nSelect a tip percentage:")
    print("1. 0%")
    print("2. 10%")
    print("3. 20%")
    print("4. 30%")
    print("5. 40%")

    tip_choices = {'1': 0.00, '2': 0.10, '3': 0.20, '4': 0.30, '5': 0.40}
    tip_choice = pyip.inputMenu(tip_choices.keys(), numbered=True)
    tip_percentage = tip_choices[tip_choice]

    tip_amount = total_with_tax * tip_percentage
    final_total = total_with_tax + tip_amount

    print(f"\nSubtotal with tax: ${total_with_tax:.2f}")
    print(f"Tip ({int(tip_percentage * 100)}%): ${tip_amount:.2f}")
    print(f"Final Total: ${final_total:.2f}")
    return final_total


def display_order_summary(pizzas, final_total):
    """
    Display the summary of the pizza order.
    :param pizzas: List of pizzas with their ingredients and costs.
    :param final_total: Final total cost including tax and tip.
    """
    print("\nOrder Summary:")
    for i, (ingredients, pizza_cost) in enumerate(pizzas, start=1):
        print(f"\nPizza #{i}:")
        for category, name, price in ingredients:
            print(f"{category:<10} {name:<15}  $ {price:>5.2f}")
        print("-" * 30)
        print(f"Subtotal:              $ {pizza_cost:>5.2f}")

    print("=" * 30)
    print(f"Final Total:           $ {final_total:>5.2f}")


def place_order(pizzas, final_total):
    """
    Save the order to a JSON file and display a confirmation message.
    :param pizzas: List of pizzas in the order.
    :param final_total: Final total price including tax and tip.
    """
    order_data = {
        "pizzas": [{"ingredients": ingredients, "subtotal": pizza_cost} for ingredients, pizza_cost in pizzas],
        "final_total": final_total,
    }
    with open("order.json", 'w') as file:
        json.dump(order_data, file, indent=4)
    print("\nYour order has been placed! Thanks for ordering with us!")



def restart_order():
    """
    Ask if the user wants to restart the order.
    :return: True if the user wants to restart, False otherwise.
    """
    return pyip.inputYesNo("\nDo you want to start a new order? (yes/no): ") == "yes"


# Run the program
main()
