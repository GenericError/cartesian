""" Cartesian - a simple representation of a cartesian plane """

from collections import namedtuple

point_tuple = namedtuple("origin", ['x', 'y'])
origin = point_tuple(0, 0)


def sqrt(number):
    """ Returns the square root of x without using the math module """
    return pow(number, 0.5)


class Point(object):
    """ A basic point """
    def __init__(self, x=0, y=0):
        """ Sets up the point """
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __str__(self):
        return "Point at x=" + str(self.x) + " and y=" + str(self.y)

    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return True
        return False

    def quadrant(self):
        """ Determines the quadrant that the point is located in """
        if self.x > 0:
            if self.y > 0:
                return 1
            elif self.y < 0:
                return 4
        elif self.x < 0:
            if self.y > 0:
                return 2
            elif self.y < 0:
                return 3

    def distance(self, point=origin):
        """ Determines the distance between this point and another point """
        return sqrt(pow((point.x - self.x), 2) + pow((point.y - self.y), 2))
