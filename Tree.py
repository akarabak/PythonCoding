class Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.sum = 0

    def insert(self, value):
        self.root = Tree.__insert_into(self.root, value)

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
