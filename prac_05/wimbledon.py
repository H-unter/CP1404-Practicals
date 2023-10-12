""""From data:
the champions and how many times they have won.
the countries of the champions in alphabetical order

Sample output:
Wimbledon Champions:
Rod Laver 2
...
Lleyton Hewitt 1
Roger Federer 8
Rafael Nadal 2
Novak Djokovic 7
Andy Murray 2

These 12 countries have won Wimbledon:
AUS, CRO, ESP, FRG, GBR, GER, NED, SRB, SUI, SWE, TCH, USA
"""
import csv

name_to_times_won = {}
victorious_countries = []

file_name = 'wimbledon.csv'
with open(file_name, "r", encoding="utf-8-sig") as in_file:
    reader = csv.reader(in_file)
    next(reader)  # remove header
    for line in reader:
        country = line[1]
        name = line[2]
        if country not in victorious_countries:
            victorious_countries.append(country)
        if name in list(name_to_times_won.keys()):
            name_to_times_won[name] += 1
        else:
            name_to_times_won[name] = 1

print(name_to_times_won)
print(victorious_countries)
