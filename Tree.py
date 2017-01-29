
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

    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self):
        self.root = None
        self.sum = 0

    def balance(self, node: Node):
        if node is None:
            return
        self.balance(node.left)
        self.balance(node.right)
        factor = self.__height(node.left) - self.__height(node.right)
        if factor > 2:
            node.rotate_right()
        elif factor < 2:
            node.rotate_left()

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
            root = Node(value)
        else:
            if root.value > value:
                root.left = Tree.__insert_into(root.left, value)
            elif root.value < value:
                root.right = Tree.__insert_into(root.right, value)
        return root

    def height(self):
        return Tree.__height(self.root)

    @staticmethod
    def __height(root):
        if not root:
            return 0
        else:
            left = Tree.__height(root.left)
            right = Tree.__height(root.right)
            return max(left, right) + 1

    def level_order(self):
        """Prints all the nodes in level order"""
        height = Tree.__height(self.root)
        for i in range(height):
            print("depth {}: ".format(i), end="")
            Tree.print_at_level(self.root, i, 0)
            print()

    @staticmethod
    def print_at_level(node: Node, level: int, current_height: int):
        if not node:
            return
        if current_height == level:
            print(node, "", end="")
            return
        current_height += 1
        Tree.print_at_level(node.left, level, current_height)
        Tree.print_at_level(node.right, level, current_height)

    def max_brunch_sum(self):
        self.__brunch_sum(self.root)
        return self.sum

    def __brunch_sum(self, root):
        if root is None:
            return 0
        else:
            left = self.__height(root.left)
            right = self.__height(root.right)
            if left + right + 1 > self.sum:
                self.sum = left + right + 1
            return max(left, right) + 1