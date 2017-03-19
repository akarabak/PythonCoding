import ranges
import unittest

class PointTest(unittest.TestCase):
    def setUp(self):
        self.first = ranges.Point(1,2)
        self.second = ranges.Point(1,2)
        self.third = ranges.Point(1,3)
        self.fourth = ranges.Point(2,3)
        self.fifth = ranges.Point(3,4)

    def test_equal(self):
        self.assertEqual(self.first, self.second)
        self.assertNotEqual(self.first, self.third)
        self.assertNotEqual(self.first, self.third)
        self.assertNotEqual(self.first, self.fourth)

    def test_lt(self):
        self.assertLess(self.first, self.fifth)

    def test_gt(self):
        self.assertGreater(self.fifth, self.first)

    def test_intersect(self):
        # Failure for greater and less, means intersects
        self.assertNotEqual(self.first, self.third)
        if self.first != self.third and not (self.first < self.third and self.first > self.third):
            self.first.combine(self.third)
        self.assertEqual(self.first, ranges.Point(1,3))


if __name__ == '__main__':
    unittest.main()