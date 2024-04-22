"""Challenge Question 8."""
from __future__ import annotations
__author__ = "730395850"


class Point:
    """This is a Point class that has both an x and a y attribute."""
    # attributes
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Initializes the Point with x and y."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scales the Point given a factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returns a new point that is scaled by a given factor."""
        x = self.x * factor
        y = self.y * factor
        return Point(x, y)