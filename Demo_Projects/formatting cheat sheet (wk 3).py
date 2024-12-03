'''
Author: Erik Granse (erik.granse@minnstate.edu)
Date: 2024-30-01
Description: A reference exercise showing different methods of formatting strings.
'''

# Goal: Hello, Alice!

name = 'Alice'

# Concatenation: Simple, but can be tricky with elements such as spaces.
print("\nConcatenation:")
print('Hello, ' + name + "!")

# Multiple values passed to print(): Doesn't work here, because it inserts a 
#   space we don't want between the name and the exclamation point.
print("\nMultiple values passed:")
print('Hello,', name, "!")

# Format string: Probably the best choice here, as it is easy to understand 
#   and hard to make mistakes.
print("\nFormat string:")
print(f"Hello, {name}!")

# Format method: Good for some situations, but maybe too complicated for this
#    simple problem.
print("\nFormat method:")
print("Hello, {}!".format(name))

# -----------------------------------------------------------------------------

# Goal: The product of 6 * 9 is 54

value_1 = 6
value_2 = 9

# Concatenation: This is becoming a messy way to do things because of the 
# number of elements and the need to convert to strings.
print("\nConcatenation:")
print("The product of " + str(value_1) + " * " + str(value_2) + " is " + str(value_1 * value_2))

# Multiple values passed to print(): This is much better than concatenation,
#   but may be a little hard to read.
print("\nMultiple values passed:")
print("The product of", value_1, '*', value_2, 'is', value_1 * value_2)

# Format string: Also better than concatenation, and maybe easier to read than
#   passing multiple values to print().
print("\nFormat string:")
print(f"The product of {value_1} * {value_2} is {value_1 * value_2}")

# Format method: A little less readable than a format string.
print("\nFormat method:")
print("The product of {} * {} is {}".format(value_1, value_2, value_1 * value_2))

# -----------------------------------------------------------------------------

# Goal:
#   Coffee             1,000     $      5.25     $  5,250.00
#   Tea                  100     $      3.15     $    315.00

coffee = 'Coffee'
coffee_cups_sold = 1000
coffee_price = 5.25
coffee_total = 5250.00

tea = 'Tea'
tea_cups_sold = 100
tea_price = 3.15
tea_total = 315.00

# Concatenation: This gets tricky quickly, and spacing is very hard unless your
#   numbers never change. Also, how do we get the thousands seperator or two decimal places?
print("\nConcatenation:")
print(coffee + "              " + str(coffee_cups_sold) + "     $      " + str(coffee_price) + "     $   " + str(coffee_total))
print(tea + "                  " + str(tea_cups_sold) + "     $      " + str(tea_price) + "     $    " + str(tea_total))

# Multiple values passed to print(): This is just as bad as concatenation:
print("\nMultiple values passed:")
print(coffee, "            ", str(coffee_cups_sold), "    $     ", str(coffee_price), "    $  ", str(coffee_total))
print(tea, "                ", str(tea_cups_sold), "    $     ", str(tea_price), "    $   ", str(tea_total))

# Format string: Much better solution than either of the two methods before.
print("\nFormat string:")
print(f"{coffee:<16}{coffee_cups_sold:>8,}{'$':>6}{coffee_price:>10,.2f}{'$':>6}{coffee_total:>10,.2f}")
print(f"{tea:<16}{tea_cups_sold:>8,}{'$':>6}{tea_price:>10,.2f}{'$':>6}{tea_total:>10,.2f}")

# Format method: Even better, because we can put reuse our string! This is the best reason to use the format method.
print("\nFormat method:")
DRINK_TABLE_STRING = "{:<16}{:>8,}{:>6}{:>10,.2f}{:>6}{:>10,.2f}"
print(DRINK_TABLE_STRING.format(coffee, coffee_cups_sold, '$', coffee_price, '$', coffee_total))
print(DRINK_TABLE_STRING.format(tea, tea_cups_sold, '$', tea_price, '$', tea_total))

# -----------------------------------------------------------------------------

# Explanation of string formatting codes

# [fill]align][width][grouping_option]["." precision][type]

DRINK_TABLE_STRING = "{:.<16}{:*>8,}{:.>6}{:*>10,.2f}{:.>6}{:*>10,.2f}"
print("\n1st column has blanks filled with periods, aligned left, 16 characters wide: {:.<16}")
print("2nd column has blanks filled with asteriks, aligned right, 8 characters wide, a comma separator: {:*>8,}")
print("3rd column has blanks filled with periods, aligned right, 6 characters wide: {:.>6}")
print("4th column has blanks filled with asteriks, aligned right, 10 characters wide, a comma separator, two decimal places: {:*>10,.2f}")
print("5th column has blanks filled with periods, aligned right, 6 characters wide: {:.>6}")
print("6th column has blanks filled with asteriks, aligned right, 10 characters wide, a comma separator, two decimal places: {:*>10,.2f}")
print()
print(DRINK_TABLE_STRING.format('Col1', 1000, '$', 1000, '$', 1000))

