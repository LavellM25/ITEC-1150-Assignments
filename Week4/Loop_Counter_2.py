"""
Author: Lavell McGrone
Date: 2024-09-26
Description: Counting program that calculates and displays the sum of all the printed numbers.
"""

print("Welcome to Lavell's counting program. ")
print("Lavell's counting program makes you count like a pro, and will add up the digits you enter. ")
print()

# Ask the user for a small number (must be a whole number 0 or higher)
while True:
    small_num_input = input("Please enter a small number, 0 or higher: ")
    if small_num_input.isnumeric():
        small_num = int(small_num_input)
        break # If user enters in correct value then break the loop
    else:
        print("Please enter a whole number only, 0 or higher. ")

# Ask the user for a second number (must be a whole number larger than the first)
while True:
    large_num_input = input(f"Please enter a whole number larger than {small_num}: ")
    if large_num_input.isnumeric() and int(large_num_input) > small_num:
        large_num = int(large_num_input)
        break # If user enters in correct value then break the loop
    else:
        print(f"Please enter a whole number larger than {small_num}. ")
        f'''
        Erik:
            I would recommend printing a different error message here, something like "Only whole numbers are 
            accepted, and it must be larger than {small_num}". Not critical, but the user will just see the same 
            prompt twice in a row if they make a mistake, and they obviously didn't read it the first time, 
            so a different message can help :-)
        '''

# Initialize total sum
total_sum = 0

# Print each number from user input and add to the total sum
for number in range(small_num, large_num + 1):
    print(number)
    total_sum = (total_sum + number)

# Display the total sum of all counted numbers
print(f"The total of all the counted numbers is {total_sum}.")

'''
Erik:
    Great work!
'''
