class Vertex:
    name: str
    neighbours: list
    discovery: bool
    finish: int
    color: int

    def add_neighbour(self, v):
        if v is None or v < 0:
            return None
        self.neighbours.append(v)
