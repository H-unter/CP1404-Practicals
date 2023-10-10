"""Start 8:31"""


def main():
    email = get_email_and_name()
    while email != "":
        email = get_email_and_name()


def get_email_and_name():
    email = input("Enter input: ")
    while len(email.split("@")) != 2:
        email = input("INVALID! Re-enter input: ")
    name = email.split("@")[0]
    prompt = input(f"is {name} your name?").lower()
    while prompt not in ['y', 'n']:
        prompt = input(f"Come again? is {name} your name?").lower()
    if prompt == 'n':
        print("Drats, enter your actual name:")
    return email


main()
