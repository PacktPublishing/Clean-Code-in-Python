"""Clean Code in Python - Chapter 7: Using Generators

> The Interface for Iteration: sequences

"""

import logging

logger = logging.getLogger(__name__)


class SequenceWrapper:
    def __init__(self, original_sequence):
        self.seq = original_sequence

    def __getitem__(self, item):
        value = self.seq[item]
        logger.debug("%s getting %s", self.__class__.__name__, item)
        return value

    def __len__(self):
        return len(self.seq)


class MappedRange:
    """Apply a transformation to a range of numbers."""

    def __init__(self, transformation, start, end):
        self._transformation = transformation
        self._wrapped = range(start, end)

    def __getitem__(self, index):
        value = self._wrapped.__getitem__(index)
        result = self._transformation(value)
        logger.debug("Index %d: %s", index, result)
        return result

    def __len__(self):
        return len(self._wrapped)
