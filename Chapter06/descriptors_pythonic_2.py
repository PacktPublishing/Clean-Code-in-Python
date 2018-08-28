"""Clean Code in Python - Chapter 6: Descriptors

> A Pythonic Implementation

"""


class HistoryTracedAttribute:
    """Trace the values of this attribute into another one given by the name at
    ``trace_attribute_name``.
    """

    def __init__(self, trace_attribute_name: str) -> None:
        self.trace_attribute_name = trace_attribute_name
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        self._track_change_in_value_for_instance(instance, value)
        instance.__dict__[self._name] = value

    def _track_change_in_value_for_instance(self, instance, value):
        self._set_default(instance)
        if self._needs_to_track_change(instance, value):
            instance.__dict__[self.trace_attribute_name].append(value)

    def _needs_to_track_change(self, instance, value) -> bool:
        """Determine if the value change needs to be traced or not.

        Rules for adding a value to the trace:
            * If the value is not previously set (it's the first one).
            * If the new value is != than the current one.
        """
        try:
            current_value = instance.__dict__[self._name]
        except KeyError:
            return True
        return value != current_value

    def _set_default(self, instance):
        instance.__dict__.setdefault(self.trace_attribute_name, [])


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

    current_city = HistoryTracedAttribute("cities_visited")

    def __init__(self, name, current_city):
        self.name = name
        self.current_city = current_city
