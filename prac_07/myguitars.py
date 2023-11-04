""""
CP1404 Practical 07 Hunter Kruger-Ilingworth
Write a program to read all of these guitars and store them in a list of Guitar objects, using the class that you
wrote recently. Display these using a loop.
"""

from prac_07.guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        reader = csv.reader(in_file)
        for line in reader:
            print(line)
            guitars.append(Guitar(line[0], int(line[1]), float(line[2])))  # add to list of guitars

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitars.append(Guitar(name, year, cost))  # add to list of guitars
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")

    guitars.sort()

    for guitar in guitars:
        print(guitar)

    with open(FILENAME, "w", newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            print(guitar)
            writer.writerow([guitar.name, guitar.year, guitar.cost])
    print(f"{len(guitars)} guitars saved to {FILENAME}")


main()
