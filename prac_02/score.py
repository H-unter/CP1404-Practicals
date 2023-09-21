"""
CP1404 Practical 01 Hunter Kruger-Ilingworth
Program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(determine_performance(score))


def determine_performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
