"""
Start: 7:12
End:
"""

from programming_language import ProgrammingLanguage


def main():
    print("Hello World!")
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)


main()
