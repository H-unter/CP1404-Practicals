"""
CP1404 Practical 09 Hunter Kruger-Ilingworth
Car class
it adds new attributes (price_per_km, current_fare_distance) and methods (get_fare, start_fare)
it overrides methods (drive, __init__ and __str__) to take account of the characteristics of a Taxi.
"""
from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = 1.23
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return round(self.price_per_km * self.current_fare_distance, 1)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
