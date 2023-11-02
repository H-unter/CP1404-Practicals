"""
Time estimate: 1:30
Start time: 12:21
"""

MENUSTRING = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>>"""


def main():
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


main()
