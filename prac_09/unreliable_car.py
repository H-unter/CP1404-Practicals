"""
CP1404 Practical 09 Hunter Kruger-Ilingworth
UnreliableCar class
"""

from car import Car
import random


class UnreliableCar(Car):
    """UnreliableCar class is a subclass of Car"""

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but factor in reliability as well"""
        num = random.randint(0, 100)
        if num < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
