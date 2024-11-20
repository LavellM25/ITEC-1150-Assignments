"""
Author: Lavell McGrone
Date: 2024-09-19
Description: Check for Apollo first landing on moon given user output
"""

# Prompt for user input
year = int(input('What year did Apollo 1 land on the moon? '))

# Check if the year is correct
if year == 1969:
    print(f'Correct! {year} is right!')

# Check if the year is close to the correct year
elif year == 1968 or year == 1970:
    print(f'{year} is a close guess, but the correct answer is 1969.')

# For guesses more than 1 year away from the correct year
else:
    print(f'Sorry, {year} is the wrong answer. The correct answer is 1969.')
