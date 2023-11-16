"""
Band Class, that has musicians by association
"""


class Band():
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __repr__(self):
        musicians_str = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name}:\n{musicians_str}"

    def add(self, new_musician):
        self.musicians.append(new_musician)

    def play(self):
        for i in self.musicians:
            print(f"{self.musicians[i]}")
