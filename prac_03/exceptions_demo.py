"""
CP1404 Practical 03 Hunter Kruger-Ilingworth
Answer the following questions:
1. When will a ValueError occur?
>>  when either the numerator or denominator are not numbers
2. When will a ZeroDivisionError occur?
>>  when the denominator is 0, and the numerator is a number
Could you change the code to avoid the possibility of a ZeroDivisionError?
>>  see corrected code below
"""
denominator = 0
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print(f"Denominator cannot be zero!")
        denominator = int(input("Re-enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
