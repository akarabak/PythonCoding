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

    def test_middle_odd(self):
        self.ll.add(2)
        self.ll.add(3)
        self.ll.add(5)
        self.assertEqual(2, self.ll.get_middle())

    def test_middle_even(self):
        self.ll.add(2)
        self.ll.add(3)
        self.ll.add(5)
        self.ll.add(10)
        self.assertEqual(3, self.ll.get_middle())

    def test_middle_short(self):
        self.assertEqual(10, self.ll.get_middle())

    def test_middle_3(self):
        self.ll.add(2)
        self.assertEqual(10, self.ll.get_middle())

    def test_reverse(self):
        self.ll.add(9)
        self.ll.add(12)
        self.ll.reverse()
        nums = [8, 10, 9, 12]
        for i, j in zip(nums, self.ll):
            self.assertEqual(i, j)


if __name__ == '__main__':
    unittest.main()
