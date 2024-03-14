from src.Figures.Circle import Circle
import pytest


def test_init():
    radius = 5
    test_circle = Circle(radius)
    assert test_circle.radius == radius
    assert test_circle.pi == 3.14


def test_get_area():
    test_circle = Circle(5)
    assert test_circle.get_area() == 78.5