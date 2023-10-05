"""Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that
many lines of output. Each line consists of 6 random numbers between 1 and 45. These values should be stored as
CONSTANTS.

Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Study the formatting below so that numbers align neatly.
"""

import random


def main():
    quick_picks_number = int(input("How many quick picks? "))
    print(quick_picks_number)

    column_length = 6
    row_length = quick_picks_number

    for row in range(row_length):
        number_list = get_random_list(column_length)
        print(', '.join([str(number) for number in number_list]))


def get_random_list(column_length):
    number_list = []
    for column in range(column_length):
        new_number = random.randint(1, 45)
        while new_number in number_list:  # ensure no repeated numbers
            new_number = random.randint(1, 45)
        number_list.append(new_number)
    return sorted(number_list)


main()
