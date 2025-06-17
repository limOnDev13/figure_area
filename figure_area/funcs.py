"""A module responsible for various library functions."""

from typing import TypeVar

from figure_area.figures import Figure

F = TypeVar("F", bound=Figure)


def calculate_area(figure: F) -> float:
    """Calculate figure area."""
    return figure.area()
