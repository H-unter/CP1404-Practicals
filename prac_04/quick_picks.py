"""
CP1404 Practical 04 Hunter Kruger-Ilingworth

Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that
many lines of output. Each line consists of 6 random numbers between 1 and 45. These values should be stored as
CONSTANTS.

Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Study the formatting below so that numbers align neatly.
"""

import random

QUICK_PICK_LENGTH = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    quick_picks_number = int(input("How many quick picks? "))
    column_length = QUICK_PICK_LENGTH
    row_length = quick_picks_number

    for row in range(row_length):
        numbers = get_random_list(column_length)
        print(', '.join([str(number) for number in numbers]))


def get_random_list(column_length):
    numbers = []
    for column in range(column_length):
        new_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while new_number in numbers:  # ensure no repeated numbers
            new_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        numbers.append(new_number)
    return sorted(numbers)


main()
