"""
Author: Lavell McGrone
Date: 2024-09-26
Description: Validate user inputs, print the numbers between two inputs, and calculate the total of all printed inputs.
"""

# Explain the purpose of this program
print("This program will print various number sequences using loops. ")
print()

# Print numbers from 0 through 5 inclusive
print("Here are the numbers from 0 through 5: ")
for num in range(0, 6):
    print(num)
print()

# Print numbers from 1 through 20 inclusive
print("Here are the numbers from 1 through 20: ")
for num in range(1, 21):
    print(num)
print()

# Print even numbers from 0 through 24 inclusive
print("Here are the even numbers from 0 through 24: ")
for num in range(0, 25, 2):
    print(num)
print()

# Print odd numbers from 37 through 53 inclusive
print("Here are the odd numbers from 37 through 53: ")
for num in range(37, 54, 2):
    print(num)
print()

# Print multiples of ten between 10 and 60 inclusive
print("Here are the multiples of 10 from 10 through 60: ")
for num in range(10, 61, 10):
    print(num)
print()

# Print numbers counting down from 30 through 20 inclusive
print("Here is a countdown from 30 through 20: ")
for num in range(30, 19, -1):
    print(num)
print()
