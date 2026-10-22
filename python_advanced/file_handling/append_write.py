#!/usr/bin/env python3
"""Append text to a file."""


def append_write(filename="", text=""):
    """Append text and return the number of characters added."""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
