"""Clean Code in Python - Chapter 2: Pythonic Code

> Dynamic Attributes

"""


class DynamicAttributes:
    """
    >>> dyn = DynamicAttributes("value")
    >>> dyn.attribute
    'value'

    >>> dyn.fallback_test
    '[fallback resolved] test'

    >>> dyn.__dict__["fallback_new"] = "new value"
    >>> dyn.fallback_new
    'new value'

    >>> getattr(dyn, "something", "default")
    'default'
    """

    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"
        raise AttributeError(
            f"{self.__class__.__name__} has no attribute {attr}"
        )
