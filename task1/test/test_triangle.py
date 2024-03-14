from src.Figures.Triangle import Triangle
import pytest


def test_init_pos():
    a = 3
    b = 4
    c = 5
    test_triangle = Triangle(a, b, c)
    assert test_triangle.a == a
    assert test_triangle.b == b
    assert test_triangle.c == c


def test_init_neg():
     with pytest.raises(Exception):
           test_triangle = Triangle(1, 2, 4)


def test_get_perimeter():
     test_triangle = Triangle(3, 4, 5)
     assert test_triangle.get_perimeter() == 12.0


def test_get_area():
     test_triangle = Triangle(3, 4, 5)
     assert test_triangle.get_area() == 6.0


def test_is_right_triangle_pos():
     test_triangle = Triangle(3, 4, 5)
     assert test_triangle.is_right_triangle() == True

    
def test_is_right_triangle_neg():
     test_triangle = Triangle(3, 4, 6)
     assert test_triangle.is_right_triangle() == False