"""Clean Code in Python - Chapter 3: General Traits of Good Code

> Exceptions
"""


class InternalDataError(Exception):
    """An exception with the data of our domain problem."""


def process(data_dictionary, record_id):
    try:
        return data_dictionary[record_id]
    except KeyError as e:
        raise InternalDataError("Record not present") from e
