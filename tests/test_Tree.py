import unittest
from tests.test_utils import captured_output
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
        self.assertEqual(self.tree.max_brunch_sum(), 7)

    def test_ancestor(self):
        self.assertEqual(self.tree.common_ancestor(4, 8), 6)
        self.assertEqual(self.tree.common_ancestor(8, 11), 10)
        emptyTree = Tree.Tree()
        self.assertEqual(emptyTree.common_ancestor(8, 11), None)

    def test_level_order(self):
        with captured_output() as out:
            self.tree.level_order()
        answer = 'depth 0: 1 \n' +\
                         'depth 1: 6 \n' +\
                         'depth 2: 5 10 \n' +\
                         'depth 3: 3 8 11 \n' +\
                         'depth 4: 2 4 7 9 \n'
        self.assertEqual(out.getvalue(), answer)

    def test_level_order_iterative(self):
        answer = 'depth 0: 1 \n' + \
                 'depth 1: 6 \n' + \
                 'depth 2: 5 10 \n' + \
                 'depth 3: 3 8 11 \n' + \
                 'depth 4: 2 4 7 9 \n'
        with captured_output() as out:
            self.tree.level_order_iterative()
        self.assertEqual(answer, out.getvalue())

    def test_inorder(self):
        with captured_output() as out:
            self.tree.print_inorder()
        self.assertEqual("1 2 3 4 5 6 7 8 9 10 11 ", out.getvalue())

    def test_inorder_iterative(self):
        with captured_output() as out:
            self.tree.print_inorder_iterative()
        self.assertEqual("1 2 3 4 5 6 7 8 9 10 11 ", out.getvalue())

    def test_postorder(self):
        with captured_output() as out:
            self.tree.print_postorder()
        self.assertEqual("2 4 3 5 7 9 8 11 10 6 1 ", out.getvalue())

    def test_postorder_iterative(self):
        with captured_output() as out:
            self.tree.print_postorder_iterative()
        self.assertEqual("2 4 3 5 7 9 8 11 10 6 1 ", out.getvalue())


if __name__ == '__main__':
    unittest.main()
