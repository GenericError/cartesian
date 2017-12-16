""" Tests for the cartesian module """

import unittest
import cartesian


class TestPointClass(unittest.TestCase):
    """ Tests for the Point class """

    def test_create_point(self):
        """ Ensures that a point can be created """
        point = cartesian.Point()
        self.assertNotEqual(point, False)

    def test_create_point_with_coords(self):
        """ Tests that the coordinates are correctly
        assigned upon creating a point """
        point = cartesian.Point(-1, 2)
        self.assertEqual(point.x, -1)
        self.assertEqual(point.y, 2)

    def test_create_point_default_coords(self):
        """ Ensures that the default coordinates are (0, 0) """
        point = cartesian.Point()
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)

    def test_point_repr(self):
        """ Ensures that repr() returns the correct result """
        point = cartesian.Point(-1, 2)
        self.assertEqual(point.__repr__(), "Point(-1, 2)")
        self.assertEqual(repr(point), "Point(-1, 2)")

    def test_point_str(self):
        """ Ensures that str() returns the correct result """
        point = cartesian.Point(-1, 2)
        self.assertEqual(point.__str__(), "Point at x=-1 and y=2")
        self.assertEqual(str(point), "Point at x=-1 and y=2")


if __name__ == '__main__':
    unittest.main()
