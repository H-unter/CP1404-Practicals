class ProgrammingLanguage:
    """Represent the key information of a programming language"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return formatted programming language information"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if the languages typing is dynamic"""
        return self.typing == "Dynamic"
