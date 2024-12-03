"""

"""

def main():
    try:
        years = get_positive_int("How many years are in the rainfall sample? ")
        for year in range(years): # loop and call
            annual_rainfall = inputs(year + 1) #
            average_annual_rainfall = processing(annual_rainfall, 12)
            outputs(annual_rainfall, average_annual_rainfall, year + 1)
        # ADD RESTART CODE HERE
    except Exception as err:
        print("An unexpected error occurred: " + str(err))


def inputs(year):
    pass # replace this with your code to get all the monthly rainfall values for a single year and then return the
         # total for the year


def processing(rainfall, period):
    pass # replace this with your code to calculate and return the average from the variables above.
         # This is for a single year!


def outputs(total_rainfall, average_rainfall, year):
    pass # replace this with your code for outputs, using the variables above
         # This is for a single year!


def get_positive_int(prompt):
    """
    This function is guaranteed to return a positive (>= 0) integer.

    @param prompt: The text to be shown to the user asking them for input
    @return: a positive (>= 0) integer
    """
    while True: # keep looping until successful
        try: # catch errors if the user enters something that can't be turned into an int
            value = int(input(prompt))
            if value < 0:
                print("The number has to be positive.") # The loop will continue to run after this
            else:
                break # no errors and >= 0, so we can end
        except:
            print("Only digits are allowed.") # printed if an error happened when trying to turn input into an int
    return value # we're out of the loop, so return the value


main()
