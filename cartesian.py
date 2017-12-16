""" Cartesian - a simple representation of a cartesian plane """


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
