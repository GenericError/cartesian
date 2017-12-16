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
        """ Ensures providied coordinates are correctly assigned """
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

    def test_point_quadrant_none(self):
        """ Ensures that a point lying on an axis has no quadrant """
        points = [
            cartesian.Point(1, 0),
            cartesian.Point(0, 1),
            cartesian.Point(-1, 0),
            cartesian.Point(0, -1),
            cartesian.Point(0, 0)
        ]

        for point in points:
            self.assertEqual(point.quadrant(), None)

    def test_point_quadrant_first(self):
        """ Ensures that the first quadrant is correctly identified """
        self.assertEqual(cartesian.Point(1, 1).quadrant(), 1)

    def test_point_quadrant_second(self):
        """ Ensures that the second quadrant is correctly identified """
        self.assertEqual(cartesian.Point(-1, 1).quadrant(), 2)

    def test_point_quadrant_third(self):
        """ Ensures that the third quadrant is correctly identified """
        self.assertEqual(cartesian.Point(-1, -1).quadrant(), 3)

    def test_point_quadrant_fourth(self):
        """ Ensures that the fourth quadrant is correctly identified """
        self.assertEqual(cartesian.Point(1, -1).quadrant(), 4)

    def test_point_distance(self):
        """ Ensures the distance is correctly calculated """
        self.assertEqual(
            cartesian.Point(3, 4).distance(cartesian.Point(0, 0)), 5
        )
        self.assertEqual(
            cartesian.Point(1, 2).distance(cartesian.Point(4, 3)), pow(10, 0.5)
        )

    def test_point_negative(self):
        """ Ensures the distance is correctly calculated with negatives """
        self.assertEqual(
            cartesian.Point(-1, 2).distance(cartesian.Point(4, 3)),
            pow(26, 0.5)
        )
        self.assertEqual(
            cartesian.Point(1, -2).distance(cartesian.Point(4, 3)),
            pow(34, 0.5)
        )
        self.assertEqual(
            cartesian.Point(-1, -2).distance(cartesian.Point(4, 3)),
            pow(50, 0.5)
        )

    def test_point_default(self):
        """ Ensures the distance is correctly calculated between the origin """
        # Real distance is 1.41... (the square root of 2)
        self.assertEqual(
            cartesian.Point(1, 1).distance(), pow(2, 0.5)
        )
        self.assertEqual(
            cartesian.Point(-1, 1).distance(), pow(2, 0.5)
        )
        self.assertEqual(
            cartesian.Point(1, -1).distance(), pow(2, 0.5)
        )
        self.assertEqual(
            cartesian.Point(-1, -1).distance(), pow(2, 0.5)
        )

    def test_point_distance_none(self):
        """ Ensures that a lack of distance returns zero """
        self.assertEqual(
            cartesian.Point(1, 1).distance(cartesian.Point(1, 1)), 0
        )
        self.assertEqual(
            cartesian.Point(-1, 1).distance(cartesian.Point(-1, 1)), 0
        )
        self.assertEqual(
            cartesian.Point(1, -1).distance(cartesian.Point(1, -1)), 0
        )
        self.assertEqual(
            cartesian.Point(-1, -1).distance(cartesian.Point(-1, -1)), 0
        )


if __name__ == '__main__':
    unittest.main()
