import unittest

from tests.test_Tree import TestTree, captured_output, TestNode
import BalancedTree as Tree


class TestBalancedTree(TestTree):
    """"Runs test of base class. Overrides some tests due to tree balancing"""
    def setUp(self):
        self.tree = Tree.BalancedTree()
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
        self.assertEqual(self.tree.height(), 4)

    def test_max_brunch_sum(self):
        self.assertEqual(self.tree.max_brunch_sum(), 7)

    def test_ancestor(self):
        self.assertEqual(self.tree.common_ancestor(4, 8), 6)
        self.assertEqual(self.tree.common_ancestor(8, 11), 8)
        emptyTree = Tree.Tree()
        self.assertEqual(emptyTree.common_ancestor(8, 11), None)

    def test_level_order(self):
        answer = 'depth 0: 6 \n' +\
                         'depth 1: 3 8 \n' +\
                         'depth 2: 2 5 7 10 \n' +\
                         'depth 3: 1 4 9 11 \n'

        with captured_output() as out:
            self.tree.level_order()
        self.assertEqual(out.getvalue(), answer)

    def test_level_order_iterative(self):
        answer = 'depth 0: 6 \n' +\
                         'depth 1: 3 8 \n' +\
                         'depth 2: 2 5 7 10 \n' +\
                         'depth 3: 1 4 9 11 \n'
        with captured_output() as out:
            self.tree.level_order_iterative()
        self.assertEqual(out.getvalue(), answer)

if __name__ == '__main__':
    unittest.main()