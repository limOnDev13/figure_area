"""The module responsible for testing the Circle."""

from math import pi
from typing import Any

import pytest

from figure_area.figures import Circle


def test_calculating_circle_area():
    """Test calculating method Circle.area()."""
    radius: Any = 1
    assert round(pi, 5) == round(Circle(radius=radius).area(), 5)

    radius = 2.17
    assert round(pi * radius**2, 5) == round(Circle(radius=radius).area(), 5)

    radius = 0
    assert Circle(radius=radius).area() == 0

    radius = -100
    try:
        Circle(radius=radius)
    except ValueError:
        pass
    else:
        pytest.fail()

    radius = "100"
    try:
        Circle(radius=radius)
    except TypeError:
        pass
    else:
        pytest.fail()
