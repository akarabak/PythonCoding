class Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def rotate_left(self):
            new_root = self.right
            self.right = new_root.left
            new_root.left = self

        def rotate_right(self):
            new_root = self.left
            self.left = new_root.right
            new_root.right = self

    def __init__(self):
        self.root = None
        self.sum = 0

    def insert(self, value):
        self.root = Tree.__insert_into(self.root, value)

    def common_ancestor(self, value1, value2):
        """"Assumes both values are in the tree"""
        start = self.root
        while start:
            if start.value > value1 and start.value > value2:
                start = start.left
            elif start.value < value1 and start.value < value2:
                start = start.right
            else:
                return start.value

        return None


    @staticmethod
    def __insert_into(root, value):
        if root is None:
            root = Tree.Node(value)
        else:
            if root.value > value:
                root.left = Tree.__insert_into(root.left, value)
            elif root.value < value:
                root.right = Tree.__insert_into(root.right, value)
        return root

    def height(self):
        return self.__height(self.root)

    def __height(self, root):
        if root is None:
            return 0
        else:
            left = self.__height(root.left)
            right = self.__height(root.right)
            if left + right + 1 > self.sum:
                self.sum = left + right + 1
            return max(left, right) + 1

    def test_max_brunch_sum(self):
        self.__height(self.root)
        return self.sum
