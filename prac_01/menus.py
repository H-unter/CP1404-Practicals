"""
CP1404 Practical 01 Hunter Kruger-Ilingworth
Simple Menu Demonstration
"""

menu_string = """(H)ello
(G)oodbye
(Q)uit
>>> """

name = input("Enter Name: ")
choice = input(menu_string).upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid Message")
    choice = input(menu_string).upper()
print("Finished.")
