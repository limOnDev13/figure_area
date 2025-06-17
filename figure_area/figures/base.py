"""The module responsible for the shapes interface."""

from abc import ABC, abstractmethod


class Figure(ABC):
    """The base class that defines the interface of all shapes."""

    @abstractmethod
    def area(self) -> float:
        """Calculate figure area."""
        pass
