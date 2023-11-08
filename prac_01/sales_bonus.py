"""
CP1404 Practical 01 Hunter Kruger-Ilingworth
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales <= 0:  # invalid input detection
    print("Invalid input")
    sales = float(input("Enter sales: $"))

if sales < 1000:
    bonus_percentage = 0.10  # 10% bonus
else:
    bonus_percentage = 0.15  # 15% bonus
print(f"Bonus is {sales * bonus_percentage}")
