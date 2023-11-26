"""
CP1404 Practical 10 Hunter Kruger-Ilingworth
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set default odometer correctly"
    assert test_car.fuel == 0, "Car does not set default fuel correctly"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly when passing the value in"


run_tests()


def format_phrase_as_sentence(sentence):
    """
     format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('meow meow meow')
    'Meow meow meow.'
    """
    if sentence[-1] != ".":
        sentence += "."
    return sentence.capitalize()


doctest.testmod()
