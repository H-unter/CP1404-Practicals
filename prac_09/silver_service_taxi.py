"""
CP1404 Practical 09 Hunter Kruger-Ilingworth
SilverServiceTaxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi - a child of the Taxi class"""

    def __init__(self, name, fuel, fanciness):
        """Initialise an instance of a SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        self.flagfall = 4.50

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi"""
        return f"{super().__str__()} plus flagfall fare of ${self.flagfall}"

    def drive(self, distance):
        """Drive like parent Taxi"""
        distance_driven = super().drive(distance)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
