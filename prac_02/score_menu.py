"""
CP1404 Practical 02 Hunter Kruger-Ilingworth
Brief:
Write a complete Python program following the standard structure that uses a main and other functions.
Use a main menu following the standard menu pattern.

The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive) (P)rint result (copy or import your function to determine the result
from score.py) (S)how stars (this should print as many stars as the score) (Q)uit Handle each of these (except quit)
separately, and consider how you can reuse your functions. In main(), before the menu loop, get the valid score. When
the user quits, say some kind of "farewell"."""


def main():
    menu = """(G)et a valid score 
(P)rint result 
(S)how stars 
(Q)uit"""
    score = int(input("Enter a score between 1 and 100: "))
    while is_invalid_score(score):
        print("Invalid score")
        score = int(input("Enter a score between 1 and 100: "))

    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter a score between 1 and 100: "))
            while is_invalid_score(score):
                print("Invalid score")
                score = int(input("Enter a score between 1 and 100: "))
        elif choice == "P":
            print(determine_performance(score))
        elif choice == "S":
            print(score*"*")
        else:
            # Invalid option
            print("Invalid")
            pass
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell")


def is_invalid_score(score):
    return score < 0 or score > 100


def determine_performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
