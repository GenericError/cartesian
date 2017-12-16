import unittest
import cartesian

class TestPointClass(unittest.TestCase):

    def test_create_point(self):
        point = cartesian.Point()

    def test_create_point_with_coords(self):
        point = cartesian.Point(-1, 2)
        self.assertEqual(point.x, -1)
        self.assertEqual(point.y, 2)

    def test_create_point_default_coordinates(self):
        point = cartesian.Point()
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)

    def test_point_repr(self):
        point = cartesian.Point(-1, 2)
        self.assertEqual(point.__repr__(), "Point(-1, 2)")
        self.assertEqual(repr(point), "Point(-1, 2)")

if __name__ == '__main__':
    unittest.main()
