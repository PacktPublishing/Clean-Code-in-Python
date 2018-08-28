"""Clean Code in Python - Chapter6: Getting more out of our objects with
descriptors

> Illustrate the basic workings of the descriptor protocol.
"""
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        logger.info(
            "Call: %s.__get__(%r, %r)",
            self.__class__.__name__,
            instance,
            owner,
        )
        return instance


class ClientClass:
    descriptor = DescriptorClass()
