#!/usr/bin/env python3
"""Defines a Square class with printing."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square."""
        self.size = size

    @property
    def size(self):
        """Return the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size after validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                print("#" * self.__size)
