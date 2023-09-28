"""
CP1404 Practical 03 Hunter Kruger-Ilingworth
Checks the validity of an inputted integer
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        is_finished = True
print("Valid result is:", result)
