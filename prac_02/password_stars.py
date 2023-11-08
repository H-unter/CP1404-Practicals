"""
CP1404 Practical 02 Hunter Kruger-Ilingworth
Program to get valid password and print asterisks equal to the password's length
"""


def main():
    """Acquire password that meets minimum length requirements and prints stars"""
    minimum_length = 3
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password):
    """Print amount of asterisks equal to the length of the input string"""
    print(len(password) * "*")


def get_password(minimum_length):
    """Get valid password from the user"""
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long.")
        password = input("Renter password: ")
    return password


main()
