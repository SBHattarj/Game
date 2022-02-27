from Vector import Vector2D
from typing import Iterable

class Line:
    def __init__(
        self,
        start: Iterable[float, float] | Vector2D,
        end: Iterable[float, float] | Vector2D
    ):
        self.start = start
        self.end = end
        self.direction = end - start