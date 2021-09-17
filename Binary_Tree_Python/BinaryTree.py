from Node import Node
from queue import LifoQueue, Queue


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

    def print_all_level_at_n(self, node):
        if node is None:
            return

        q = [node]
        while q.__len__() > 0:
            dnode = q.pop(0)
            print(dnode.value, end=" ")
            if dnode.left is not None:
                q.append(dnode.left)

            if dnode.right is not None:
                q.append(dnode.right)

    def print_reverse_level(self, node):
        if node is None:
            return

        h = self.height(node)
        for i in range(h, -1, -1):
            self.print_same_level(node, i)
            print()

    def print_reverse_level_Stack(self, node):
        if node is None:
            return
        q = Queue(maxsize=0)
        stack = LifoQueue(maxsize=0)

        q.put(node)
        while not q.empty():
            el = q.get()

            stack.put(el)
            if el.right is not None:
                q.put(el.right)
            if el.left is not None:
                q.put(el.left)

        while not stack.empty():
            print(stack.get().value, end=" ")

    def print_all_levels_newline(self, node):
        if node is None:
            return
        q = Queue(maxsize=0)
        s = LifoQueue(maxsize=0)
        c = self.height(node) + 1
        q.put(node)

        while True:
            count = q.qsize()
            if count == 0:
                break

            while count > 0:
                el = q.get()
                print(el.value, end=" ")
                if el.left is not None:
                    q.put(el.left)
                if el.right is not None:
                    q.put(el.right)

                count = count - 1

            print()

    maxlevel = 0

    def print_left_view(self, node, level):
        if node is None:
            return

        if level >= self.maxlevel:
            print(node.value, end=" ")
            self.maxlevel = self.maxlevel + 1

        self.print_left_view(node.left, level + 1)
        self.print_left_view(node.right, level + 1)

    def print_right_view(self, node, level):
        if node is None:
            return

        if level >= self.maxlevel:
            print(node.value, end=" ")
            self.maxlevel = self.maxlevel + 1

        self.print_right_view(node.right, level + 1)
        self.print_right_view(node.left, level + 1)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(6)
    tree.root.right = Node(7)
    tree.root.left.left = Node(13)
    tree.root.left.right = Node(10)
    tree.root.right.left = Node(8)
    tree.root.right.right = Node(14)
    # print(tree.sum_of_nodes(tree.root))
    # print(tree.num_leaf_nodes(tree.root))
    # print(tree.height(tree.root))
    # print((tree.print_same_level(tree.root, 2)))
    # tree.print_all_level(tree.root)
    # tree.print_all_level_at_n(tree.root)
    # tree.print_reverse_level(tree.root)
    # tree.print_reverse_level_Stack(tree.root)
    # tree.print_all_levels_newline(tree.root)
    # tree.print_left_view(tree.root, 0)
    # tree.print_right_view(tree.root, 0)
    # tree.postorder(tree.root)
    tree.preorder(tree.root)
