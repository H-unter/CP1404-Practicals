""""
CP1404 Practical 05 Hunter Kruger-Ilingworth
From Wimbledon:
the champions and how many times they have won.
the countries of the champions in alphabetical order
"""
import csv


def main():
    """Read Wimbledon data from file and output interesting findings"""
    name_to_times_won = {}
    victorious_countries = []
    file_name = 'wimbledon.csv'
    populate_data(file_name, name_to_times_won, victorious_countries)
    print_champions_data(name_to_times_won)
    print_countries_data(victorious_countries)


def print_countries_data(victorious_countries):
    """Print country winning data"""
    victorious_countries.sort()
    print(f"\nThese {len(victorious_countries)} countries have won Wimbledon: ")
    print(', '.join([country for country in victorious_countries]))


def print_champions_data(name_to_times_won):
    """Print athlete winning data"""
    print(f"Wimbledon Champions:")
    for name, times_won in name_to_times_won.items():
        print(f"{name} {times_won}")


def populate_data(file_name, name_to_times_won, victorious_countries):
    """"Populate name_to_times_won and victorious_countries based on contents of wimbledon.csv"""
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # remove header from file reading
        for line in reader:
            country = line[1]
            name = line[2]
            if country not in victorious_countries:
                victorious_countries.append(country)
            if name in list(name_to_times_won.keys()):
                name_to_times_won[name] += 1
            else:
                name_to_times_won[name] = 1


main()
