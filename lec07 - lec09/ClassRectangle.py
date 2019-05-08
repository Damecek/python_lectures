#!/usr/bin/env python3
"""rectangle class"""


class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def get_area(self):
        return self.w * self.h

    def set_size(self, h, w):
        self.w = w
        self.h = h

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() == other.get_area()
        return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() < other.get_area()
        return False

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() <= other.get_area()
        return False

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() > other.get_area()
        return False

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() >= other.get_area()
        return False


r = Rectangle(2, 5)
print(r.get_area())
r.set_size(4, 7)
print(r.get_area())
print(r == Rectangle(7, 4))
print(r >= Rectangle(3, 5))
