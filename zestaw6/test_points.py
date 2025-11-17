import unittest
from points import Point

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(2, 3)
        self.p2 = Point(4, 1)

    # test __str__ i __repr__
    def test_print(self):
        self.assertEqual(str(self.p1), "(2, 3)")
        self.assertEqual(str(self.p2), "(4, 1)")

        self.assertEqual(repr(self.p1), "Point(2, 3)")
        self.assertEqual(repr(self.p2), "Point(4, 1)")

    # test == i !=
    def test_cmp(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(1, 2) == Point(2, 1))
        self.assertTrue(Point(1, 2) != Point(2, 1))
        self.assertFalse(Point(1, 2) != Point(1, 2))

    # test dodawania
    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(6, 4))
        self.assertEqual(Point(0, 0) + Point(5, 7), Point(5, 7))

    # test odejmowania
    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(-2, 2))
        self.assertEqual(Point(5, 5) - Point(2, 3), Point(3, 2))

    # test iloczynu skalarnego
    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 2*4 + 3*1)  # 8 + 3 = 11
        self.assertEqual(Point(1, 1) * Point(1, 1), 2)

    # test cross
    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), 2*1 - 3*4)  # 2 - 12 = -10
        self.assertEqual(Point(1, 0).cross(Point(0, 1)), 1)

    # test length
    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertAlmostEqual(Point(1, 1).length(), 2**0.5)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()