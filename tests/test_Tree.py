import unittest
import sys
from io import StringIO

import Tree


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Tree.Node(1)
        self.node.left = Tree.Node(2)

    def test_print(self):
        self.assertEqual(str(self.node), '1')


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

    def test_ancestor(self):
        self.assertEqual(self.tree.common_ancestor(4, 8), 6)
        self.assertEqual(self.tree.common_ancestor(8, 11), 10)
        emptyTree = Tree.Tree()
        self.assertEqual(emptyTree.common_ancestor(8, 11), None)

    def test_level_order(self):
        stdout = sys.stdout
        out = StringIO()
        sys.stdout = out
        self.tree.level_order()
        sys.stdout = stdout
        answer = 'depth 0: 1 \n' +\
                         'depth 1: 6 \n' +\
                         'depth 2: 5 10 \n' +\
                         'depth 3: 3 8 11 \n' +\
                         'depth 4: 2 4 7 9 \n'
        self.assertEqual(out.getvalue(), answer)

    def test_level_order_iterative(self):
        stdout = sys.stdout
        out = StringIO()
        sys.stdout = out
        self.tree.level_order_iterative()
        sys.stdout = stdout
        answer = 'depth 0: 1 \n' +\
                         'depth 1: 6 \n' +\
                         'depth 2: 5 10 \n' +\
                         'depth 3: 3 8 11 \n' +\
                         'depth 4: 2 4 7 9 \n'
        self.assertEqual(out.getvalue(), answer)

if __name__ == '__main__':
    unittest.main()