"""Hunter Kruger-Ilingworth write a program that asks the user for a password, with error-checking to repeat if the
password doesn't meet a minimum length set by a variable. The program should then print asterisks as long as the
word. Example: if the user enters Pythonista (10 characters), the program should print **********."""


def main():
    minimum_length = 3
    password = get_password(minimum_length)

    print_asterisks(password)


def print_asterisks(password):
    print(len(password) * "*")


def get_password(minimum_length):
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long.")
        password = input("Renter password: ")
    return password


main()
