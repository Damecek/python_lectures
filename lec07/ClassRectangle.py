#!/usr/bin/env python3
"""rectangle class"""

class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def get_area(self):
        return self.w * self.h

    def set_size(self, h , w):
        self.w = w
        self.h = h


r = Rectangle(2, 5)
print(r.get_area())
r.set_size(4, 7)
print(r.get_area())
