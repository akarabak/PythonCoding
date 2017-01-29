from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        return new_root

    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        return new_root

    def __str__(self):
        return str(self.value)


class Tree:
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

    def height(self):
        """Height of tree by counting nodes, not edges"""
        return Tree._height(self.root)

    def level_order_iterative(self):
        """Print all the nodes in level order iteratively. O(n) runtime"""
        queue = deque()
        queue.append(self.root)
        depth = 0
        while len(queue) > 0:
            count_current_level = len(queue)
            print('depth {}: '.format(depth), end="")
            while count_current_level > 0:
                count_current_level -= 1
                node = queue.popleft()
                print(node, "", end="")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()
            depth += 1

    def max_brunch_sum(self):
        self.__brunch_sum(self.root)
        return self.sum

    def __brunch_sum(self, root):
        if not root:
            return 0
        else:
            left = self.__brunch_sum(root.left)
            right = self.__brunch_sum(root.right)
            if left + right + 1 > self.sum:
                self.sum = left + right + 1
            return max(left, right) + 1

    @staticmethod
    def __insert_into(node, value):
        if not node:
            node = Node(value)
        else:
            if node.value > value:
                node.left = Tree.__insert_into(node.left, value)
            elif node.value < value:
                node.right = Tree.__insert_into(node.right, value)

        return node

    @staticmethod
    def _height(root):
        if not root:
            return 0
        else:
            left = Tree._height(root.left)
            right = Tree._height(root.right)
            return max(left, right) + 1

    def level_order(self):
        """Prints all the nodes in level order recursively. O(logn)^2 runtime"""
        height = Tree._height(self.root)
        for i in range(height): # O(logn)
            print("depth {}: ".format(i), end="")
            Tree.__print_at_depth(self.root, i) # 2O(logn)
            print()

    @staticmethod
    def __print_at_depth(node: Node, depth: int):
        """Prints values of tree at given depth
        Subtracts 1 from depth at each recursion, prints when reaches 0 (meaning reached the required depth)"""
        if not node:
            return
        if depth == 0:
            print(node, "", end="")
            return
        Tree.__print_at_depth(node.left, depth - 1) #O(logn - 1)
        Tree.__print_at_depth(node.right, depth - 1) #O(logn - 1)