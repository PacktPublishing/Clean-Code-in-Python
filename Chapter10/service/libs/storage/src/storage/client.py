"""Abstraction to the database.

Provide a client to connect to the database and expose a custom API, at the
convenience of the application.

"""
import os

import asyncpg


def _extract_from_env(variable, *, default=None):
    try:
        return os.environ[variable]

    except KeyError as e:
        if default is not None:
            return default

        raise RuntimeError(f"Environment variable {variable} not set") from e


DBUSER = _extract_from_env("DBUSER")
DBPASSWORD = _extract_from_env("DBPASSWORD")
DBNAME = _extract_from_env("DBNAME")
DBHOST = _extract_from_env("DBHOST", default="127.0.0.1")
DBPORT = _extract_from_env("DBPORT", default=5432)


async def DBClient():
    return await asyncpg.connect(
        user=DBUSER,
        password=DBPASSWORD,
        database=DBNAME,
        host=DBHOST,
        port=DBPORT,
    )
