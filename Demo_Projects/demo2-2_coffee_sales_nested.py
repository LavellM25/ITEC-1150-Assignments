"""
Author: Erik Granse
Date: 2024-09-23
Description: This program tracks coffee stand sales by drink, price, subtotal per drink and grand total for both cups
    and sales. The results are printed into columns.
    Adapted from M. Bock 6/11/2019
"""

drink_types = input('How many different types of drinks did you sell today? ')

# Validate that drink_type is an int
while not drink_types.isnumeric():
    print("Please enter a whole, positive number: ")
    drink_types = input('How many different types of drinks did you sell today? ')

drink_types = int(drink_types)
# initialize variables
total_cups = 0
total_sales = 0.0

# run through the loop as many times as there are drinks:
for drink_type in range(1, drink_types + 1):
    drink_name = input(f'\nName of the drink type #{drink_type}: ')
    for size in range(1, 4):
        cups_sold = input(f'\tNumber of cups of {drink_name} size {size} sold: ')
        # validate number of cups sold
        while not cups_sold.isnumeric():
            print("\tPlease enter a whole, positive number: ")
            cups_sold = input(f'\tNumber of cups of {drink_name} size {size} sold: ')
        cups_sold = int(cups_sold)

        price = float(input(f'\tPrice of {drink_name} size {size}: $ '))

        # Print a subtotal for the drink and size
        subtotal = round(cups_sold * price, 2)
        print('\t{:<12}Sz.{:>2,d}{:>9,d}{:>8}{:>4,.2f}{:>8}{:>9,.2f}'
              .format(drink_name, size, cups_sold,'$',price,'$',subtotal))

        # add up totals
        total_cups += cups_sold
        total_sales += subtotal

# Print daily report
print('\nToday\'s Drink Sales for the Reporting Period')
print('{:<12}{:^13}{:^12}{:^13}'.format('Types','Cups Sold','','Total'))
print('{:<12}{:>7,d}{:>20}{:>7.2f}'.format(drink_types,total_cups,'$',total_sales))
