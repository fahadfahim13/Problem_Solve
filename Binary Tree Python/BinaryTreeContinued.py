from Node import Node
from BinaryTree import BinaryTree
from queue import LifoQueue


class BinaryTreeContinued(BinaryTree):
    def __init__(self):
        super()

    @staticmethod
    def inorder_loop(node):
        if node is None:
            return
        st = LifoQueue(maxsize=0)
        while node is not None:
            st.put(node)
            node = node.left

        while st.qsize() > 0:
            newnode = st.get()
            print(newnode.value, end=" ")
            if newnode.right is not None:
                newnode = newnode.right
                while newnode is not None:
                    st.put(newnode)
                    newnode = newnode.left


if __name__ == '__main__':
    tree = BinaryTreeContinued()
    tree.root = Node(5)
    tree.root.left = Node(6)
    tree.root.right = Node(7)
    tree.root.left.left = Node(13)
    tree.root.left.right = Node(10)
    tree.root.right.left = Node(8)
    tree.root.right.right = Node(14)

    tree.inorder_loop(tree.root)