""" Cartesian - a simple representation of a cartesian plane """

class Point(object):
    """ A basic point """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __str__(self):
        return "Point at x=" + str(self.x) + " and y=" + str(self.y)
