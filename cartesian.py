""" Cartesian - a simple representation of a cartesian plane """


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

    def quadrant(self):
        """ Determines the quadrant that the point is located in """
        if self.x == 0 or self.y == 0:
            return None
        elif self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return None

    def distance(self, point=None):
        """ Determines the distance between this point and another point """
        if not point:
            x = sqrt(pow((0 - self.x), 2) + pow((0 - self.y), 2))
        else:
            x = sqrt(pow((point.x - self.x), 2) + pow((point.y - self.y), 2))

        if x is None:
            return 0
        elif x < 0:
            return x * -1
        else:
            return x
