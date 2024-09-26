"""
CP1404 Practical 09 Hunter Kruger-Ilingworth
Testing code for silver service taxi
"""
from silver_service_taxi import SilverServiceTaxi

# For an 18 km trip in a SilverServiceTaxi with fanciness of 2, the fare should be $48.78 (yikes!)

fancy_taxi = SilverServiceTaxi("Golden Car", 100, 2)
fancy_taxi.start_fare()
fancy_taxi.drive(18)
print(fancy_taxi.get_fare())
