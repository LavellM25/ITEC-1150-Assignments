
"""
Author: Lavell McGrone
Date: 2024-11-14
Description: Utilize pyinputplus to calculate the total cost of a custom sandwich order by gathering
ingredient choices, building sandwiches, and display an order summary, based on user input.
"""

import pyinputplus as pyip   # Importing PyInputPlus for input validation


# Prices dictionary for ingredients
PRICES = {
    "bread": {"white": 1.95, "wheat": 2.00, "sourdough": 2.25},
    "protein": {"chicken": 2.75, "turkey": 2.50, "ham": 2.50, "tofu": 2.00},
    "cheese": {"cheddar": 1.00, "swiss": 1.25, "mozzarella": 1.25},
    "extras": {"mayo": 0.10, "mustard": 0.05, "lettuce": 0.50, "tomato": 0.75},
}


def main():
    """
    Main function to control the sandwich ordering process.
    """
    while True:
        num_sandwiches = get_num_sandwiches()   # Input: Get the number of sandwiches

        # Processing: Build each sandwich and calculate total order cost
        sandwiches, total_order_cost = process_order(num_sandwiches)

        display_order_summary(sandwiches, total_order_cost)   # Output: Display the order summary

        if not restart_order():   # Ask if the user wants to start a new order
            print("Thanks for using the sandwich ordering program!")
            break   # End the program if user does not wish to restart


def get_num_sandwiches():
    """
    Input function to get the number of sandwiches from the user.
    :return: The number of sandwiches to order as an integer.
    """
    return pyip.inputInt("How many sandwiches would you like to order? ", min=1)


def get_sandwich_ingredients():
    """
    This function gathers sandwich ingredients and calculates the total cost for one sandwich.
    It prompts the user to choose from available bread, protein, cheese, and extra options.
    """

    ingredients = []   # Initialize an empty list to store chosen ingredients with their costs
    total_cost = 0     # Initialize the total cost for the sandwich to 0

    # Step 1: Ask the user to choose a type of bread
    # inputMenu() shows the options and waits for the user to pick one
    # "numbered=True" adds a number to each choice, making it easier for the user to select
    bread_choice = pyip.inputMenu(["white", "wheat", "sourdough"], numbered=True)

    # Add the bread choice and its price to our list of ingredients as a tuple (bread name, bread price)
    # This list will help keep track of bread choices in the sandwich.
    ingredients.append((bread_choice, PRICES["bread"][bread_choice]))

    # Add the price of the chosen bread to the total cost
    total_cost = total_cost + PRICES["bread"][bread_choice]

    # Step 2: Ask the user to choose a type of protein
    # inputMenu() displays protein options and lets the user select one
    # "numbered=True" adds a number to each choice, making it easier for the user to select
    protein_choice = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], numbered=True)

    # This list will keep track of protein choices in the ingredients of the sandwich
    # Add the chosen protein to the ingredients list as a tuple (protein name, protein price)
    ingredients.append((protein_choice, PRICES["protein"][protein_choice]))

    # Add the price of the chosen protein to the total cost
    total_cost = total_cost + PRICES["protein"][protein_choice]

    # Step 3: Ask the user if they want cheese
    # inputYesNo() only accepts "yes" or "no" as valid answers
    if pyip.inputYesNo("Do you want cheese? (yes/no): ") == "yes":

        # If the user wants cheese, show a menu of cheese options to choose from
        # "numbered=True" adds a number to each choice, making it easier for the user to select
        cheese_choice = pyip.inputMenu(["cheddar", "swiss", "mozzarella"], numbered=True)

        # Add the chosen cheese to the ingredients list with its price
        ingredients.append((cheese_choice, PRICES["cheese"][cheese_choice]))

        # Add the price of the chosen cheese to the total cost (longhand notation)
        total_cost = total_cost + PRICES["cheese"][cheese_choice]

    # Step 4: Ask the user if they want additional extras (mayo, mustard, lettuce, tomato)
    # Use a loop to ask about each extra individually
    for extra in ["mayo", "mustard", "lettuce", "tomato"]:

        # Ask the user if they want the current extra
        if pyip.inputYesNo(f"Do you want {extra}? (yes/no): ") == "yes":

            # If yes, add the extra and its price to the ingredients list
            ingredients.append((extra, PRICES["extras"][extra]))

            # Add the price of the extra to the total cost (longhand notation)
            total_cost = total_cost + PRICES["extras"][extra]

    return ingredients, total_cost   # Return the ingredients list and the total cost of the sandwich


def process_order(num_sandwiches):
    """
    Processing function to build each sandwich and calculate the total order cost.
    :param num_sandwiches: Number of sandwiches to order.
    :return: A list of sandwiches with their ingredients and costs, and the total cost of the order.
    """
    sandwiches = []        # Start with an empty list to store each sandwich's ingredients and cost.
    total_order_cost = 0   # Set the total order cost to zero initially.

    # Loop through the number of sandwiches the customer wants.
    for i in range(1, num_sandwiches + 1):  # have num_sandwiches + 1, so it's user-friendly and don't start at 0.
        # Print the sandwich number to show we're starting a new sandwich.
        print(f"\nBuilding sandwich #{i}...")

        # Call the function to get the ingredients and cost of this sandwich.
        ingredients, sandwich_cost = get_sandwich_ingredients()

        # Add this sandwich's ingredients and cost to the list of sandwiches.
        sandwiches.append((ingredients, sandwich_cost))

        # Add this sandwich's cost to the total order cost.
        total_order_cost = total_order_cost + sandwich_cost

    # After building all sandwiches, return the full list of sandwiches and the total cost of the order.
    return sandwiches, total_order_cost


def display_order_summary(sandwiches, total_order_cost):
    """
    Output function to display the summary of the order.
    :param sandwiches: List of sandwiches with their ingredients and costs.
    :param total_order_cost: Total cost of the order.
    """
    print("\nOrder Summary:")   # Print a title for the order summary.

    # Loop through each sandwich in the list, with `i` as the sandwich number (starting at 1).
    for i, (ingredients, sandwich_cost) in enumerate(sandwiches, start=1):
        print(f"\nSandwich #{i}:")   # Print the sandwich number.

        # Loop through each ingredient and its price in the current sandwich.
        for ingredient, price in ingredients:
            # Print the ingredient name (capitalized) and its price formatted to 2 decimal places in a column.
            print(f"{ingredient.capitalize():<15}      $     {price:>6.2f}")
        print("-" * 40)   # Print a line separator below the list of ingredients for readability.

        # Print the subtotal (cost) of the current sandwich formatted to 2 decimal places in a column.
        print(f"Subtotal             $     {sandwich_cost:>6.2f}")
    print("-" * 40)       # Print another line separator to visually separate individual sandwiches from the total.

    # Print the total cost for all sandwiches, formatted to 2 decimal places.
    print(f"Total Order Cost     $ {total_order_cost:>10.2f}")


def restart_order():
    """
    Asks if the user wants to start a new order.
    :return: True if the user wants to restart, False otherwise.
    """
    return pyip.inputYesNo("\nDo you want to start a new order? (yes/no): ") == "yes"


# Run the program
if __name__ == "__main__":
    main()
