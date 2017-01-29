from Tree import Tree, Node


class BalancedTree(Tree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        self.root = BalancedTree.__insert_into(self.root, value)

    @staticmethod
    def __insert_into(node, value):
        # returns with no changes if already there
        if not node:
            node = Node(value)
        else:
            if node.value > value:
                node.left = BalancedTree.__insert_into(node.left, value)
                node = BalancedTree.__balance(node)
            elif node.value < value:
                node.right = BalancedTree.__insert_into(node.right, value)
                node = BalancedTree.__balance(node)

        return node

    @staticmethod
    def __balance(node: Node):
        """Balances the node"""
        while True:
            factor = BalancedTree.__balance_factor(node)
            if factor >= 2:
                b_factor = BalancedTree.__balance_factor(node.left)
                if b_factor <= -1:
                    node.left = node.left.rotate_left()
                node = node.rotate_right()
            elif factor <= -2:
                b_factor = BalancedTree.__balance_factor(node.right)
                if b_factor >= 1:
                    node.right = node.right.rotate_right()
                node = node.rotate_left()
            else:
                break

        return node

    @staticmethod
    def __balance_factor(node):
        """Calculates balance factor of the node"""
        if not node.left and not node.right:
            return 0
        elif not node.left:
            return 0 - Tree._height(node.right)
        elif not node.right:
            return Tree._height(node.left)
        else:
            return Tree._height(node.left) - Tree._height(node.right)