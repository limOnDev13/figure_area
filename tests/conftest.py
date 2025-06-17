"""Pytest fixtures."""

import random
from typing import List

import pytest

from figure_area.figures import (
    Circle,
    Rectangle,
    Triangle,
)


@pytest.fixture()
def rectangles() -> List[Rectangle]:
    """Get 100 random rectangles."""
    return [
        Rectangle(random.uniform(0, 100), random.uniform(0, 100))
        for _ in range(100)
    ]


@pytest.fixture()
def circles() -> List[Circle]:
    """Get 100 random circles."""
    return [Circle(random.uniform(0, 100)) for _ in range(100)]


@pytest.fixture()
def triangles() -> List[Triangle]:
    """Get 100 random triangles."""
    return [
        Triangle(
            random.uniform(0, 100),
            random.uniform(0, 100),
            random.uniform(0, 100),
        )
        for _ in range(100)
    ]
