class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class LinkedNode:
    def __init__(self, data):
        self.value = data
        self.prev = None
        self.next = None


class AVLNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.parent = None
        self.bf = 0
