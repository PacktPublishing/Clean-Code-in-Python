"""Clean Code in Python - Chapter 6: Descriptors

> A Pythonic Implementation


"""
import time


class Traveller:
    """A person visiting several cities.

    We wish to track the path of the traveller, as he or she is visiting each
    new city.

    >>> alice = Traveller("Alice", "Barcelona")
    >>> alice.current_city = "Paris"
    >>> alice.current_city = "Brussels"
    >>> alice.current_city = "Amsterdam"

    >>> alice.cities_visited
    ['Barcelona', 'Paris', 'Brussels', 'Amsterdam']

    >>> alice.current_city
    'Amsterdam'

    >>> alice.current_city = "Amsterdam"
    >>> alice.cities_visited
    ['Barcelona', 'Paris', 'Brussels', 'Amsterdam']

    >>> bob = Traveller("Bob", "Rotterdam")
    >>> bob.current_city = "Amsterdam"
    >>> bob.current_city
    'Amsterdam'
    >>> bob.cities_visited
    ['Rotterdam', 'Amsterdam']

    """
    def __init__(self, name, current_city):
        self.name = name
        self._current_city = current_city
        self._cities_visited = [current_city]

    @property
    def current_city(self):
        return self._current_city

    @current_city.setter
    def current_city(self, new_city):
        if new_city != self._current_city:
            self._cities_visited.append(new_city)
        self._current_city = new_city

    @property
    def cities_visited(self):
        return self._cities_visited
