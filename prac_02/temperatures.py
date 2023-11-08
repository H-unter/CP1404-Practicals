"""
CP1404 Practical 02 Hunter Kruger-Ilingworth
Temperature conversion program which can convert between Celsius and Fahrenheit
"""


def main():
    """Convert temperature between Celsius and Fahrenheit"""
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_in = float(input("Celsius: "))
            fahrenheit_out = convert_celsius_to_fahrenheit(celsius_in)
            print(f"Result: {fahrenheit_out:.2f} F")
        elif choice == "F":
            fahrenheit_in = float(input("Fahrenheit: "))
            celsius_out = convert_fahrenheit_to_celsius(fahrenheit_in)
            print(f"Result: {celsius_out:.2f} F")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
