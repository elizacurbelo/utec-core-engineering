#!/usr/bin/env python3
"""Defines a Square class with string representation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the square position."""
        if (type(value) is not tuple or len(value) != 2
                or any(type(n) is not int or n < 0 for n in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Return the square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using #."""
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the square as a string."""
        if self.__size == 0:
            return ""
        spaces = " " * self.__position[0]
        lines = [spaces + "#" * self.__size
                 for row in range(self.__size)]
        return "\n" * self.__position[1] + "\n".join(lines)
