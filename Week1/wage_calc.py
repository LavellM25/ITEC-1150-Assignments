"""
Author: Lavell McGrone
Date: 2024-09-03
Description: Calculate and display sentence with a total that includes regular and overtime pay.
"""

# Define variables & amounts provided
reg_rate = 15.34
ot_rate = reg_rate * 1.5
reg_hours = 40
ot_hours = 10

# Calculate regular and overtime pay separately
reg_pay = round(reg_hours * reg_rate, 2)
ot_pay = round(ot_hours * ot_rate, 2)

# Calculate the gross pay and total hours worked
gross_pay = round(reg_pay + ot_pay, 2)
total_hours = reg_hours + ot_hours

# Display the gross amount, formatted in a sentence
print(f'Your gross pay is ${gross_pay:,.2f}.')
