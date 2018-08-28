"""Helper to generate test data."""
import os
from tempfile import gettempdir

PURCHASES_FILE = os.path.join(gettempdir(), "purchases.csv")


def create_purchases_file(filename, entries=1_000_000):
    if os.path.exists(PURCHASES_FILE):
        return

    with open(filename, "w+") as f:
        for i in range(entries):
            line = f"2018-01-01,{i}\n"
            f.write(line)


if __name__ == "__main__":
    create_purchases_file(PURCHASES_FILE)
