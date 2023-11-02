from prac_07.guitar import Guitar
import csv

# Write a program to read all of these guitars and store them in a list of Guitar objects, using the class that you
# wrote recently. Display these using a loop.
FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        reader = csv.reader(in_file)
        for line in reader:
            print(line)
            guitars.append(Guitar(line[0], int(line[1]), float(line[2])))  # add to list of guitars

    guitars.sort()
    print(guitars)


main()
