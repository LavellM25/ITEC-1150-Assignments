"""
Author: Lavell McGrone
Date: 2024-12-13
Description: Create a JSON file named ingredients.json with base options and toppings for a pizza ordering system.
"""

import json


def create_ingredients_file():
    ingredients = {
        "base_options": [
            {
                "category": "crust",
                "options": {
                    "Thin": 10.99,
                    "Traditional": 10.99,
                    "Deep dish": 12.99,
                    "Thick": 6.50,
                    "Gluten-free": 7.00
                }
            },
            {
                "category": "sauce",
                "options": {
                    "Traditional red": 0,
                    "Olive oil": 0,
                    "Marinara": 1.50,
                    "Alfredo": 2.00,
                    "BBQ sauce": 1.75
                }
            },
            {
                "category": "cheese",
                "options": {
                    "Three-cheese blend": 0,
                    "Tuscan Blend": 1.99,
                    "Mozzarella": 2.00,
                    "Cheddar": 2.50,
                    "vegan": 3.00
                }
            }
        ],
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
            "Jalapenos": 1.50
        }
    }

    with open('ingredients.json', 'w') as file:
        json.dump(ingredients, file, indent=4)

    print("ingredients.json has been created successfully!")


# Call the function to create the file
create_ingredients_file()
