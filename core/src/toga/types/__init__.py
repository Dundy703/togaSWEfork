from collections import namedtuple
from typing import TypeVar

Size = namedtuple("Size", ["width", "height"])
Position = namedtuple("Position", ["x", "y"])

SizeT = TypeVar("SizeT", Size, tuple[int, int])
PositionT = TypeVar("PositionT", Position, tuple[int, int])
