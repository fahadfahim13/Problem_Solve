from Node import Node
from BinaryTree import BinaryTree
from queue import LifoQueue
# from Trees import getTwoTree


class BinaryTreeContinued(BinaryTree):
    def __init__(self):
        super().__init__()

    def inorder_loop(self, node):
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

    def preorder_iter(self, node):
        if node is None:
            return
        stack = LifoQueue(maxsize=0)
        stack.put(node)

        while stack.qsize() > 0:
            newnode = stack.get()
            print(newnode.value, end=" ")
            if newnode.right is not None:
                stack.put(newnode.right)
            if newnode.left is not None:
                stack.put(newnode.left)

    def postorder_iter(self, node):
        if node is None:
            return
        stack = LifoQueue(maxsize=0)
        final_stack = LifoQueue(maxsize=0)
        # while node is not None:
        #     stack.put(node)
        #     final_stack.put(node)
        #     node = node.right
        #
        # while stack.qsize() > 0:
        #     newnode = stack.get()
        #     if newnode.left is not None:
        #         newnode = newnode.left
        #         while newnode is not None:
        #             stack.put(newnode)
        #             final_stack.put(newnode)
        #             newnode = newnode.right
        stack.put(node)

        while stack.qsize() > 0:
            newnode = stack.get()
            final_stack.put(newnode)
            if newnode.left is not None:
                stack.put(newnode.left)
            if newnode.right is not None:
                stack.put(newnode.right)

        while final_stack.qsize() > 0:
            newnode = final_stack.get()
            print(newnode.value, end=" ")

    def mirror(self, node):
        if node is None:
            return
        newnode = node.left
        node.left = node.right
        node.right = newnode

        self.mirror(node.left)
        self.mirror(node.right)

    def deleteTree(self, node):
        if node is None:
            return None

        node.left = self.deleteTree(node.left)
        node.right = self.deleteTree(node.right)

        print("Deleting node: " + str(node.value))
        node = None
        return node

    def checkEqualTree(self, tree1_node, tree2_node):
        if tree1_node is None and tree2_node is None:
            return True

        if tree1_node is None or tree2_node is None:
            return False

        return (tree1_node.value == tree2_node.value) and self.checkEqualTree(tree1_node.left, tree2_node.left) and self.checkEqualTree(tree1_node.right, tree2_node.right)




