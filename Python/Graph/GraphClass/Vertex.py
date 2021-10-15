class Vertex:
    name: str or int
    visited: bool
    weight: int

    def __init__(self, name, weight=1):
        self.name = name
        self.visited = False
        self.weight = weight

    def set_visited(self):
        self.visited = True

    def set_weight(self, weight):
        self.weight = weight

