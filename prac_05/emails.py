"""
CP1404 Practical 05 Hunter Kruger-Ilingworth
Estimate: 30 mins
Actual: 37 mins
"""


def main():
    """Ask user for email and name and store into dictionary"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = infer_name_from_email(email)
        name_confirmation = input(f"is your name {name}? (Y/n) ").lower()
        if name_confirmation not in ['y', '']:
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print("")  # newline to match sample output
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def infer_name_from_email(email):
    """Parse email to infer name"""
    name = email.split("@")[0]
    name = name.split(".")
    name = " ".join(name).title()
    return name


main()
