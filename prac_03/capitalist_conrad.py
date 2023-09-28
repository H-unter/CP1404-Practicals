"""
CP1404 Practical 03 Hunter Kruger-Ilingworth
Stock price simulator for a volatile stock.
"""
import random

OUTPUT_FILE = "output_file.txt"
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
number_of_days = 0

price = INITIAL_PRICE
print(f"On day {number_of_days} price is: ${price:,.2f}")
with open(OUTPUT_FILE, "w") as out_file:  # write to file in order to override previously written data
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    number_of_days += 1
    print(f"On day {number_of_days} price is: ${price:,.2f}")
    with open(OUTPUT_FILE, "a") as out_file:
        print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)
