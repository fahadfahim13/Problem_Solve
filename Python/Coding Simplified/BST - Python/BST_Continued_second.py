import math
from BST_Continued import BST_Continued
from queue import LifoQueue
from Binary_Tree_Python.Node import Node
from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList


class BSTContinuedSecond(BST_Continued):
    def checkBst(self, node):
        if node is None:
            return False
        stack = LifoQueue(maxsize=0)
        while node is not None:
            stack.put(node)
            newnode = node
            node = node.left

        prevnode = Node(-math.inf)
        while stack.qsize() > 0:
            newnode = stack.get()
            if newnode.value < prevnode.value:
                return False
            prevnode = newnode
            newnode = newnode.right
            while newnode is not None:
                stack.put(newnode)
                newnode = newnode.left

        return True

    def checkBSTRec(self, node):
        if node is None:
            return False
        if node.left is not None and node.right is None:
            if node.value > node.left.value:
                return self.checkBSTRec(node.left)
            else:
                return False
        elif node.left is None and node.right is not None:
            if node.value < node.right.value:
                return self.checkBSTRec(node.right)
            else:
                return False
        elif node.left is not None and node.right is not None:
            if node.right.value > node.value > node.left.value:
                return self.checkBSTRec(node.left) and self.checkBSTRec(node.right)
            else:
                return False
        else:
            return True

    def getSortedDoublyLinkedList(self, node):
        if node is None:
            return
        list = DoublyLinkedList()
        stack = LifoQueue(maxsize=0)
        while node is not None:
            stack.put(node)
            node = node.left

        while stack.qsize() > 0:
            newnode = stack.get()
            list.insert(newnode.value)
            newnode = newnode.right
            while newnode is not None:
                stack.put(newnode)
                newnode = newnode.left
        return list

    def getBBST(self, node):
        if node is None:
            return
        arr = []
        self.convertToSortedArray(node, arr)
        if arr is None:
            return None
        return self.constructBBST(arr, 0, len(arr) - 1)

    def constructBBST(self, arr, st, end):
        if arr is None or len(arr) <= 0 or st > end or st > len(arr) or end > len(arr) or st < 0:
            return None
        if st == end:
            return Node(arr[st])
        mid = (st + end) // 2
        node = Node(arr[mid])
        node.left = self.constructBBST(arr, st, mid - 1)
        node.right = self.constructBBST(arr, mid + 1, end)
        return node

    def inorder_predecessor(self, node):
        if node is None:
            return
        pred = node
        node = node.left
        while node is not None:
            pred = node
            node = node.right
        return pred


if __name__ == '__main__':
    data = [8, 6, 2, 7, 15, 1, 3, 13, 20, 12, 14, 16, 21]
    tree = BSTContinuedSecond()
    root = tree.insert(None, data[0])
    for i in range(1, len(data)):
        tree.insert(root, data[i])

    print(tree.checkBst(root))
    print(tree.checkBSTRec(root))
    list = tree.getSortedDoublyLinkedList(root)
    list.printLinkedList()
    print("Inorder Predecessor: ", end=" ")
    print(tree.inorder_predecessor(root.right.right.right).value)
    balanced_tree_node = tree.getBBST(root)
    if balanced_tree_node is not None:
        balanced_tree = BSTContinuedSecond()
        balanced_tree.insert(balanced_tree_node, balanced_tree_node.value)
        balanced_tree.preorder(balanced_tree_node)
        print()
        balanced_tree.inorder(balanced_tree_node)