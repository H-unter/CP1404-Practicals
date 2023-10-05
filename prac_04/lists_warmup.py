"""
CP1404 Practical 04 Hunter Kruger-Ilingworth
Program to test functionality of lists
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])  # Output: 3
print(numbers[-1])  # Output: 5
print(numbers[3])  # Output: 1
print(numbers[:-1])  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numbers[3:4])  # Output: [1]
print(5 in numbers)  # Output: True
print(7 in numbers)  # Output: False
print("3" in numbers)  # Output: False
print(numbers + [6, 5, 3])  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 6, 5, 3]

numbers[0] = "ten"
numbers[-1] = 1
print(len(numbers))
print([numbers[i] for i in range(len(numbers)) if i > 1])
print(9 in numbers)
