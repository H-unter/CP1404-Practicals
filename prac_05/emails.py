"""
CP1404 Practical 05 Hunter Kruger-Ilingworth
Estimate: 30 mins
Actual: 37 mins
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = email.split("@")[0]  # take portion before @ symbol
        name_confirmation = input(f"is your name {name}? (Y/n) ").lower()
        if name_confirmation not in ['y', '']:
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print("")  # newline to match sample output
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
