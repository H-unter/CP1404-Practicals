"""
Start: 7:35

"""

from guitar import Guitar


def main():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(f"{guitar}")

    print(guitar.is_vintage())


main()
