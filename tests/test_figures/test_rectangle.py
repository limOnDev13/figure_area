"""The module responsible for testing the Rectangle."""

from typing import Any

import pytest

from figure_area.figures import Rectangle


def test_calculating_rectangle_area():
    """Test calculating method Rectangle.area()."""
    a: Any
    b: Any
    a, b = 1, 1
    assert 1 == Rectangle(a, b).area()

    a, b = 2.17, 35.011
    assert a * b == Rectangle(a, b).area()

    a, b = 0, 0
    assert 0 == Rectangle(a, b).area()

    a, b = -1, 12
    try:
        Rectangle(a, b)
    except ValueError:
        pass
    else:
        pytest.fail()

    a, b = 12, "13"
    try:
        Rectangle(a, b)
    except TypeError:
        pass
    else:
        pytest.fail()
