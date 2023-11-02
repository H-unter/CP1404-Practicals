"""
Time estimate: 1:30
Start time: 12:21
Break: 12:49
Resume: 1:30
"""
import datetime

from prac_07.project import Project

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

    menu_choice = input(f"{MENUSTRING}").lower()
    while menu_choice != "q":
        if menu_choice == "l":  # (L)oad projects
            projects = read_from_file(FILENAME)
        elif menu_choice == "s":  # (S)ave projects
            pass
        elif menu_choice == "d":  # (D)isplay projects
            display_projects(projects)
        elif menu_choice == "f":  # (F)ilter projects by date
            filter_projects(projects)  # does not change the data
        elif menu_choice == "a":  # (A)dd new project
            projects = add_new_project(projects)
        elif menu_choice == "u":  # (U)pdate project
            pass
            # projects = update_project(projects)
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


def display_projects(projects):
    for project in projects:
        print(project)


def add_new_project(projects):
    name = input("Let's add a new project\nName: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    estimated_cost = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    new_project = Project(name, start_date, priority, estimated_cost, completion_percentage)
    projects.append(new_project)
    return projects


def filter_projects(projects):
    cutoff_date = input("Show projects that start after date (dd/mm/yy): ")
    datetime.datetime.strptime(cutoff_date, "%d/%m/%y").date()
    filtered_projects = [project for project in projects if project.start_date > cutoff_date]
    display_projects(filtered_projects)


main()
