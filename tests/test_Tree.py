import unittest
import Tree


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree.Tree()
        self.tree.insert(1)
        self.tree.insert(6)
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(10)
        self.tree.insert(8)
        self.tree.insert(7)
        self.tree.insert(9)
        self.tree.insert(11)

    def test_height(self):
        self.assertEqual(self.tree.height(), 5)

    def test_max_brunch_sum(self):
        self.assertEqual(self.tree.test_max_brunch_sum(), 7)