import LinkedList
import unittest


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList.LinkedList(8)
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