"""Clean Code in Python - Chapter 8: Unit Testing

> Mock Objects

    - File under test: mock_1.py

"""

from unittest.mock import MagicMock

from mock_1 import GitBranch, author_by_id


def test_find_commit():
    branch = GitBranch([{"id": "123", "author": "dev1"}])
    assert author_by_id("123", branch) == "dev1"


def test_find_any():
    mbranch = MagicMock()
    mbranch.__getitem__.return_value = {"author": "test"}
    assert author_by_id("123", mbranch) == "test"
