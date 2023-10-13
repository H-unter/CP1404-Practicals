""""
CP1404 Practical 05 Hunter Kruger-Ilingworth
Program to determine hex value from colour name
"""

COLOUR_TO_HEX = {
    'Absolute Zero': '#0048ba',
    'Acid Green': '#b0bf1a',
    'AliceBlue': '#f0f8ff',
    'Alizarin crimson': '#e32636',
    'Amaranth': '#e52b50',
    'Amber': '#ffbf00',
    'Amethyst': '#9966cc',
    'AntiqueWhite': '#faebd7',
    'AntiqueWhite1': '#ffefdb',
    'AntiqueWhite2': '#eedfcc'
}  # raw output from website

lowercase_colour_to_hex = {colour.lower(): hex_value for colour, hex_value in COLOUR_TO_HEX.items()}

requested_colour = input("Enter colour name: ").lower()
while requested_colour != "":
    if requested_colour in list(lowercase_colour_to_hex.keys()):
        print(f"The hex value of {requested_colour} is {lowercase_colour_to_hex[requested_colour]}")
    else:
        print(f"Error: {requested_colour} not in colour list")
    requested_colour = input("Enter colour name: ").lower()
