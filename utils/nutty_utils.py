class point2d:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        if self.y < other.y:
            return self.y < other.y
        return self.x < other.x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if self.y > other.y:
            return self.y > other.y
        return self.x > other.x

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

class point3d:
    def __init__(self, x=0, y=0, z=0):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __lt__(self, other):
        if self.z < other.z:
            return self.z < other.z
        if self.y < other.y:
            return self.y < other.y
        return self.x < other.x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __gt__(self, other):
        if self.z > other.z:
            return self.z > other.z
        if self.y > other.y:
            return self.y > other.y
        return self.x > other.x

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)
