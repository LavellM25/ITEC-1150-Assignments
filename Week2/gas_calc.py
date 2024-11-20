"""
Author: Lavell McGrone
Date: 2024-09-13
Description: Calculate and display gas usage for a trip
"""

# Define Variables
miles_driven = float(input('how many miles did you drive?'))
gallons_of_gas = float(input('how many gallons of gas did you use?'))
price_per_gallon = float(input('what is the price of gas?'))

# Calculate miles per gallon = MPG
MPG = miles_driven / gallons_of_gas
print(MPG)

# Calculate total trip cost
trip_cost = gallons_of_gas * price_per_gallon
print(f'Total trip cost: ${trip_cost:.2f}')

# Calculate gallons used
gallons = (trip_cost / price_per_gallon)

# Calculate Miles driven
miles = (MPG * gallons)

# Display the total cost of the trip and the miles per gallon
print("Here are some fun facts about your trip")
print(f'{"MPG":<15} {MPG:>10.2f}')
print(f'{"Total cost":<15}${trip_cost:>10.2f}')
