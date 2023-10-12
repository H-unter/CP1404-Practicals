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
print(lowercase_colour_to_hex)
requested_colour = input("Enter colour name: ").lower()
while requested_colour != "":
    requested_colour = input("Enter colour name: ").lower()
    if requested_colour in list(lowercase_colour_to_hex.keys()):
        print(f"{requested_colour} Requested hex value: {lowercase_colour_to_hex[requested_colour]}")
