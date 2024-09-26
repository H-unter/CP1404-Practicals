"""
CP1404 Practical 09 Hunter Kruger-Ilingworth
Taxi simulator program
"""
from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU_STRING = f"""
    q)uit, c)hoose taxi, d)rive
    >>> """


def main():
    """Taxi simulator that makes use of the Taxi and SilverServiceTaxi subclasses"""
    print("Let's drive! ")
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.0

    print(f"Bill to date: ${bill}")
    choice = input(MENU_STRING).lower()
    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == 'd':
            bill = drive_taxi(taxis, current_taxi, bill)
        print(f"Bill to date: ${bill}")
        choice = input(MENU_STRING).lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(taxis, current_taxi, bill):
    """Drive the chosen Taxi and update the bill"""
    if not current_taxi:
        print("You need to choose a taxi before you can drive")
    else:
        distance = int(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        bill += current_taxi.get_fare()
    return bill


def choose_taxi(taxis, current_taxi):
    """Choose a Taxi"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    except ValueError:
        print("Not a valid number")
    except IndexError:
        print("Invalid option")
    return current_taxi


if __name__ == "__main__":
    main()
