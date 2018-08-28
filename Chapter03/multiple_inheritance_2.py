"""Clean Code in Python - Chapter 3: General traits of good code

> Multiple inheritance: Mixins

"""


class BaseTokenizer:
    """
    >>> tk = BaseTokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
    >>> list(tk)
    ['28a2320b', 'fd3f', '4627', '9792', 'a2b38e3c46b0']
    """

    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        yield from self.str_token.split("-")


class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())


class Tokenizer(UpperIterableMixin, BaseTokenizer):
    """
    >>> tk = Tokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
    >>> list(tk)
    ['28A2320B', 'FD3F', '4627', '9792', 'A2B38E3C46B0']
    """
