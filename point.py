#!/usr/bin/env python

class Point():
    """ A simple class """

    def __init__(self, x=0, y=0):
        if is_number(x) and is_number(y):
            self.x = x
            self.y = y
        else:
            raise TypeError("Only numbers")

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def norma(self):
        return (self.x**2 + self.y**2)**0.5

    def distance(self, other):
        r = self.__sub__(other)
        return r.norma()

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


def is_number(value):
    return isinstance(value, (int, float, complex))


if __name__ == "__main__":
    p = Point(3,5)
    q = Point(2,9)

    print(p.distance(q))

    print(p)