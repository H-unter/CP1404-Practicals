"""
CP1404 Practical 02 Hunter Kruger-Ilingworth
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(determine_performance(score))

    score_random = random.randint(0, 100)
    print(f"Random score: {score_random}")
    print(determine_performance(score_random))


def determine_performance(score):
    """Return a comment about performance based on an input score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
