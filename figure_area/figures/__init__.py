"""
The package responsible for the shapes.

The base class of all shapes is the abstract Figure class.
To create a custom shape, you need to inherit your class from the Figure class
and implement the area method to calculate the area of the shape.
"""

from .base import Figure
from .circle import Circle
from .rectangle import Rectangle
from .triangle import Triangle
