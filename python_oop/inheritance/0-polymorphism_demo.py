#!/usr/bin/env python3
"""Demonstrates inheritance and polymorphism."""


class Animal:
    """Parent class for animals."""

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Dog class."""

    def speak(self):
        """Return the dog's sound."""
        return "Woof"


class Cat(Animal):
    """Cat class."""

    def speak(self):
        """Return the cat's sound."""
        return "Meow"


dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
