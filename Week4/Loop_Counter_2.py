"""
Author: Lavell McGrone
Date: 2024-09-26
Description: This program asks the user for two whole numbers (a smaller and a larger number).
It counts and displays each number in the range and calculates the total sum of all the numbers.
"""

print("Welcome to Lavell's Counting Program!")
print("This program will count numbers between the two values you provide and calculate their total sum.")
print()

# Prompt the user for a small number (must be a whole number 0 or higher)
while True:
    small_num_input = input("Please enter a small number, 0 or higher: ")
    if small_num_input.isnumeric():  # Validate that input is a whole number
        small_num = int(small_num_input)
        break  # Exit the loop if input is valid
    else:
        print("Invalid input. Please enter a whole number, 0 or higher.")

# Prompt the user for a larger number (must be a whole number greater than the first)
while True:
    large_num_input = input(f"Please enter a whole number larger than {small_num}: ")
    if large_num_input.isnumeric() and int(large_num_input) > small_num:  # Validate input
        large_num = int(large_num_input)
        break  # Exit the loop if input is valid
    else:
        print(f"Invalid input. Please enter a whole number larger than {small_num}. "
              "Only whole numbers are accepted.")

# Initialize the total sum
total_sum = 0

# Iterate through the range of numbers and calculate the total sum
print("Counting the numbers:")
for number in range(small_num, large_num + 1):
    print(number)  # Display each number in the range
    total_sum = total_sum + number  # Update the total sum

# Display the total sum of all counted numbers
print(f"The total of all the counted numbers is {total_sum}.")
