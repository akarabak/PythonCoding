
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, *args):
        self.head = None
        if len(args) == 1:
            self.head = None(args[0])

    def push(self, value):
        n = Node(value)
        n.next = self.head
        self.head = n

    def pop(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            raise ValueError