"""
Time estimate: 1:30
Start time: 12:21
"""
from prac_07.project import Project
import csv

FILENAME = "projects.txt"

MENUSTRING = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>>"""


def main():
    projects = read_from_file(FILENAME)
    print(projects)

    menu_choice = input(f"{MENUSTRING}").lower()
    while menu_choice != "q":
        if menu_choice == "l":  # (L)oad projects
            pass
        elif menu_choice == "s":  # (S)ave projects
            pass
        elif menu_choice == "d":  # (D)isplay projects
            pass
        elif menu_choice == "f":  # (F)ilter projects by date
            pass
        elif menu_choice == "a":  # (A)dd new project
            pass
        elif menu_choice == "u":  # (U)pdate project
            pass
        else:
            print("Invalid menu choice")
            menu_choice = input(f"{MENUSTRING}").lower()


def read_from_file(FILENAME):
    projects = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()  # get rid of header
        for line in in_file:
            parts = line.strip().split('\t')
            projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))  # add to list of guitars
    return projects


main()
