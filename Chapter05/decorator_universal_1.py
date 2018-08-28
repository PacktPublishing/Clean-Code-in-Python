"""Clean Code in Python - Chapter 5: Decorators

Universal Decorators: create decorators that can be applied to several
different objects (e.g. functions, methods), and won't fail.

"""
from functools import wraps

from log import logger


class DBDriver:
    def __init__(self, dbstring):
        self.dbstring = dbstring

    def execute(self, query):
        return f"query {query} at {self.dbstring}"


def inject_db_driver(function):
    """This decorator converts the parameter by creating a ``DBDriver``
    instance from the database dsn string.
    """

    @wraps(function)
    def wrapped(dbstring):
        return function(DBDriver(dbstring))

    return wrapped


@inject_db_driver
def run_query(driver):
    return driver.execute("test_function")


class DataHandler:
    """The decorator will not work for methods as it is defined."""

    @inject_db_driver
    def run_query(self, driver):
        return driver.execute(self.__class__.__name__)
