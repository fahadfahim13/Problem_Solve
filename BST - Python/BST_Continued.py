from BST import BST
from queue import LifoQueue


class BST_Continued(BST):
    def existPair(self, node, sum):
        if node is None:
            return False
        if self.search(node, sum - node.value):
            return True
        else:
            return self.existPair(node.left, sum) or self.existPair(node.right, sum)

    def existPairWithSet(self, node, sum, set):
        if node is None:
            return False
        if str(sum - node.value) in set:
            return True
        else:
            set[str(node.value)] = 1
            return self.existPairWithSet(node.left, sum, set) or self.existPairWithSet(node.right, sum, set)

    def convertToSortedArray(self, node, arr):
        if node is None:
            return
        self.convertToSortedArray(node.left, arr)
        arr.append(node.value)
        self.convertToSortedArray(node.right, arr)

    def existTripletSum(self, node, sum):
        if node is None:
            return False
        arr = []
        self.convertToSortedArray(node, arr)
        for i in range(0, len(arr) - 1):
            start = i + 1
            end = len(arr) - 1
            while start < end:
                c_s = arr[i] + arr[start] + arr[end]
                if c_s < sum:
                    start = start + 1
                elif c_s > sum:
                    end = end - 1
                else:
                    return True

        return False

    def LCA(self, node, a, b):
        if node is None:
            return None
        if (a <= node.value <= b) or (b <= node.value <= a):
            return node
        elif a > node.value and b > node.value:
            return self.LCA(node.right, a, b)
        else:
            return self.LCA(node.left, a, b)

    def KthSmallest(self, node, k):
        if node is None:
            return -1

        count = 0
        stack = LifoQueue(maxsize=0)
        while node is not None:
            stack.put(node)
            node = node.left

        while stack.qsize() > 0:
            newnode = stack.get()
            count = count + 1
            if count == k:
                return newnode.value
            if newnode.right is not None:
                newnode = newnode.right
                while newnode is not None:
                    stack.put(newnode)
                    newnode = newnode.left

        return -1

    def KthLargest(self, node, k):
        if node is None or k < 1:
            return -1

        count = 0
        stack = LifoQueue(maxsize=0)
        while node is not None:
            stack.put(node)
            node = node.right

        while stack.qsize() > 0:
            newnode = stack.get()
            count = count + 1
            if count == k:
                return newnode.value
            newnode = newnode.left
            while newnode is not None:
                stack.put(newnode)
                newnode = newnode.right

        return -1

    def checkEqual(self, node, node2):
        if node is None and node2 is None:
            return True
        elif node is None or node2 is None:
            return False
        elif node.value != node2.value:
            return False
        else:
            return self.checkEqual(node.left, node2.left) and self.checkEqual(node.right, node2.right)


if __name__ == '__main__':
    # data = [8, 3, 6, 10, 4, 7, 1, 14, 13]
    data = [8, 6, 2, 7, 15, 1, 3, 13, 20, 12, 14, 16, 21]
    data2 = [8, 6, 2, 7, 15, 1, 3, 13, 20, 12, 14, 16, 21]
    tree = BST_Continued()
    root = tree.insert(None, data[0])
    for i in range(1, len(data)):
        tree.insert(root, data[i])

    tree2 = BST_Continued()
    root2 = tree2.insert(None, data2[0])
    for i in range(1, len(data2)):
        tree2.insert(root2, data2[i])

    arr = []
    tree.convertToSortedArray(root, arr)
    print(arr)
    print(tree.existTripletSum(root, -1))
    lca = tree.LCA(root, 15, 21)
    if lca is not None:
        print(lca.value)

    print(tree.KthSmallest(root, 3))
    print(tree.KthLargest(root, 5))
    print(tree.checkEqual(root, root2))