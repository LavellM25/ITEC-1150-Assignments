"""
Author: Lavell McGrone
Date: 2024-09-04
Description: Calculate amount spent on bus fares this month
"""
# Define Variables
reg_fare = 1.75
rush_fare = 3
reg_rides = 7
rush_rides = 12

# Calculate amount spent this month at the bus fare
reg_cost = reg_rides * reg_fare
rush_cost = rush_rides * rush_fare

# Calculate monthly total cost at the bus fare
monthly_total_cost = reg_cost + rush_cost


# Display the total amount spent on bus fare
print(f"This month I spent ${monthly_total_cost:,.2f} on bus fare.")
