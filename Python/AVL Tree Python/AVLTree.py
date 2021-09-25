from Binary_Tree_Python.Node import AVLNode


class AVLTREE:
    def __init__(self):
        self.total_nodes = 0

    def right_rotate(self, node):
        if node is None:
            return None
        p = node.parent
        temp = node.left
        if temp is not None:
            node.left = temp.right
            temp.right.parent = node
            temp.right = node
            temp.parent = node.parent
            node.parent = temp
            if p is not None:
                if p.left.value == node.value:
                    p.left = temp
                else:
                    p.right = temp
        return temp

    def left_rotate(self, node):
        if node is None:
            return None

        p = node.parent
        if node.right is not None:
            b = node.right
            c = node.right.left
            node.right = c
            c.parent = node
            b.left = node
            b.parent = p
            if p is not None:
                if p.left.value == node.value:
                    p.left = b
                else:
                    p.right = b
            return b
        return node

    def LLImbalance(self, node):
        if node is None:
            return None
        return self.right_rotate(node)

    def RRImbalance(self, node):
        if node is None:
            return None
        return self.left_rotate(node)

    def LRImbalance(self, node):
        if node is None:
            return
        self.left_rotate(node.left)
        return self.right_rotate(node)

    def RLImbalance(self, node):
        if node is None:
            return
        self.right_rotate(node.right)
        return self.left_rotate(node)

    def insertion(self, node, data):
        if data is None:
            return False
        if node is None:
            return AVLNode(data)


