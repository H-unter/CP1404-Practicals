"""Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that
many lines of output. Each line consists of 6 random numbers between 1 and 45. These values should be stored as
CONSTANTS.

Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Study the formatting below so that numbers align neatly.
"""


def main():
    quick_picks_number = int(input("How many quick picks? "))
    print(quick_picks_number)

    column_length = 6
    row_length = quick_picks_number

    for row in range(row_length):
        print(column_length * " test ")


main()
