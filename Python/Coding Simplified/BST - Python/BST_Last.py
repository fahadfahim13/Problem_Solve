import math
from BST_Continued_second import BSTContinuedSecond
from Binary_Tree_Python.Node import Node


class BSTLast(BSTContinuedSecond):
    def deleteOutRange(self, node, minimum, maximum):  # Time complexity O(n) as we're traversing the whole tree.
        if node is None:  # Space complexity: O(h), h -> height of tree.
            return None  # As the stack size will be maximum h
        node.left = self.deleteOutRange(node.left, minimum, maximum)
        node.right = self.deleteOutRange(node.right, minimum, maximum)
        if node.value < minimum:
            return node.right
        elif node.value > maximum:
            return node.left
        else:
            return node

    def createTreeFromPreorder(self, arr, start, end):
        if start > end:
            return None
        if start == end:
            return Node(arr[start])
        node = Node(arr[start])
        big_index = end + 1
        for ix in range(start + 1, end + 1):
            if arr[ix] > node.value:
                big_index = ix
                break
        node.left = self.createTreeFromPreorder(arr, start + 1, big_index - 1)
        node.right = self.createTreeFromPreorder(arr, big_index, end)
        return node

    def createTreeFromPostorder(self, arr, start, end):
        if start > end:
            return None
        if start == end:
            return Node(arr[start])
        node = Node(arr[end])
        low_point = start - 1
        for i in range(end, start - 1, -1):
            if arr[i] < node.value:
                low_point = i
                break
        node.left = self.createTreeFromPostorder(arr, start, low_point)
        node.right = self.createTreeFromPostorder(arr, low_point + 1, end - 1)
        return node

    def closestElement(self, node, val):
        if node is None:
            return None
        min_diff = math.inf
        ans_node = None

        while node is not None:
            curr_diff = math.fabs(node.value - val)
            if curr_diff < min_diff:
                min_diff = curr_diff
                ans_node = node.value
            if val < node.value:
                node = node.left
            elif val > node.value:
                node = node.right
            else:
                break
        return ans_node


if __name__ == '__main__':
    arr = [8, 6, 7, 2, 5, 3, 15, 12, 20]
    tree = BSTLast()
    root = tree.insert(None, arr[0])
    for idx in range(1, len(arr)):
        tree.insert(root, arr[idx])

    tree.inorder(root)
    tree.deleteOutRange(root, 4, 12)
    print()
    tree.inorder(root)
    print()
    new_tree = BSTLast()
    postorder = [2, 5, 9, 8, 4, 12, 20, 15, 10]
    # preorder = [10, 4, 2, 8, 5, 9, 15, 12, 20]
    new_root = new_tree.createTreeFromPostorder(postorder, 0, len(postorder) - 1)
    # new_root = new_tree.createTreeFromPreorder(preorder, 0, len(preorder) - 1)
    new_tree.inorder(new_root)
    print()
    new_tree.preorder(new_root)
    print()
    print(new_tree.closestElement(new_root, 5))
