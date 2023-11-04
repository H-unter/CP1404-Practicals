"""
Time estimate: 1:30
Start time: 12:21
Break: 12:49
Resume: 1:30
Stop 2:30
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
    """"Add, edit and manipulate list of projects"""
    projects = read_from_file()
    menu_choice = input(f"{MENUSTRING}").lower()
    while menu_choice != "q":
        if menu_choice == "l":  # (L)oad projects
            projects = read_from_file()
        elif menu_choice == "s":  # (S)ave projects
            write_to_file(projects)
        elif menu_choice == "d":  # (D)isplay projects
            display_projects(projects)
        elif menu_choice == "f":  # (F)ilter projects by date
            filter_projects(projects)  # does not change the data
        elif menu_choice == "a":  # (A)dd new project
            projects = add_new_project(projects)
        elif menu_choice == "u":  # (U)pdate project
            projects = update_project(projects)
        else:
            print("Invalid menu choice")
        menu_choice = input(f"{MENUSTRING}").lower()


def read_from_file():
    """"Load projects from file"""
    projects = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()  # get rid of header
        for line in in_file:
            parts = line.strip().split('\t')
            projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))  # add to list of projects
    return projects


def write_to_file(projects):
    """"Write changes made to file"""
    with open(FILENAME, "w") as out_file:
        print(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            out_file.write(project.to_line() + '\n')


def display_projects(projects):
    """Display projects"""
    for project in projects:
        print(project)


def add_new_project(projects):
    """"Add new project"""
    name = input("Let's add a new project\nName: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    estimated_cost = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    new_project = Project(name, start_date, priority, estimated_cost, completion_percentage)
    projects.append(new_project)
    return projects


def update_project(projects):
    """"Update completion and priority of project"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        edited_project = projects[int(input("Project choice: "))]
        print(edited_project)
        completion_percentage = int(input("New Percentage: "))
        priority = int(input("New Priority: "))
        edited_project.completion_percentage = completion_percentage
        edited_project.priority = priority
    except (ValueError, IndexError):
        print(f"An error occurred")
    return projects


def filter_projects(projects):
    """"Filter projects by date"""
    cutoff_date = input("Show projects that start after date (dd/mm/yy): ")
    datetime.datetime.strptime(cutoff_date, "%d/%m/%y").date()
    filtered_projects = [project for project in projects if project.start_date > cutoff_date]
    display_projects(filtered_projects)


main()
