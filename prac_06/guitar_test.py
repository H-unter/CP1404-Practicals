"""
Start: 7:35
End: 8:15
"""

from guitar import Guitar


# guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
# another_guitar = Guitar("Another guitar", 2013, 4.50)
#
# print(f"{guitar.name} get_age() - Expected {2023 - 1922}. Got {guitar.get_age()}")
# print(f"{another_guitar.name} get_age() - Expected {2023 - 2013}. Got {another_guitar.get_age()}")
#
# print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
# print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")
def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost} added.")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2010, 765.40))
    for i, guitar in enumerate(guitars):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
