import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, *args):
        self.head = None
        if len(args) == 1:
            self.head = None(args[0])

    def push(self, value):
        n = Node(value)
        n.next = self.head
        self.head = n

    def pop(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            raise ValueError


class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_pop_and_push(self):
        with self.assertRaises(ValueError):
            self.s.pop()
        self.s.push(5)
        self.s.push(7)
        self.assertEqual(self.s.pop(), 7)
        self.assertEqual(self.s.pop(), 5)


if __name__ == '__main__':
    unittest.main()