class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, right):
        return self.x == right.x and self.y == right.y

    def __lt__(self, right):
        return self.x < right.x and self.y < right.x

    def combine(self, right):
        self.x = min(self.x, right.x)
        self.y = max(self.y, right.y)

    def __len__(self):
        return self.y - self.x + 1

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.x + self.y)

    def intersect(self, right):
        self.x = min(self.x, right.x)
        self.y = max(self.y, right.y)


