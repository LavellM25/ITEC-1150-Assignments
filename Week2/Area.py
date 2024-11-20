"""
Author: Lavell McGrone
Date: 2024-09-13
Description: Calculate and display area of rectangle given user measurement units
"""
# Define variables for measurement
inches = 12
feet = (inches /12)
meter = (feet * 3.28084)

# Display and print length and width and formatted sentences
unit = input("What is your measurement unit (in., ft., cm., m, etc.)? ")
length = float(input(f"What is the length of the rectangle in {unit}? "))
width = float(input(f"What is the width of the rectangle in {unit}? "))

# Calculate the area of the rectangle
area = (length * width)

# Display area of rectangle in formatted sentence
print(f"Your rectangle is {area:.2f} square {unit}.")
