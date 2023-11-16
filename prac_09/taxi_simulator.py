"""
Taxi simulator program
"""
from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU_STRING = f"""
    q)uit, c)hoose taxi, d)rive
    >>> """


def main():
    print("Let's drive! ")
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    my_taxi = SilverServiceTaxi("Gerald", 150, 60)
    current_taxi = None
    bill = 0

    print(f"Bill to date: ${bill}")
    choice = input(MENU_STRING).lower()
    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            bill = drive_taxi(taxis, current_taxi, bill)
        print(f"Bill to date: ${bill}")
        choice = input(MENU_STRING).lower()


def drive_taxi(taxis, current_taxi, bill):
    if current_taxi == None:
        print("You need to choose a taxi before you can drive")
    else:
        distance = int(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        bill += current_taxi.get_fare()
    return bill


def choose_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    taxi_choice = int(input("Choose taxi: "))
    while taxi_choice not in range(0, len(taxis)):
        taxi_choice = input("Choose taxi in range: ")
    return taxis[taxi_choice]


main()
