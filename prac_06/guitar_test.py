"""
Start: 7:35

"""

from guitar import Guitar


def main():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another guitar", 2013, 4.50)

    print(f"{guitar.name} get_age() - Expected {2023 - 1922}. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {2023 - 2013}. Got {another_guitar.get_age()}")

    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")


main()
