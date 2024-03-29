import math
from Binary_Tree_Python.Node import Node


class BST():
    def insert(self, node, val):
        if node is None:
            return Node(val)

        if val < node.value:
            node.left = self.insert(node.left, val)
        elif val > node.value:
            node.right = self.insert(node.right, val)
        return node

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return
        print(node.value, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def search(self, node, val):
        if node is None:
            return None
        if node.value == val:
            return node
        left_found = self.search(node.left, val)
        if left_found is not None:
            return left_found
        else:
            return self.search(node.right, val)

    def getParentNode(self, node, val):
        if node.value == val:
            return node
        newnode = None
        while node.value != val:
            newnode = node
            if node.value < val:
                node = node.right
            elif node.value > val:
                node = node.left
            if node is None:
                return None

        return newnode

    def findSibling(self, node, val):
        if node is None:
            return None
        parent = self.getParentNode(node, val)
        if parent.left is not None and parent.left.value == val:
            return parent.right
        elif parent.right is not None and parent.right.value == val:
            return parent.left

        return None

    def inorder_parent(self, node, val):
        if node is None:
            return None
        newnode = None

        while node is not None:
            if node.value < val:
                newnode = None
                node = node.right
            elif node.value > val:
                newnode = node
                node = node.left
            else:
                return newnode
        return newnode

    def inorder_successor(self, start_node, val):
        if start_node is None:
            return None
        ans_node = self.search(start_node, val)
        if ans_node is not None:
            right = ans_node.right
            find_left = right
            while find_left is not None:
                right = find_left
                find_left = find_left.left
            return right
        return None

    def diff_of_even_odd_levels(self, node):
        if node is None:
            return 0
        return node.value - self.diff_of_even_odd_levels(node.left) - self.diff_of_even_odd_levels(node.right)

    def get_max(self, node):
        if node is None:
            return 0
        return max(node.value, self.get_max(node.right))

    def get_min(self, node):
        if node is None:
            return math.inf
        return min(node.value, self.get_min(node.left))

    def deleteValue(self, node, val):
        if not node:
            return None
        if node.value == val:
            if not node.left and not node.right:
                return None
            elif node.left and not node.right:
                return node.left
            elif node.right and not node.left:
                return node.right
            else:
                return self.inorder_successor(node, val)
        elif node.value > val:
            node.left = self.deleteValue(node.left, val)
        else:
            node.right = self.deleteValue(node.right, val)
        return node


if __name__ == '__main__':
    data = [8, 3, 6, 10, 4, 7, 1, 14, 13]
    tree = BST()
    root = tree.insert(None, data[0])
    for i in range(1, len(data)):
        tree.insert(root, data[i])

    tree.inorder(root)
    print()
    print(tree.search(root, 1))
    parent = tree.inorder_parent(root, 4)
    if parent is not None:
        print(parent.value)
    else:
        print("Parent not found")

    sibling = tree.inorder_successor(root, 14)
    if sibling is not None:
        print(sibling.value)
    else:
        print("No Sibling")

    print(tree.get_min(root))

