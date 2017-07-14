import unittest
import Matrix


class TestMatrix(unittest.TestCase):
    def test_rotate(self):
        self.assertEqual(Matrix.rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]),
                                       [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])


if __name__ == '__main__':
    unittest.main()