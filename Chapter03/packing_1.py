"""Clean Code in Python - Chapter 3: General Traits of Good Code

> Packing / unpacking
"""


USERS = [(i, f"first_name_{i}", f"last_name_{i}") for i in range(1_000)]


class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.user_id!r}, {self.first_name!r}, {self.last_name!r})"


def bad_users_from_rows(dbrows) -> list:
    """A bad case (non-pythonic) of creating ``User``s from DB rows."""
    return [User(row[0], row[1], row[2]) for row in dbrows]


def users_from_rows(dbrows) -> list:
    """Create ``User``s from DB rows."""
    return [
        User(user_id, first_name, last_name)
        for (user_id, first_name, last_name) in dbrows
    ]
