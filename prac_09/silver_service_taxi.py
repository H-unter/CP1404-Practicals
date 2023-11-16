from taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        self.flagfall = 4.50

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance}km on current fare, {self.price_per_km}/km plus flagfall of ${self.flagfall}"

    def drive(self, distance):
        """Drive like parent Taxi"""
        distance_driven = super().drive(distance)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
