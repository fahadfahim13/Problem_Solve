from Node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

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

    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end=" ")

    def sum_of_nodes(self, node):
        if node is None:
            return 0

        return node.value + self.sum_of_nodes(node.left) + self.sum_of_nodes(node.right)

    def num_leaf_nodes(self, node):
        if node is None:
            return 0
        if (node.right is None) and (node.left is None):
            return 1
        return self.num_leaf_nodes(node.left) + self.num_leaf_nodes(node.right)

    def height(self, node):
        if node is None:
            return -1

        return max(self.height(node.left), self.height(node.right)) + 1

    def print_same_level(self, node, h):
        if node is None:
            return

        if h == 0:
            if node.value is not None:
                print(node.value, end=" ")
            return

        self.print_same_level(node.left, h - 1)
        self.print_same_level(node.right, h - 1)

    def print_all_level(self, node):
        if node is None:
            return

        height = self.height(node)
        for i in range(0, height + 1):
            self.print_same_level(node, i)
            print()


if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(6)
    tree.root.right = Node(7)
    tree.root.left.left = Node(13)
    tree.root.left.right = Node(10)
    tree.root.right.left = Node(8)
    tree.root.right.right = Node(14)
    print(tree.sum_of_nodes(tree.root))
    print(tree.num_leaf_nodes(tree.root))
    print(tree.height(tree.root))
    print((tree.print_same_level(tree.root, 2)))
    print(tree.print_all_level(tree.root))
