#!/usr/bin/env python3
"""Defines the Square class."""

SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Represent a square."""

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height)
