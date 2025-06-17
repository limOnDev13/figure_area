"""The module responsible for implementing the rectangle."""

from typing import Union

from .base import Figure


class Rectangle(Figure):
    """A class that encapsulates the properties of a rectangle."""

    def __init__(self, a: Union[int, float], b: Union[int, float]):
        """
        Init class.

        :param a: One side of the rectangle.
        :param b: Other side of the rectangle.

        :raise ValueError: If a < 0 or b < 0.
        :raise TypeError: If a or b are not int or float.
        """
        if a < 0 or b < 0:
            raise ValueError(
                f"Rectangle side can not be less then 0. a = {a}, b = {b}"
            )
        if not (
            (isinstance(a, int) or isinstance(a, float))
            and (isinstance(b, int) or isinstance(b, float))
        ):
            raise TypeError(
                f"Side of rectangle must be int or float. "
                f"{type(a)=}, {type(b)=}"
            )

        self.a = float(a)
        self.b = float(b)

    def area(self) -> float:
        """Calculate rectangle area."""
        return self.a * self.b
