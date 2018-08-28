"""Clean Code in Python - Chapter 01: Introcution, Tools, and Formatting

Tests for annotations examples

"""
import pytest

from src.annotations import NewPoint, Point, locate


@pytest.mark.parametrize(
    "element,expected",
    (
        (locate, {"latitude": float, "longitude": float, "return": Point}),
        (NewPoint, {"lat": float, "long": float}),
    ),
)
def test_annotations(element, expected):
    """test the class/functions againts its expected annotations"""
    assert getattr(element, "__annotations__") == expected
