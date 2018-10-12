class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, *args):
        self.head = None
        self.size = 0
        if len(args) == 1:
            self.size += 1
            self.head = Node(args[0])

    def __iter__(self):
        start = self.head
        while start:
            yield start.value
            start = start.next

    def __eq__(self, right):
        for i, j in zip(self, right):
            if i != j:
                return False
        return True

    def get_middle(self):
        start = self.head
        slow = self.head
        counter = 0
        while start:
            start = start.next
            if counter == 2:
                counter = 0
                slow = slow.next
            counter += 1

        return slow.value

    def add(self, value):
        start = self.head
        self.size += 1
        if start is None:
            start = Node(value)
        else:
            new = Node(value)
            new.next = self.head
            self.head = new

    def __getitem__(self, index):
        if index >= self.size:
            raise ValueError('Index({}) out of range'.format(index))
        i = 0
        start = self.head
        while i < index:
            i += 1
            start = start.next
        return start.value

    def __len__(self):
        return self.size

    def __str__(self):
        result = ''
        for i in self:
            result += str(i) + ' '
        return result

    def remove(self, index):
        if index >= self.size:
            raise ValueError('Index({}) out of range'.format(index))
        self.size -= 1
        start = self.head
        i = 0
        if index == 0:
            self.head = start.next
        else:
            while i + 1 != index:
                i += 1
                start = start.next
            start.next = start.next.next

    def reverse(self):
        stack = []
        start = self.head
        while start:
            stack.append(start)
            start = start.next

        current = None
        for i, e in enumerate(reversed(stack)):
            if i == 0:
                self.head = e
                current = self.head
            else:
                current.next = e
                current = current.next
        current.next = None
