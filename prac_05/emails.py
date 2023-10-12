"""
Start 8:31
Working 8:46"""


def main():
    name_to_email = {}

    while get_pair() != "":
        pair = get_pair()
        print(f"to be appended:{pair}")
        name_to_email[pair[0]] = pair[1]
        print(f"dictionary: {name_to_email}")


def get_pair():
    email = input("Email: ")
    while len(email.split("@")) != 2:  # only 1 @ symbol is present in a valid email
        email = input("INVALID! Re-enter input: ")
    name = email.split("@")[0]
    prompt = input(f"is your name {name}? (Y/N) ").lower()
    while prompt not in ['y', 'n']:
        print("Invalid response.")
        prompt = input(f"is your name {name}? (Y/N) ").lower()
    if prompt == 'n':
        name = input("Name: ")

    return [name, email]


main()
