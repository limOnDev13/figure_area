"""The module responsible for testing functions from the funcs module."""

from typing import List

from figure_area.figures import Circle, Rectangle, Triangle
from figure_area.funcs import calculate_area


def test_calculate_area(
    circles: List[Circle],
    triangles: List[Triangle],
    rectangles: List[Rectangle],
):
    """Test func calculate_area."""
    figures = circles + rectangles + triangles

    for figure in figures:
        assert figure.area() == calculate_area(figure)
