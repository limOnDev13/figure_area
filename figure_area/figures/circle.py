"""The module responsible for implementing the circle."""

from math import pi
from typing import Union

from .base import Figure


class Circle(Figure):
    """A class that encapsulates the properties of a circle."""

    def __init__(self, radius: Union[float | int]):
        """
        Init class.

        :param radius: Circle radius.

        :raise ValueError: If radius < 0.
        :raise TypeError: if radius is not numeric.
        """
        if radius < 0:
            raise ValueError(
                f"Circle radius can be less then 0. Circle radius = {radius}"
            )
        if not (isinstance(radius, int) or isinstance(radius, float)):
            raise TypeError(f"Radius must be int or float. {type(radius)=}")
        self.radius = radius

    def area(self) -> float:
        """Calculate circle area."""
        return pi * pow(self.radius, 2)
