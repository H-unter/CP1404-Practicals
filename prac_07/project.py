class Project:
    # name: ___ start: 20 / 07 / 2022, priority 1, estimate: $25.00, completion: 55 %
    def __init__(self, name, start_date, priority, estimated_cost, completion_percentage):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimated_cost = estimated_cost
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimated_cost}, "
                f"completion: {self.completion_percentage}%")
