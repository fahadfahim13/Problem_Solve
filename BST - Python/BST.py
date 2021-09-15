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

    def search(self, node, val):
        if node is None:
            return False
        if node.value == val:
            return True
        return self.search(node.left, val) or self.search(node.right, val)

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



if __name__ == '__main__':
    data = [8, 3, 6, 10, 4, 7, 1, 14, 13]
    tree = BST()
    root = tree.insert(None, data[0])
    for i in range(1, len(data)):
        tree.insert(root, data[i])

    tree.inorder(root)
    print()
    print(tree.search(root, 1))
    parent = tree.getParentNode(root, 14)
    if parent is not None:
        print(parent.value)
    else:
        print("Node not found")

    sibling = tree.findSibling(root, 6)
    if sibling is not None:
        print(sibling.value)
    else:
        print("No Sibling")

