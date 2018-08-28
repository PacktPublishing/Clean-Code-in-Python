"""Clean Code in Python - Chapter 6: Descriptors

> How Python uses descriptors internally: __slots__
"""

class Coordinate2D:
    """
    >>> coord = Coordinate2D(1, 2)
    >>> repr(coord)
    'Coordinate2D(1, 2)'
    """
    __slots__ = ("lat", "long")

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __repr__(self):
        return f"{self.__class__.__name__}({self.lat}, {self.long})"
