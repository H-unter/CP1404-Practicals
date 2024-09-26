"""
Band Class, that has musicians by association
"""


class Band():
    """Band class containing instances of the Musician class"""

    def __init__(self, name):
        """Initialise a Band."""
        self.name = name
        self.musicians = []

    def __repr__(self):
        """Represent a Band."""
        musicians_string = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} {musicians_string}"

    def add(self, new_musician):
        """Add new member to Band."""
        self.musicians.append(new_musician)

    def play(self):
        """Use the play method in the musician class for all members in the Band"""
        return '\n'.join([musician.play() for musician in self.musicians])
