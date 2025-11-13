from __future__ import annotations
from typing import Any


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        elif isinstance(other, (float, int)):
            return Distance(self.km + other)

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, (float, int)):
            self.km = self.km + other
            return self
        elif isinstance(other, Distance):
            self.km = self.km + other.km
            return self

    def __mul__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km * other
            )
        elif isinstance(other, Distance):
            return None

    def __eq__(self, other: int | float | Distance) -> Any:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __lt__(self, other: int | float | Distance) -> Any:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

    def __le__(self, other: int | float | Distance) -> Any:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

    def __gt__(self, other: int | float | Distance) -> Any:
        if isinstance(other, Distance):
            return self.km > other.km

        if isinstance(other, (int, float)):
            return self.km > other

        return NotImplemented

    def __ge__(self, other: int | float | Distance) -> Any:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other

    def __truediv__(self, other: Any) -> Distance:
        km = round(self.km / other, 2)
        return Distance(
            km=km
        )
