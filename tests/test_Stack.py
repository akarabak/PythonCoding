import Stack
import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack.Stack()

    def test_pop_and_push(self):
        with self.assertRaises(ValueError):
            self.s.pop()
        self.s.push(5)
        self.s.push(7)
        self.assertEqual(self.s.pop(), 7)
        self.assertEqual(self.s.pop(), 5)


if __name__ == '__main__':
    unittest.main()