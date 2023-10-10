file_name = "countries.csv"
countries = {}
with open(file_name, "r") as in_file:
    for line in in_file:
        if line != "Country (or territory),Capital,Population,% of country,Source":
            print(line)
            new_line = line.strip().split(',')
            countries[new_line[0]] = new_line[1:]
