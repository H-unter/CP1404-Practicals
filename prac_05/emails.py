"""
CP1404 Practical 05 Hunter Kruger-Ilingworth
Estimate: 30 mins
Actual: 37 mins
"""


def main():
    name_to_email = {}
    pair = get_pair()
    while get_pair() != "":
        print(f"to be appended:{pair}")
        name_to_email[pair[0]] = pair[1]
        print(f"dictionary: {name_to_email}")
        pair = get_pair()

    print("DONE YAAY")


def get_pair():
    email = input("Email: ")
    if email == "":
        return ""
    name = email.split("@")[0]  # take portion before @ symbol
    prompt = input(f"is your name {name}? (Y/N) ").lower()
    while prompt not in ['y', '']:
        name = input("Name: ")

    return [name, email]


main()
