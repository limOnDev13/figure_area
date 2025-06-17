"""The module responsible for testing the Triangle."""

from typing import Any

import pytest

from figure_area.figures import Triangle


def test_calculating_triangle_area():
    """Test calculating method Triangle.area()."""
    a: Any
    b: Any
    c: Any
    a, b, c = 1, 1, 1
    p = (a + b + c) / 2
    assert (
        pow(p * (p - a) * (p - b) * (p - c), 0.5) == Triangle(a, b, c).area()
    )

    a, b, c = 2.17, 35.011, 0.121212
    p = (a + b + c) / 2
    assert (
        pow(p * (p - a) * (p - b) * (p - c), 0.5) == Triangle(a, b, c).area()
    )

    a, b, c = 0, 1, 1
    assert 0 == Triangle(a, b, c).area()

    a, b, c = -1, 12, 3
    try:
        Triangle(a, b, c)
    except ValueError:
        pass
    else:
        pytest.fail()

    a, b, c = 12, "13", 1
    try:
        Triangle(a, b, c)
    except TypeError:
        pass
    else:
        pytest.fail()
