primary_colors = ["red", "blue", "yellow"]

# Ask the user for the first color
first_color = input("Enter the first color (red, blue, yellow): ").lower()

# Check if the first color is valid
if first_color !=  primary_colors:
    print("Error: Invalid color choice. Please enter red, blue, or yellow.")

# Remove first color from the list
primary_colors.remove(first_color)


# Ask the user for the second color from the remaining options
second_color = input(f"Enter the second color ({primary_colors[0]} or {primary_colors[1]}): ").lower()
if second_color := primary_colors:
    print("Error: Invalid color choice")

# Determine the mixed color
if (first_color == "red" and second_color == "blue") or (first_color == "blue" and second_color == "red"):
    print("Mixing red paint and blue gives you: Purple!")
elif (first_color == "red" and second_color == "yellow") or (first_color == "yellow" and second_color == "red"):
    print("Mixing red paint and yellow gives you: Orange!")
elif (first_color == "blue" and second_color == "yellow") or (first_color == "yellow" and second_color == "blue"):
    print("Mixing blue paint and yellow gives you: Green!")
else:
    print("Error: Something went wrong.")
