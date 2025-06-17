"""The module responsible for implementing the triangle."""

from .base import Figure


class Triangle(Figure):
    """A class that encapsulates the properties of a triangle."""

    def __init__(self, a: float, b: float, c: float):
        """
        Init class.

        :param a: first side of the triangle.
        :param b: second side of the triangle.
        :param c: third side of the triangle.

        :raise ValueError: If a < 0 or b < 0 or c < 0.
        :raise TypeError: If a or b or c are not int or float.
        """
        if a < 0 or b < 0 or c < 0:
            raise ValueError(
                f"Triangle side can not be less then 0. "
                f"a = {a}, b = {b}, c = {c}"
            )
        if not (
            (isinstance(a, int) or isinstance(a, float))
            and (isinstance(b, int) or isinstance(b, float))
            and (isinstance(c, int) or isinstance(c, float))
        ):
            raise TypeError(
                f"Side of triangle must be int or float. "
                f"{type(a)=}, {type(b)=}, {type(c)=}"
            )

        self.a = a
        self.b = b
        self.c = c

    def perimeter(self) -> float:
        """Calculate triangle perimeter."""
        return self.a + self.b + self.c

    def area(self) -> float:
        """Calculate triangle area."""
        half_p = self.perimeter() / 2
        return pow(
            half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c),
            0.5,
        )
