import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, *args):
        self.head = None
        self.size = 0
        if len(args) == 1:
            self.size += 1
            self.head = Node(args[0])

    def __iter__(self):
        start = self.head
        while start:
            yield start.value
            start = start.next

    def __eq__(self, right):
        for i, j in self, right:
            if i != j:
                return False
        return True

    def add(self, value):
        start = self.head
        self.size += 1
        if start is None:
            start = Node(value)
        else:
            new = Node(value)
            new.next = self.head
            self.head = new

    def __getitem__(self, index):
        if index >= self.size:
            raise ValueError('Index({}) out of range'.format(index))
        i = 0
        start = self.head
        while i < index:
            i += 1
            start = start.next
        return start.value

    def __len__(self):
        return self.size

    def remove(self, index):
        if index >= self.size:
            raise ValueError('Index({}) out of range'.format(index))
        self.size -= 1
        start = self.head
        i = 0
        if index == 0:
            self.head = start.next
        else:
            while i + 1 != index:
                i += 1
                start = start.next
            start.next = start.next.next


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList(8)
        self.ll.add(10)

    def test_add(self):
        self.ll.add(5)
        compare = [5, 10, 8]
        for i in range(3):
            self.assertEqual(self.ll[i], compare[i])

    def test_remove(self):
        self.ll.remove(1)
        self.ll.add(1)
        compare = [1, 10]
        for i in range(len(self.ll)):
            self.assertEqual(self.ll[i], compare[i])


if __name__ == '__main__':
    unittest.main()
