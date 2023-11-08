"""
CP1404 Practical 01 Hunter Kruger-Ilingworth
Program to demonstrate for loop functionality
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print("\n")

for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")

for i in range(20, 1, -1):
    print(i, end=' ')
print("\n")

n = int(input("What number of stars would you like? "))
for i in range(0, n + 1, 1):
    print(i * "*")  # display i number of stars
