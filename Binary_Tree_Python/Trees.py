from Node import Node
from BinaryTreeContinued import BinaryTreeContinued


def getTwoTree():
    tree1 = BinaryTreeContinued()
    tree1.root = Node(5)
    tree1.root.left = Node(6)
    tree1.root.right = Node(7)
    tree1.root.left.left = Node(13)
    tree1.root.left.right = Node(10)
    tree1.root.right.left = Node(8)
    tree1.root.right.right = Node(14)

    tree2 = BinaryTreeContinued()
    tree2.root = Node(5)
    tree2.root.left = Node(6)
    tree2.root.right = Node(7)
    tree2.root.left.left = Node(13)
    tree2.root.left.right = Node(10)
    tree2.root.right.left = Node(8)
    tree2.root.right.right = Node(14)

    return tree1, tree2

