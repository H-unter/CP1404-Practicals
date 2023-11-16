"""
CP1404 Practical 09 Hunter Kruger-Ilingworth
Test the taxi and car classes
"""
from prac_09.taxi import Taxi

# Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
my_taxi = Taxi("Prius 1", 100)
# drive the taxi 40 km
my_taxi.drive(40)
# Print the taxi's details and the current fare
print(f"{my_taxi}, current fare: {my_taxi.get_fare()}")
# Restart the meter (start a new fare) and then drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)
# Print the details and the current fare
print(f"{my_taxi}, current fare: {my_taxi.get_fare()}")
