"""
CP1404 Practical 04 Hunter Kruger-Ilingworth
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read and display subject data stored in external file"""
    data = get_data()
    print_subject_info(data)


def get_data():
    """Read data and print raw result"""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(f"{parts}")  # See if that worked
        data.append(parts)
    input_file.close()
    return data


def print_subject_info(data):
    """Print data in a readable format"""
    for entry in range(len(data)):
        print(f"{data[entry][0]} is taught by {data[entry][1]} and has {data[entry][2]} students")


main()
