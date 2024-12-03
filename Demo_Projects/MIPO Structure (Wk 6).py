"""
Author: Erik Granse, adapted from M. Bock 6/13/2019
Date: 2024-02-10
Description: this program figures volume of a rectangular solid, but more importantly, it provides a model of functions
 talking to each other, int validation, exception handling and restart
"""


def main():
    """
    Main execution control method.
    :return: None
    """
    print('This program calculates the volume of a box. ')
    try:
        length, width, height = inputs()
        volume = processing(length, width, height)
        outputs(volume)
        restart = input('Continue? Enter y or n: ')
        if restart == 'y' or restart == 'Y':
            print('OK, let\'s calculate volume of another box.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:
        print(err)


def inputs():
    """
    Gathers and validates input from the user about the dimensions of a box.

    :return: the length, width, and height of the box. Guaranteed to be positive numbers.
    """
    length = get_pos_num('What\'s the length of the box? ')
    width = get_pos_num('What\'s the width? ')
    height = get_pos_num('What\'s the height? ')
    return length, width, height


def processing(length, width, height):
    """
    Core program logic which calculates the volume of a cubic solid.

    :param length: A positive number representing the length of a cubic solid
    :param width: A positive number representing the width of a cubic solid
    :param height: A positive number representing the height of a cubic solid
    :return: A positive number representing the volume of a cubic solid as specified by the parameters above.
    """
    volume = length * width * height
    return volume


def outputs(volume):
    """
    Displays the result to the user.

    :param volume: Inserted into the message.
    :return: None
    """
    print(f'The volume of the object is: {volume:.2f} cubic units.')


def get_pos_num(prompt):
    """
    Gets a positive number from a user. Prompts the user for a number, validates that it's a positive number, and
    will not return until a valid entry is received.

    :return: A positive number
    """
    while True:
        try:
            pos_int = float(input(f'{prompt} (positive numbers only) '))
            if pos_int >= 0:
                break
            else:
                print("The number must be greater than zero.")
        except:
            print("Only digits and a decimal point are allowed.")
    return pos_int


main()
